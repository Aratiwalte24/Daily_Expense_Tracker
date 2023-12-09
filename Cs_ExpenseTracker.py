from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry

ltt = []
check, total, z = 0, 0, 0
list1 = []
listv = []

table_name = "expense_tracker"
conn = sqlite3.connect(r"Database\ExpenseTracker.db")
cur = conn.cursor()


def initial():
    global table_name
    try:
        cur.execute("CREATE TABLE " + str(
            table_name) + " (Date_Of_Payment text,Method_Of_Payment text, Paid_To text,Description text,Amount_Paid REAL)")
    except sqlite3.OperationalError:
        pass


def tables():
    global list1
    list1 = []
    cur.execute('SELECT name from sqlite_master where type="table"')
    dta = cur.fetchall()

    for a in dta:
        s = a[0]
        if s in list1:
            pass
        else:

            list1.append(a[0])



def name():
    global table_name
    table_name = ""
    table_name = table_entry.get()
    conn = sqlite3.connect(r"Database\ExpenseTracker.db")
    cur = conn.cursor()
    try:

        cur.execute("CREATE TABLE " + str(
            table_name) + " (Date_Of_Payment text,Method_Of_Payment text, Paid_To text,Description text,Amount_Paid REAL)")
        messagebox.showinfo("SUCCESS", "Table " + str(table_name) + " has been created")
        _entry = StringVar()
        _entry.set("Current Table(in use): " + table_name)
        Entry(screen, width=35, textvariable=_entry, state=DISABLED, relief=SOLID, bg="black", fg="white").place(x=265,
                                                                                                                 y=100)
        tot = 0
        cur.execute("SELECT Amount_Paid FROM " + table_name)
        amt = cur.fetchall()
        for amount in amt:
            tot += int(amount[0])

        screen.title("Current Total Expense : Rupees " + str(tot))
        conn.commit()
        conn.close()
        new_screen2.destroy()
        win.destroy()
        manage()
    except sqlite3.OperationalError:
        messagebox.showwarning("WARNING", "PLEASE ENTER A VALID TABLE NAME")


def create_table():
    global table_entry
    global new_screen2
    new_screen2 = Toplevel(screen)
    new_screen2.iconbitmap(r'Requirements\icons8-money-box-50.ico')
    new_screen2.title("Create New Table")
    Label(new_screen2, text="Please enter the name of the new table").pack()

    table_entry = Entry(new_screen2, width=30)
    table_entry.pack()
    Button(new_screen2, text="ENTER", command=name).pack()


def submit(data_list):
    check = 0
    for i in data_list:
        if i.get() == "":
            pass
        else:
            check += 1

    try:

        if check == 4:
            global total


            conn = sqlite3.connect(r"Database\ExpenseTracker.db")
            cur = conn.cursor()

            cur.execute("INSERT INTO " + str(
                table_name) + " VALUES (:Date_Of_Payment,:Method_of_Payment,:Paid_To,:Description,:Amount_Paid)",
                        {'Date_Of_Payment': (data_list[0]).get(),'Method_of_Payment':Method_Of_Payment_Entry.get(),
                         'Paid_To': (data_list[1]).get(), 'Description': (data_list[2]).get(),
                         'Amount_Paid': float(data_list[3].get())})
            conn.commit()

            messagebox.showinfo("Success", "Successfully added the record to the database")
            for i in data_list:
                i.delete(0, END)
            tot = 0

            cur.execute("SELECT Amount_Paid FROM " + table_name)
            amt = cur.fetchall()
            for amount in amt:
                tot += amount[0]

            screen.title("Current Total Expense : Rupees " + str(tot))
            conn.close()

        else:
            messagebox.showwarning("WARNING!", "One or more than one fields are empty\nPlease Check Again")
            pass

    except ValueError:
        messagebox.showwarning("WARNING!", "Amount Paid must be integer number\nPlease Check Again")

    new_screen.destroy()
    new_Records()
def main_screen():
    global screen
    global table_name
    global _entry
    global render4
    global render5
    conn = sqlite3.connect(r"Database\ExpenseTracker.db")
    cur = conn.cursor()
    tot = 0
    cur.execute("SELECT Amount_Paid FROM " + table_name)
    amt = cur.fetchall()
    for amount in amt:
        tot += int(amount[0])
    screen = Tk()
    screen.iconbitmap(r'Requirements\icons8-money-box-50.ico')
    screen.geometry("700x500+150+135")
    screen.title("Current Total Expense : Rupees " + str(tot))
    conn.commit()
    conn.close()
    my_img = ImageTk.PhotoImage(Image.open(r"Requirements\Expense-Tracker.png"))
    button1_img = ImageTk.PhotoImage(Image.open(r"Requirements\button1.png"))
    button_img = ImageTk.PhotoImage(Image.open(r"Requirements\button.png"))
    bg_img = ImageTk.PhotoImage(Image.open(r"Requirements\bg2.png"))
    load = Image.open(r"Requirements\Expense-Tracker.png")
    image = load.resize((700, 80), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(image)
    load3 = Image.open(r"Requirements\button.png")
    image3 = load3.resize((276, 50), Image.ANTIALIAS)
    render3 = ImageTk.PhotoImage(image3)
    load1 = Image.open(r"Requirements\button1.png")
    image1 = load1.resize((276, 50), Image.ANTIALIAS)
    render1 = ImageTk.PhotoImage(image1)
    load2 = Image.open("Requirements\exit.png")
    image2 = load2.resize((100, 40), Image.ANTIALIAS)
    render2 = ImageTk.PhotoImage(image2)
    load4 = Image.open(r"Requirements\create_new_table.png")
    image4 = load4.resize((176, 50), Image.ANTIALIAS)
    render4 = ImageTk.PhotoImage(image4)
    load5 = Image.open(r"Requirements\update.png")
    image5 = load5.resize((176, 50), Image.ANTIALIAS)
    render5 = ImageTk.PhotoImage(image5)
    load6 = Image.open(r"Requirements\manage.png")
    image6 = load6.resize((176, 50), Image.ANTIALIAS)
    render6 = ImageTk.PhotoImage(image6)
    Label(screen, image=bg_img).place(x=0, y=0, relwidth=1)
    Label(screen, image=render, bg="#576E8D", relief=GROOVE, bd=0).place(x=0, y=0, relwidth=1)
    Button(screen, image=render3, command=new_Records, bg="#BDC9D9", relief=SOLID, bd=1).place(x=550, y=150)
    Button(screen, image=render1, command=previous_Records, bg="#E1E4EB", relief=SOLID, bd=1).place(x=550, y=250)
    Button(screen, image=render2, command=screen.quit, bg="#EAEDF2", bd=0, relief=SUNKEN).place(x=650, y=430)
    Button(screen, image=render6, command=manage, relief=SOLID, bd=1).place(x=600, y=345)
    _entry = StringVar()
    _entry.set("Current Table(in use): " + table_name)
    Entry(screen, width=35, textvariable=_entry, state=DISABLED, relief=SOLID, bg="black", fg="white").place(x=580,
                                                                                                             y=100)

    screen.mainloop()
def manage():
    global win
    global lt
    global lst
    global n
    tables()
    win = Toplevel(screen)
    win.iconbitmap(r'Requirements\icons8-money-box-50.ico')
    win.title("MANAGE TABLES")
    Button(win, image=render4, command=create_table, relief=SOLID, bd=1).pack(pady=30, expand=True)
    Button(win, text="DELETE SELECTED TABLE", font=("BOLD", 10), bg="red", command=remove_table, relief=SUNKEN,
           bd=1).pack(padx=30, ipadx=30, pady=10, ipady=10)

    Label(win, text="Choose the Table that you want to use:", font=("Bold", 15)).pack()
    lt = []
    lst = []
    n = 0

    for n in range(0, len(list1), 1):
        lt.append("var" + str(n))

    n__ = 0
    for a_ in list1:
        lt[n__] = IntVar()
        Checkbutton(win, text=str(a_), variable=lt[n__]).pack(anchor=NW, ipadx=50)
        lst.append(a_)
        n__ += 1
    Button(win, text="Done", font=("BOLD", 15), command=change, relief=SOLID, bd=1).pack(ipadx=90, padx=30, pady=10)
    win.mainloop()
def select():
    global p
    global z
    global listv
    listv = []
    m = 0
    selection = my_tree.focus()
    name_box1.delete(0, END)
    name_box2.delete(0, END)
    name_box3.delete(0, END)
    name_box4.delete(0, END)
    name_box5.delete(0, END)


    values = my_tree.item(selection, 'values')
    if selection == "":
        messagebox.showwarning("Attention", "You must select atleast one record to perform this action")
    else:
        for k in range(0, 5):
            listv.append(values[k])

        try:
            name_box1.insert(0, values[0])
            name_box2.set(values[1])
            name_box3.insert(0, values[2])
            name_box4.insert(0, values[3])
            name_box5.insert(0, values[4])
            z = 1
        except IndexError:
            pass
def update1():
    global p
    global z
    global listv

    m = 0
    selection = my_tree.focus()
    if [name_box1.get(), name_box2.get(), name_box3.get(), name_box4.get(), str(name_box5.get())] == listv:
        messagebox.showinfo("Attention", "Seems as if you didn't make any change to the existing record")
    else:

        if z == 1 and selection != "":
            z = 0
            try:

                conn = sqlite3.connect(r"Database\ExpenseTracker.db")
                cur = conn.cursor()
                selection = my_tree.focus()
                values = my_tree.item(selection, text="", values=(
                name_box1.get(), name_box2.get(), name_box3.get(), name_box4.get(), name_box5.get()))
                x = my_tree.selection()
                for record in x:
                    cur.execute("UPDATE " + str(
                    table_name) + " SET Date_Of_Payment = '"+str(name_box1.get()) + "' , Method_of_Payment = '"+str(name_box2.get()) +"' , Paid_To = '"+ str(name_box3.get())+"' , Description = '"+str(name_box4.get())+"' , Amount_Paid = "+str(name_box5.get())+" WHERE oid = " + str(ltt[(int(record) - 1)])+" ;")
                name_box1.delete(0, END)
                # name_box2.delete(0, END)
                name_box3.delete(0, END)
                name_box4.delete(0, END)
                name_box5.delete(0, END)
                tot = 0
                cur.execute("SELECT Amount_Paid FROM " + table_name)
                amt = cur.fetchall()
                for amount in amt:
                    tot += amount[0]

                screen.title("Current Total Expense : Rupees " + str(tot))
                conn.commit()
                conn.close()
            except sqlite3.OperationalError:
                messagebox.showwarning("WARNING!", "Amount Paid must be a number\nPlease Check Again")
        else:

            messagebox.showwarning("Attention", "Seems You didn't select any record\nPlease Check Again")





def remove():
    ch = 0
    conn = sqlite3.connect(r"Database\ExpenseTracker.db")
    cur = conn.cursor()
    x = my_tree.selection()

    for record in x:

        cur.execute("DELETE FROM " + str(table_name) + " WHERE oid=" + str(ltt[(int(record) - 1)]))
        my_tree.delete(record)
        ch += 1
    if ch == 0:
        messagebox.showwarning("Attention", "You must select at least one record to perform this action")
    tot = 0
    cur.execute("SELECT Amount_Paid FROM " + table_name)
    amt = cur.fetchall()
    for amount in amt:
        tot += int(amount[0])

    screen.title("Current Total Expense : Rupees " + str(tot))
    conn.commit()
    conn.close()


def remove_table():
    _i = 0
    _n = 0
    conn = sqlite3.connect(r"Database\ExpenseTracker.db")
    cur = conn.cursor()
    global table_name


    for _i in range(0, len(lst)):

        if (lt[_i].get()) == 1:
            table_name = lst[_n]
            if table_name == "expense_tracker":
                messagebox.showwarning("Warning", "Can't Delete The Default Table 'expense_tracker'")

            else:
                cur.execute("DROP TABLE " + table_name)
                messagebox.showinfo("SUCCESS", "Successfully Delete Table " + table_name)
                table_name="expense_tracker"


                _entry = StringVar()
                _entry.set("Current Table(in use): " + table_name)
                Entry(screen, width=35, textvariable=_entry, state=DISABLED, relief=SOLID, bg="black",
                      fg="white").place(x=265,
                                        y=100)

                tot = 0
                cur.execute("SELECT Amount_Paid FROM " + table_name)
                amt = cur.fetchall()
                for amount in amt:
                    tot += int(amount[0])
                screen.title("Current Total Expense : Rupees " + str(tot))
                win.destroy()
                manage()
            break
        _n += 1


    conn.commit()
    conn.close()


def change():
    _i = 0
    _n = 0
    global table_name
    tempp = 0

    for _i in range(0, len(lst)):

        if (lt[_i].get()) == 1:
            table_name = lst[_n]
            messagebox.showinfo("SUCCESS", "The current table has been changed to- '" + table_name + "'")
            entry = StringVar()
            _entry.set("Current Table(in use): " + table_name)
            Entry(screen, width=35, textvariable=_entry, state=DISABLED, relief=SOLID, bg="black", fg="white").place(
                x=265, y=100)
            tot = 0
            cur.execute("SELECT Amount_Paid FROM " + table_name)
            amt = cur.fetchall()
            for amount in amt:
                tot += int(amount[0])
            screen.title("Current Total Expense : Rupees " + str(tot))

            tempp += 1
            break

        _n += 1
    if tempp == 0:
        messagebox.showwarning("WARNING", "SELECT AT LEAST ONE TABLE TO WORK ON")
        win.destroy()
        manage()
    else:
        win.destroy()
        tot = 0
        cur.execute("SELECT Amount_Paid FROM " + table_name)
        amt = cur.fetchall()
        for amount in amt:
            tot += int(amount[0])
            screen.title("Current Total Expense : Rupees " + str(tot))


def new_Records():
    global new_screen
    global Method_Of_Payment_Entry

    new_screen = Toplevel(screen)
    new_screen.iconbitmap(r'Requirements\icons8-money-box-50.ico')
    new_screen.title("New Records")
    Amount_Paid = DoubleVar()
    Date_Of_Payment_Entry = DateEntry(new_screen, width=12,
background='darkblue', foreground='white', borderwidth=2)

    Date_Of_Payment_Entry.grid(row=0, column=1, padx=20)
    Method_Of_Payment_Entry=StringVar()
    Method_Of_Payment_Entry.set("CASH")
    OptionMenu(new_screen,Method_Of_Payment_Entry,"CASH","CARD","PAYTM","CHEQUE","ONLINE TRANSACTION","PHONE PAY","GOOGLE PAY").grid(padx=30,row=1, column=1)

    Paid_To_Entry = Entry(new_screen, width=100)
    Paid_To_Entry.grid(row=2, column=1)
    Description_Entry = Entry(new_screen, width=100)
    Description_Entry.grid(row=3, column=1)
    Amount_Paid_Entry = Entry(new_screen, width=100, textvariable=Amount_Paid)
    Amount_Paid_Entry.grid(row=4, column=1)

    Label(new_screen, text="DATE OF PAYMENT\n (MM\DD\YY)").grid(row=0, column=0)
    Label(new_screen, text="METHOD OF PAYMENT\n").grid(row=1, column=0)
    Label(new_screen, text="PAID TO").grid(row=2, column=0)
    Label(new_screen, text="DESCRIPTION").grid(row=3, column=0)
    Label(new_screen, text="AMOUNT PAID(In Rupees)").grid(row=4, column=0)

    _list = [Date_Of_Payment_Entry, Paid_To_Entry, Description_Entry, Amount_Paid_Entry]

    conn = sqlite3.connect(r"Database\ExpenseTracker.db")
    cur = conn.cursor()
    Button(new_screen, text="Add Record to Database", command=lambda: submit(_list)).grid(row=5, column=0,
                                                                                          columnspan=2,
                                                                                          pady=10, padx=10,
                                                                                          ipadx=100)
    conn.commit()
    conn.close()
    new_screen.mainloop()


def previous_Records():
    global new_screen1
    global my_tree
    global p
    global name_box1
    global name_box2
    global name_box3
    global name_box4
    global name_box5
    global name_box
    global ltt
    ltt = []

    new_screen1 = Toplevel(screen)
    new_screen1.iconbitmap(r'Requirements\icons8-money-box-50.ico')
    new_screen1.title("Previous Records")

    conn = sqlite3.connect(r"Database\ExpenseTracker.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + table_name)
    records = cur.fetchall()
    cur.execute("SELECT oid FROM " + table_name)
    rec = cur.fetchall()

    for recc in rec:

        ltt.append(recc[0])
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background="white", foreground="black", rowheight=25, fieldbackground="white")
    style.map('Treeview', background=[('selected', 'green')])

    tree_scroll = Scrollbar(new_screen1)
    tree_scroll.pack(side=RIGHT, fill=Y)

    my_tree = ttk.Treeview(new_screen1, yscrollcommand=tree_scroll.set)

    tree_scroll.config(command=my_tree.yview)

    my_tree.tag_configure("oddrow", background="WHITE")
    my_tree.tag_configure("evenrow", background="lightblue")
    my_tree['columns'] = ('Date Of Payment', 'Method Of Payment', 'Paid To', 'Description', 'Amount Paid(In Rupees)')
    my_tree.column("#0", width=0, anchor=W, minwidth=0, stretch=NO)
    my_tree.column("Date Of Payment", width=150, anchor=W, minwidth=25 )
    my_tree.column("Method Of Payment", width=150, anchor=W, minwidth=25)
    my_tree.column("Paid To", width=150, anchor=W, minwidth=25)
    my_tree.column("Description", width=150, anchor=W, minwidth=50)
    my_tree.column("Amount Paid(In Rupees)", width=150, anchor=W, minwidth=25)

    my_tree.heading("#0", text="Label", anchor=W)
    my_tree.heading("Date Of Payment", text="Date Of Payment (MM/DD/YY)", anchor=W)
    my_tree.heading("Method Of Payment", text="Method Of Payment", anchor=W)
    my_tree.heading("Paid To", text="Paid To", anchor=W)
    my_tree.heading("Description", text="Description", anchor=W)
    my_tree.heading("Amount Paid(In Rupees)", text="Amount Paid(In Rupees)", anchor=W)

    p, q = 1, 0
    for record in records:
        if p % 2 == 0:
            my_tree.insert(parent='', index='end', iid=p, text='Parent', values=record, tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=p, text='Parent', values=record, tags=('oddrow',))

        p += 1
    my_tree.pack(padx=10, ipadx=50, ipady=20)
    Button(new_screen1, text="DELETE THE SELECTED RECORD", bg="red", font=("BOLD", 15), command=remove).pack(padx=10,
                                                                                                             pady=10,
                                                                                                             ipadx=220)
    Label(new_screen1, text="UPDATE RECORDS :-", font=("BOLD", 15)).pack(pady=10)
    add_frame = Frame(new_screen1)
    add_frame.pack(pady=10, ipady=10)

    Button(new_screen1, text="PRESS THIS BUTTON TO EDIT THE SELECTED RECORD", bg="purple",font=("BOLD",15),command=select).pack(padx=10,
                                                                                                                pady=10,
                                                                                                                ipadx=100)

    Button(new_screen1, text="UPDATE RECORD", bg="blue", font=("BOLD", 15), command=update1).pack(padx=25, pady=10,
                                                                                                 ipadx=300)

    n1 = Label(add_frame, text="Date Of Payment (MM/DD/YY)")
    n1.grid(row=1, column=0)
    n2 = Label(add_frame, text="Method Of Payment")
    n2.grid(row=1, column=1)
    n3 = Label(add_frame, text="Paid To")
    n3.grid(row=1, column=2)
    n4 = Label(add_frame, text="Description")
    n4.grid(row=1, column=3)
    n5 = Label(add_frame, text="Amount Paid")
    n5.grid(row=1, column=4)

    name_box = IntVar()
    name_box.set("")
    name_box1 = DateEntry(add_frame,background='darkblue', foreground='white', borderwidth=2)
    name_box1.grid(row=2, column=0)

    name_box2 = StringVar()
    name_box2.set("CASH")
    OptionMenu(add_frame, name_box2,"CASH","CARD","PAYTM","CHEQUE","ONLINE TRANSACTION").grid(row=2, column=1)
    name_box3 = Entry(add_frame)
    name_box3.grid(row=2, column=2)
    name_box4 = Entry(add_frame)
    name_box4.grid(row=2, column=3)
    name_box5 = Entry(add_frame, textvariable=name_box)
    name_box5.grid(row=2, column=4)

    conn.commit()
    conn.close()


initial()
main_screen()

conn.commit()
conn.close()
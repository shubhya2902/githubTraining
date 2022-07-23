from tkinter import *
from tkinter import messagebox, ttk
from tkinter.ttk import Combobox
from PIL import Image,ImageTk
import mysql.connector


# registration page

def reg():

    def message2():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="cafe"
        )
        mycursor = mydb.cursor()

        name = e11.get()
        mail = e14.get()
        pwd = e12.get()
        pwd2 = e13.get()

        if pwd == pwd2:
# insert newly register values
            sql = "insert into reg VALUES (%s,%s,%s)"
            val = (name, mail, pwd)
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("LOGIN", "REGISTER SUCCESSFULLY")
            abc(4)
        else:
            messagebox.showerror("ERROR", "BOTH PASSWORDS DIDN'T MATCH . TRY AGAIN")

    def clear():
        e11.delete(0,END)
        e12.delete(0,END)
        e13.delete(0,END)
        e14.delete(0,END)

    global root2
    root2 = Tk()
    root2.geometry("540x540")
    root2.configure(background="black",highlightthickness="8")
    # image = Image.open("C:\\Users\\LENOVO\\Downloads\\retro(logo).jpg",)
    # photo = ImageTk.PhotoImage(image)
    # label = Label(image=photo)
    # label.pack()


    l11 = Label(root2,text= "RESTO CAFE",fg="red",bg="black",font=("broadway",20,"bold"))
    l11.place(x=140,y=10)
    Label(root2,text="REGISTRATION",fg="red",bg="black",font=("broadway",20,"bold")).place(x=120,y=50)

    l12 = Label(root2, text="USER NAME",fg="white",bg="black", font=("italic", 13, "bold"))
    l12.place(x=100, y=100)
    Label(root2, text="*", fg="red",bg="black", font=("bold", 13)).place(x=205, y=100)
    e11 = Entry(root2, font=("broadway", 13, "bold"))
    e11.place(x=100, y=130)

    l15 = Label(root2, text="EMAIL ID", fg="white",bg="black", font=("italic", 13, "bold"))
    l15.place(x=100, y=170)
    Label(root2, text="*", fg="red",bg="black", font=("bold", 13)).place(x=175, y=170)
    e14 = Entry(root2, font=("broadway", 13, "bold"))
    e14.place(x=100, y=200)

    l13 = Label(root2, text="PASSWORD", fg="white",bg="black", font=("italic", 13, "bold"))
    l13.place(x=100, y=240)
    Label(root2, text="*", fg="red",bg="black", font=("bold", 13)).place(x=205, y=240)
    e12 = Entry(root2, font=("broadway",13, "bold"))
    e12.place(x=100, y=270)

    l14 = Label(root2, text="CONFIRM PASSWORD",fg="white",bg="black", font=("italic", 13, "bold"))
    l14.place(x=100, y=310)
    Label(root2, text="*", fg="red",bg="black", font=("bold", 13)).place(x=285, y=310)
    e13 = Entry(root2, font=("broadway", 13, "bold"))
    e13.place(x=100, y=340)

    b11 = Button(root2,text="Register", fg="black",bg="orange",font =("broadway",14,"bold"),command=lambda: message2())
    b11.place(x=50,y=420)
    b11.configure(padx=40)

    b13 = Button(root2,text="Clear", fg="black",bg="orange",font =("broadway",14,"bold"),command=lambda: clear())
    b13.place(x=310,y=420)
    b13.configure(padx=40)

    root2.mainloop()


# login page

def login():
    def clear():
        e1.delete(0, END)
        e2.delete(0, END)

    def insert():
        user = e1.get()
        pwd = e2.get()

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="cafe")

        mycursor = mydb.cursor()

# check validation is register id and password match with database

        sql = "select name,pwd from reg where name = %s and pwd = %s"
        mycursor.execute(sql, [ (user) , (pwd)])
        result = mycursor.fetchall()
        if result:
            messagebox.showinfo("login", "Login Successful")
            win.destroy()
            main()
            return True
        else:
            messagebox.showerror("fail", "Invalid ID or PASSWORD")
            return False


    global win
    win = Tk()
    win.title("Resto Cafe")
    win.geometry("400x500")
    win.configure(background="grey")
    image = Image.open("C:\\Users\\LENOVO\\Downloads\\download.png",)
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    label.pack()

    Label(win,text="              RESTO CAFE              ",bg="black",fg="white",font=("broadway",20,"bold")).place(x=0,y=460)

    l1 = Label(win,text="ID",bg="black",fg="white",font=("bold",15))
    l1.place(x=60,y=250)
    e1 = Entry(win,font=("bold",16))
    e1.place(x=60,y=275)

    l2 = Label(win,text="PASSWORD",bg="black",fg="white",font=("bold",15))
    l2.place(x=60,y=310)
    e2 = Entry(win,font=("bold",16))
    e2.place(x=60,y=335)

    b1 = Button(win,text="LOGIN",bg="grey",fg="black",font=("bold",14),command=insert)
    b1.place(x=120,y=370)
    b2 = Button(win,text="CLEAR",bg="grey",fg="black",font=("bold",14),command=clear)
    b2.place(x=210,y=370)
    b3 = Button(win,text="SIGN-UP",bg="grey",fg="black",font=("bold",14),command=lambda:abc(5))
    b3.place(x=150,y=415)



    win.mainloop()

# main page

def main():
    global root
    root = Tk()
    root.title("RESTO CAFE")
    root.geometry("1500x800")
    root.configure(background="black")
    image = Image.open("C:\\Users\\LENOVO\\Downloads\\black_bg.jpg",)
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    label.pack()


    l1 = Label(root,text="Order No",fg="white",bg="black",font=("Helvetica",15,"bold"))
    l1.place(x=150,y=100)
    e1 = Entry(root,font=("Helvetica",10,"bold"))
    e1.place(x=150,y=140)



    Label(root,text="MENU",fg="white",bg="black",font=("broadway",22,"bold")).place(x=690,y=100)

    global content
    btn = IntVar()
    global member
    member = []

    def xyz():
        global selection
        selection = btn.get()
        global cb

        if selection == 1:
            l = ["Cold coffee", "Hot coffee","White coffee"]
            cb = Combobox(root, values=l, font=("aerial", 13, "bold"))
            cb.place(x=380, y=350)

        if selection == 2:
            l = ["Mexican pizza","Farm house pizza","Double cheese pizza"]
            cb = Combobox(root, values=l, font=("aerial", 13, "bold"))
            cb.place(x=380, y=350)

        if selection == 3:
            l = ["Resto special", "Veg", "Veg grilled","Non-veg","Non-veg grilled"]
            cb = Combobox(root, values=l, font=("aerial", 13, "bold"))
            cb.place(x=380, y=350)

        if selection == 4:
            l = ["Masala pasta", "White pasta", "Pasta with cheese"]
            cb = Combobox(root, values=l, font=("aerial", 13, "bold"))
            cb.place(x=380, y=350)

        if selection == 5:
            l = ["Badam shake", "Milk shake", "Chocolate shake","Mango shake"]
            cb = Combobox(root, values=l, font=("aerial", 13, "bold"))
            cb.place(x=380, y=350)

        if selection == 6:
            l = ["French fries", "Masala fries", "Peri-peri fries"]
            cb = Combobox(root, values=l, font=("aerial", 13, "bold"))
            cb.place(x=380, y=350)

        if selection == 7:
            l = ["Virgin mojito", "Pitch", "Peru"]
            cb = Combobox(root, values=l, font=("aerial", 13, "bold"))
            cb.place(x=380, y=350)

        if selection == 8:
            l = ["Mango", "Pista", "Chocolate"]
            cb = Combobox(root, values=l, font=("aerial", 13, "bold"))
            cb.place(x=380, y=350)

        if selection == 9:
            l = ["Mexican nachos", "American nachos"]
            cb = Combobox(root, values=l, font=("aerial", 13, "bold"))
            cb.place(x=380, y=350)
           
        
# insert price of the item in price box when it click on item in listbox


    def insert_price(event):
        val = cb.get()
        # if val == "Cold coffee":
        #     e3.insert(END,"30")
        # elif val == "Hot coffee":
        #     e3.insert(END,"40")
        # elif val == "White coffee":
        #     e3.insert(END,"30")
        # elif val == "Mexican pizza":
        #     e3.insert(END, "180")
        # elif val == "Farm house pizza":
        #     e3.insert(END,"200")
        # elif val == "Double cheese pizza":
        #     e3.insert(END,"220")
        # elif val == "Resto special":
        #     e3.insert(END,"120")
        # elif val == "Veg":
        #     e3.insert(END,"60")
        # elif  val == "Veg-grilled":
        #     e3.insert(END,"80")
        # elif val == "Non-veg":
        #     e3.insert(END,"80")
        # elif val == "Non-veg grilled":
        #     e3.insert(END,"100")
        # elif val == "Masala pasta":
        #     e3.insert(END,"120")
        # elif val == "White pasta":
        #     e3.insert(END,"100")
        # elif val == "Pasta with cheese":
        #     e3.insert(END,"140")
        # elif val == "Badam shake":
        #     e3.insert(END,"80")
        # elif val == "Milk shake":
        #     e3.insert(END,"70")
        # elif val == "Chocolate shake":
        #     e3.insert(END,"80")
        # elif val == "Mango shake":
        #     e3.insert(END,"100")
        # elif val ==  "French fries":
        #     e3.insert(END,"70")
        # elif val == "Masala fries":
        #     e3.insert(END,"80")
        # elif val == "Peri-peri fries":
        #     e3.insert(END,"100")
        # elif val == "Virgin mojito":
        #     e3.insert(END,"50")
        # elif val == "Pitch":
        #     e3.insert(END, "50")
        # elif val == "Peru":
        #     e3.insert(END,"50")
        # elif val == "Mango":
        #     e3.insert(END, "130")
        # elif val == "Pista":
        #     e3.insert(END, "110")
        # elif val == "Chocolate":
        #     e3.insert(END, "120")
        # elif val == "Mexican nachos":
        #     e3.insert(END,"100")
        # elif val == "American nachos":
        #     e3.insert(END,"100")

        m = {
            "Cold coffee":"30","Hot coffee":"40","White coffee":"40",
            "Mexican pizza":"180","Farm house pizza":"200","Double cheese pizza":"220",
            "Resto special":"120","Veg":"60","Veg-grilled":"80","Non-veg":"80","Non-veg grilled":"100",
            "Masala pasta":"120", "White pasta":"100", "Pasta with cheese":"140",
            "Badam shake":"80", "Milk shake":"70", "Chocolate shake":"90","Mango shake":"100",
            "French fries":"70", "Masala fries":"80", "Peri-peri fries":"100",
            "Virgin mojito":"50", "Pitch":"50", "Peru":"50",
            "Mango":"130", "Pista":"110", "Chocolate":"120",
            "Mexican nachos":"100", "American nachos":"100"
            }
        for item_name,price in m.items():
            if item_name == val:
                e3.insert(END,price)

    r1 = Radiobutton(root,text="COFFEE",fg="black",bg="white",font=("broadway",13,"bold"),value="1",variable=btn,command=xyz)
    r1.place(x=200,y=200)

    r2 = Radiobutton(root,text="PIZZA",fg="black",bg="white",font=("broadway",13,"bold"),value="2",variable=btn,command=xyz)
    r2.place(x=320,y=200)

    r3 = Radiobutton(root,text="SANDWICH",fg="black",bg="white",font=("broadway",13,"bold"),value="3",variable=btn,command=xyz)
    r3.place(x=425,y=200)

    r4 = Radiobutton(root,text="PASTA",fg="black",bg="white",font=("broadway",13,"bold"),value="4",variable=btn,command=xyz)
    r4.place(x=580,y=200)

    r5 = Radiobutton(root,text="SHAKE",fg="black",bg="white",font=("broadway",13,"bold"),value="5",variable=btn,command=xyz)
    r5.place(x=690,y=200)

    r2 = Radiobutton(root,text="FRIES",fg="black",bg="white",font=("broadway",13,"bold"),value="6",variable=btn,command=xyz)
    r2.place(x=250,y=250)

    r3 = Radiobutton(root,text="MOCKTAIL",fg="black",bg="white",font=("broadway",13,"bold"),value="7",variable=btn,command=xyz)
    r3.place(x=350,y=250)

    r4 = Radiobutton(root,text="DESSERT",fg="black",bg="white",font=("broadway",13,"bold"),value="8",variable=btn,command=xyz)
    r4.place(x=500,y=250)

    r5 = Radiobutton(root,text="NACHOS",fg="black",bg="white",font=("broadway",13,"bold"),value="9",variable=btn,command=xyz)
    r5.place(x=630,y=250)

    cd = Combobox(root,font=("aerial", 13, "bold"))
    cd.place(x=380, y=350)

    Label(root, text="QUANTITY", fg="black", bg="white", font=("broadway", 15, "bold")).place(x=300, y=450)
    e2 = Entry(root,bd=7, width=10, justify='center', font=("aerial", 13, "bold"))
    e2.place(x=310,y=480)
    e2.bind('<FocusIn>',insert_price)

    Label(root, text="PRICE", fg="black", bg="white", font=("broadway", 15, "bold")).place(x=540, y=450)
    e3 = Entry(root,bd=7,width=10, justify = 'center',font=("aerial", 13, "bold"))
    e3.place(x=525,y=480)





    def clear():
        e2.delete(0, END)
        e3.delete(0, END)

# add data in textbox
# insert data in database

    def add():
        a = e2.get()
        val = int(a)

        b = e3.get()
        val1 = int(b)

        t = val*val1
        global tot
        tot = str(t)

        global oder_no
        oder_no = e1.get()

        global item
        item = cb.get()

        global qty
        qty = e2.get()

        global price
        price = e3.get()

        Label(root,text=oder_no).place(x=1110,y=182)
        txtReceipt.insert(END,f"{item}\t    {qty}\t     {price}\t    {tot}\n")


        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="cafe"
        )
        mycursor = mydb.cursor()

        sql = "insert into bill VALUES (%s,%s,%s,%s,%s)"
        val = (oder_no,item,qty,price,tot)
        mycursor.execute(sql, val)
        mydb.commit()


    b1 = Button(root,text="ADD", bg="blue",fg="white",font=("broadway", 15, "bold"),command=add)
    b1.place(x=270,y=650)
    b2 = Button(root,text="CLEAR", bg="blue",fg="white", font=("broadway", 15, "bold"),command=clear)
    b2.place(x=400,y=650)
    b3 = Button(root,text="DELETE", bg="blue",fg="white", font=("broadway", 15, "bold"),)
    b3.place(x=550,y=650)
    b4 = Button(root,text="PRINT BILL", bg="green",font=("broadway", 14, "bold"),command=bill)
    b4.place(x=1140,y=650)
    
    
# display all selected content


    global txtReceipt
    txtReceipt = Text(root, height=30, width=40)
    txtReceipt.place(x=1000,y=150)
    txtReceipt.insert(END, "               RESTO CAFE\n")
    txtReceipt.insert(END,"========================================")
    txtReceipt.insert(END, "\n Order No. :- ")
    txtReceipt.insert(END,"\n\n****************************************")
    txtReceipt.insert(END, "\n   item\t    qty\t     price\t    total\n")
    txtReceipt.insert(END,"****************************************\n\n")



    root.mainloop()
    
    
# bill page


def bill():

    global final
    final = Tk()
    final.title("Bill")
    final.geometry("1050x500")
    final.configure(background="grey")
    Label(final,text="******************************************************************************************************"
                     ,fg="black",bg="grey",font=("bold",20)).place(x=0,y=10)
    Label(final,text="RESTO CAFE",fg="black",bg="grey",font=("broadway",18,"bold")).place(x=390,y=30)
    Label(final,text="******************************************************************************************************",
          fg="black",bg="grey",font=("bold",20)).place(x=0,y=60)

    Label(final,text="Order No.",fg="black",bg="grey",font=("bold",13)).place(x=5,y=130)

    e4 = Entry(final,width=8,bg="grey",fg="black", font=("bold",11))
    e4.place(x=90,y=132)

    global orno
    orno = e4.get()
    
    
# by entering order no we can get data from database available at that order no

# we have to make some changes in block


    def receive():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="cafe")
        mycursor = mysqldb.cursor()

        sql="SELECT * FROM bill where order_no=%s"
        val = orno

        # mycursor.execute("SELECT * FROM bill")

        mycursor.execute(sql,val)
        records = mycursor.fetchall()
        # for i, (order_no,item,qty,price,total) in enumerate(records, start=1):
        #     Listbox.insert("", END, values=(order_no,item,qty,price,total))
        #     mysqldb.close()


    Button(final,text="Get",bg="grey",font=("bold",13),command=receive).place(x=290,y=125)

    Button(final,text="close",font=("bold",13),command=lambda:abc(3)).place(x=950,y=440)

    cols = ('order_no','item','qty','price','total')
    Listbox = ttk.Treeview(final, columns=cols, show='headings')
    for col in cols:
        Listbox.heading(col, text=col)
        Listbox.grid(row=1, column=0)
        Listbox.place(x=20, y=200)

    final.mainloop()
    
    
# for changes windows

def abc(x):
    if x == 1:
        win.destroy()
        main()
    if x == 3:
        final.destroy()
        main()
    if x == 4:
        root2.destroy()
        login()
    if x == 5:
        win.destroy()
        reg()


login()





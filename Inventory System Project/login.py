from tkinter import *
from tkinter import messagebox
import os
import sqlite3
root=Tk()
root.title("Login Screen")
root.attributes("-fullscreen",True)

photo=PhotoImage(file="bar.png")
w=Label(root)
w.configure(image=photo)
w.place(x=0,y=0)

root.configure(bg="black")
varusername=StringVar()
varpassword=StringVar()

def login_clicked():
    sqlite_file="invent.sqlite"
    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    uname=str(varusername.get())
    pwd=str(varpassword.get())

    c.execute("select * from tblogin where username=(?) and password=(?)",(uname,pwd))
    data=c.fetchall()
    if(len(data)==0):
        messagebox.showinfo("Sorry","User does not exist")
    else:
        messagebox.showinfo("Great!!","Login Sucessful!")
        root.destroy()
        os.system("menu.py")
    conn.commit()
    conn.close()

def create_clicked():
    root.destroy()
    os.system("create.py")

def cancel_clicked():
    root.destroy()

titleLabel=Label(root,text="Login Here",font=("Gothic",40)).place(x=500,y=100)
tblusername=Label(root,text="USERNAME",font=("Stencil",30)).place(x=300,y=250)
tblpassword=Label(root,text="PASSWORD",font=("Stencil",30)).place(x=300,y=350)

txtusername=Entry(root,font=("Arial",30),textvariable=varusername)
txtusername.place(x=750,y=250)
txtpassword=Entry(root,font=("Arial",30),show="*",textvariable=varpassword)
txtpassword.place(x=750,y=350)

btnlogin=Button(root,text="LOGIN",font=("Stencil",20),bg='light yellow',command=login_clicked).place(x=100,y=500)
btncreate=Button(root,text="CREATE USER",font=("Stencil",20),bg='light yellow',command=create_clicked).place(x=540,y=500)
btncancel=Button(root,text="CANCEL",font=("Stencil",20),bg='light yellow',command=cancel_clicked).place(x=1100,y=500)
txtusername.focus

root.mainloop()

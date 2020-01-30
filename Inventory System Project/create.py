from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
root.title("Create Username")
root.attributes("-fullscreen",True)
root.configure(bg="aquamarine")

photo=PhotoImage(file="create.png")
w=Label(root)
w.configure(image=photo)
w.place(x=0,y=0)
varusername=StringVar()
varpassword=StringVar()

def create_clicked():
    sqlite_file='invent.sqlite'
    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    uname=str(varusername.get())
    upass=str(varpassword.get())

    c.execute("select * from tblogin where username=(?) and password=(?)",(uname,upass))
    data=c.fetchall()
    if(len(data)==0):
        c.execute("insert into tblogin(username,password) values(?,?)",(uname,upass))
        messagebox.showinfo("Great!!","User Created")
    else:
        messagebox.showinfo("Error","User already exists!!")
    conn.commit()
    conn.close()
def clear_clicked():
    varusername.set("")
    varpassword.set("")

def back_clicked():
    import os
    root.destroy()
    os.system("login.py")

def exit_clicked():
    root.destroy()

title=Label(root,text="SET USERNAME AND PASSWORD",font=("MV boli bold",35)).place(x=300,y=100)
lblusername=Label(root,text="USERNAME",font=("MV Boli bold",25)).place(x=300,y=250)
lblpassword=Label(root,text="PASSWORD",font=("MV Boli bold",25)).place(x=300,y=350)
txtusername=Entry(root,font=("Arial",30),textvariable=varusername)
txtusername.place(x=750,y=250)
txtpassword=Entry(root,font=("Arial",30),textvariable=varpassword)
txtpassword.place(x=750,y=350)
btncreate=Button(root,text="CREATE",font=("Consolas",20),bg="light yellow",command=create_clicked).place(x=100,y=500)
btnclear=Button(root,text="CLEAR",font=("Consolas",20),bg="light yellow",command=clear_clicked).place(x=500,y=500)
btnback=Button(root,text="BACK",font=("Consolas",20),bg="light yellow",command=clear_clicked).place(x=850,y=500)
btnexit=Button(root,text="EXIT",font=("Consolas",20),bg="light yellow",command=exit_clicked).place(x=1250,y=500)
txtusername.focus()
root.mainloop()

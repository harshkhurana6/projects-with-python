from tkinter import *
import tkinter as tk
import tkinter.ttk as TTK
from tkinter import messagebox
import os
import sqlite3
from tkinter import filedialog

root=Tk()
root.title("Stock Entry Screen")
root.attributes("-fullscreen",True)

photo1=PhotoImage(file="")
w=Label(root)
w.configure(image=photo1)
w.place(x=0,y=0)

varicode=StringVar()
variname=StringVar()
varrate=StringVar()
varqih=StringVar()
varopen=StringVar()
varimg=StringVar()

def getautoicode():
    sqlite_file='invent.sqlite'
    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    c.execute("select icode from tbstock")
    data=c.fetchall()
    if(len(data)==0):
        varicode.set("1001")
    else:
        lastrow=data[-1]
        ic=int(lastrow[0])
        ic=ic+1
        print(ic)
        varicode.set(str(ic))
    conn.close()

def clear_clicked():
    varicode.set("")
    variname.set("")
    varrate.set("")
    varqih.set("")
    varopen.set("")

def open_file():
    global photo
    name=filedialog.askopenfilename()
    photo=PhotoImage(file=name)
    btn.configure(image=photo)
    varopen.set(name)

photo=PhotoImage(file="",height=1,width=1)
btn=Button(root,image=photo,command=open_file)
btn.place(x=100,y=200)

def insertitem_clicked():
    sqlite_file='invent.sqlite'
    conn=sqslite3.connect(sqlite_file)
    c=conn.cursor()
    vic=varicode.get()
    vin=variname.get()
    vr=varrate.get()
    vqih=varqih.get()
    vopen=varimg.get()

    c.execute("insert into tbstock(icode,iname,rate,qih,picpath) values(?,?,?,?,?)",(vic,vin,vr,vqih,vopen))
    messagebox.showinfo("Great!!","Item Inserted...")
    conn.commit()
    conn.close()
    clear_clicked()
    getautoicode()
    txtiname.focus()

def cancel_clicked():
    root.destroy()

titlelbl=Label(root,text="ENTER ITEM",font=("Arial bold",30),bg='black',fg='white').place(x=600,y=100)

lblicode=Label(root,text="ITEM CODE",font=("Arial",20),bg='black',fg='white').place(x=520,y=250)
lbliname=Label(root,text="ITEM NAME",font=("Arial",20),bg='black',fg='white').place(x=520,y=350)
lblrate=Label(root,text="RATE",font=("Arial",20),bg='black',fg='white').place(x=520,y=450)
lblqoh=Label(root,text="QIH",font=("Arial",20),bg='black',fg='white').place(x=520,y=550)
lblopen=Label(root,text="FILE ADDRESS",font=("Arial",20),bg='black',fg='white').place(x=520,y=650)

txticode=Entry(root,font=("Arial",20),state='disabled',textvariable=varicode)
txticode.place(x=850,y=250)
txtiname=Entry(root,font=("Arial",20),textvariable=variname)
txtiname.place(x=850,y=350)
txtrate=Entry(root,font=("Arial",20),textvariable=varrate)
txtrate.place(x=850,y=450)
txtqih=Entry(root,font=("Arial",20),textvariable=varqih)
txtqih.place(x=850,y=550)
txtopen=Entry(root,font=("Arial",20),textvariable=varopen)
txtopen.place(x=850,y=650)

loginbtn=Button(root,text="INSERT",font=("Stencil",20),bg='black',fg='white',command=insertitem_clicked).place(x=600,y=700)
createbtn=Button(root,text="CLEAR",font=("Stencil",20),bg='black',fg='white',command=clear_clicked).place(x=800,y=700)
cancelbtn=Button(root,text="CANCEL",font=("Stencil",20),bg='black',fg='white',command=cancel_clicked).place(x=1000,y=700)
openbtn=Button(root,text="OPEN",font=("Stencil",20),bg='black',fg='white',command=open_file).place(x=1200,y=700)

getautoicode()
root.mainloop()

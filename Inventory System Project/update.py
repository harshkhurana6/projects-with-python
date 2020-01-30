from tkinter import *
from tkinter import messagebox
import os
import sqlite3
import tkinter.ttk as TTK

root=Tk()
root.title("Stock Updation")
root.attributes("-fullscreen",True)
root.configure(bg="teal")
varicode=StringVar()
variname=StringVar()
varrate=StringVar()
varqih=StringVar()
vardoi=StringVar()
varqtyissue=StringVar()

def clear_clicked():
    varicode.set("")
    variname.set("")
    varrate.set("")
    varqih.set("")
    vardoi.set("")
    varqtyissue.set("")

def updateitem_clicked():
    sqlite_file='invent.sqlite'
    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    vic=varicode.get()
    vin=variname.get()
    vr=varrate.get()
    vqih=varqih.get()
    vdoi=vardoi.get()
    vqtyissue=varqtyissue.get()
    c.execute("update tbstock st iname=(?), rate=(?),qih=(?) where icode=(?)",(vin,vr,vqih,vic))
    conn.commit()
    conn.close()
    messagebox.showinfo("Great!!","Item Updated")

def cancel_clicked():
    root.destroy()

def geticodelist():
    sqlite_file="invent.sqlite"
    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    c.execute("select icode from tbstock")
    icodelist=[row[0] for row in c.fetchall()]
    conn.close()
    return icodelist
def delete_clicked():
    sqlite_file='invent.sqlite'
    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    c.execute("delete from tbstock where icode=(?)",(vic,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Item Deleted")
    clear_clicked()
    txticode['values']=geticodelist()

def onitem_clicked(event):
    sqlite_file='invent.sqlite'
    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    vic=varicode.get()
    c.execute("select * from tbstock where icode=(?)"(vic))
    for row in c.fetchall():
        variname.set(row[1])
        varrate.set(row[2])
        varqih.set(row[3])
    conn.commit()
    conn.close()

titleLabel=Label(root,text="UPDATE STOCK",font=("Stencil",30)).place(x=600,y=100)
lblicode=Label(root,text="ITEM CODE",font=("Stencil",20)).place(x=520,y=250)
lbliname=Label(root,text="ITEM NAME",font=("Stencil",20)).place(x=520,y=350)
lblrate=Label(root,text="RATE",font=("Stencil",20)).place(x=520,y=450)
lblqoh=Label(root,text="QOH",font=("Stencil",20)).place(x=520,y=550)

txticode=TTK.Combobox(root,font=("Arial",20),textvariable=varicode)
txticode.place(x=850,y=250)
txticode.bind("<<ComboboxSelected>>",onitem_clicked)

##icodelist=geticodelist()
##txticode['values']=icodelist

txtiname=Entry(root,font=("Arial",20),textvariable=variname)
txtiname.place(x=850,y=350)
txtrate=Entry(root,font=("Arial",20),textvariable=varrate)
txtrate.place(x=850,y=450)
txtqih=Entry(root,font=("Arial",20),textvariable=varqih)
txtqih.place(x=850,y=550)

btnmodify=Button(root,text="MODIFY",font=("Stencil",20),command=updateitem_clicked).place(x=500,y=700)
btndelete=Button(root,text="DELETE",font=("Stencil",20),command=delete_clicked).place(x=700,y=700)
btncreate=Button(root,text="CLEAR",font=("Stencil",20),command=clear_clicked).place(x=900,y=700)
btncancel=Button(root,text="CANCEL",font=("Stencil",20),command=cancel_clicked).place(x=1100,y=700)

root.mainloop()

from tkinter import *
from tkinter import messagebox
import sqlite3
import tkinter.ttk as TTK
from tkinter import filedialog

root=Tk()
root.title("Issue Screen")
root.attributes("-fullscreen",True)

photo=PhotoImage(file="bar1.png")
w=Label(root)
w.configure(image=photo)
w.place(x=0,y=0)

varicode=StringVar()
variname=StringVar()
varrate=StringVar()
varqih=StringVar()
vardoi=StringVar()
varqtyissue=StringVar()
varimg=StringVar()

def clear_clicked():
    varicode.set("")
    variname.set("")
    varrate.set("")
    varqih.set("")
    vardoi.set("")
    varqtyissue.set("")
    varimg.set("")

def issue_clicked():
    sqlite_file="invent.sqlite"
    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    vic=varicode.get()
    vin=variname.get()
    vr=varrate.get()
    vqih=varqih.get()
    vdoi=vardoi.get()
    vqtyissue=varqtyissue.get()
    c.execute('update tbstock set qih=qih(?) where icode(?)',(vqtyissue,vic))
    conn.commit()
    messagebox.showinfo("Great!!","Stock Updated")

    c.execute("insert into tbissue (icode,doi,qtyissue) values(?,?,?)",(vic,vdoi,vqtyissue))
    messagebox.showinfo("Great!!","Item Inserted")
    conn.commit()
    conn.close()
    clear_clicked()
    txticode['value']=geticodelist()

def cancel_clicked():
    root.destroy()

def geticodelist():
    sqlite_file="invent.sqlit"
    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    #c.execute("select icode from tbstock")
    icodelist=[row[0] for row in c.fetchall()]
    conn.close()
    return icodelist

    if icodelist.get():
        txticode.PhotoImage(height=20,width=20)

def onitem_clicked(event):
    global photo1
    sqlite_file='invent.sqlite'
    conn=sqlite3.connect(sqlite_file)
    c=conn.cursor()
    vic=varicode.get()
    vimg=varimg.get()
    c.execute("select * from tbstock where icode=(?)",(vic,))
    for row in c.fetchall():
        variname.set(row[1])
        varrate.set(row[2])
        varqih.set(row[3])
        varimg.set(row[4])
        name=row[4]
        photo1=PhotoImage(file=name)
        btn.configure(image=photo1)
    conn.commit()
    conn.close()

photo1=PhotoImage(file="bartender.png")
btn=Button(root, image=photo1,command=onitem_clicked,height=320,width=300)
btn.place(x=100,y=250)
ttlbl=Label(root,text="ORDER ITEM",font=("Stencil",30)).place(x=600,y=50)
lblicode=Label(root,text="ITEM CODE",font=("Stencil",20)).place(x=520,y=150)
lbliname=Label(root,text="ITEM NAME",font=("Stencil",20)).place(x=520,y=250)
lblrate=Label(root,text="RATE",font=("Stencil",20)).place(x=520,y=350)
lblqoh=Label(root,text="QOH",font=("Stencil",20)).place(x=520,y=450)
lblrate=Label(root,text="DOI",font=("Stencil",20)).place(x=520,y=550)
lblqoh=Label(root,text="QTY TO ORDER",font=("Stencil",20)).place(x=520,y=650)
txticode=TTK.Combobox(root,font=("Arial",20),textvariable=varicode)
txticode.place(x=850,y=150)
txticode.bind("<<ComboboxSelected>>", onitem_clicked)
icodelist=geticodelist()
txticode['values']=icodelist
txtiname=Entry(root,font=("Arial",20),textvariable=variname,state="disable")
txtiname.place(x=850,y=250)
txtrate=Entry(root,font=("Arial",20),textvariable=varrate,state="disable")
txtrate.place(x=850,y=350)
txtqoh=Entry(root,font=("Arial",20),textvariable=varqih,state="disable")
txtqoh.place(x=850,y=450)
txtdoi=Entry(root,font=("Arial",20),textvariable=vardoi)
txtdoi.place(x=850,y=550)
txtqtyissued=Entry(root,font=("Arial",20),textvariable=varqtyissue)
txtqtyissued.place(x=850,y=650)
btnissue=Button(root,text="ORDER",font=("Stencil",20),command=issue_clicked).place(x=500,y=800)
btnclear=Button(root,text="CLEAR",font=("Stencil",20),command=clear_clicked).place(x=700,y=800)
btncancel=Button(root,text="CANCEL",font=("Stencil",20),command=cancel_clicked).place(x=900,y=800)
root.mainloop()

from tkinter import *
from tkinter import filedialog
import os

root=Tk()
root.title("Menu")
root.attributes("-fullscreen",True)
photo=PhotoImage(file="menu.png")
w=Label(root)
w.configure(image=photo)
w.place(x=0,y=0)

def putitem():
    root.destroy()
    os.system('putdata.py')

def updateitem():
    root.destroy()
    os.system('update.py')

def issueitem():
    root.destroy()
    os.system('issue_screen.py')

def reportitem():
    root.destroy()
    os.system('report.py')

mymenu=Menu(root)
root.config(menu=mymenu)
filemenu=Menu(mymenu)
tranmenu=Menu(mymenu)
reportmenu=Menu(mymenu)
lastmenu=Menu(mymenu)

mymenu.add_cascade(label="Stock",menu=filemenu)
filemenu.add_command(label="Add Item",command=putitem)
filemenu.add_separator()
filemenu.add_command(label="Modify Item",command=updateitem)

tranmenu=Menu(mymenu)
mymenu.add_cascade(label="Transaction",menu=tranmenu)
tranmenu.add_command(label="Order",command=putitem)
tranmenu.add_command(label="Item Receipt")

reportmenu=Menu(mymenu)
mymenu.add_cascade(label='Report',menu=reportmenu)
reportmenu.add_command(label="All item details",command=reportitem)
reportmenu.add_separator()
reportmenu.add_command(label="Ordered items details")
reportmenu.add_separator()
reportmenu.add_command(label="Bill")

lastmenu=Menu(mymenu)
mymenu.add_cascade(label="Exit",menu=lastmenu)
lastmenu.add_command(label="Quit App",command=root.destroy)

root.mainloop()

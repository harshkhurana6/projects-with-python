from tkinter import *
import time

root=Tk()
root.title("Splash screen")
root.attributes("-fullscreen",True)

photo=PhotoImage(file="bar.png")
w=Label(root)
w.configure(image=photo)
w.place(x=0,y=0)

def login_clicked():
    import os
    root.destroy()
    os.system("login.py")
t1=Label(root,text="Bar Order",font=("Monotype Corsiva", 50,"bold"),fg="black")
t1.place(x=550,y=150)

t2=Label(root,text="SYSTEM",font=("Monotype Corsiva",50,"bold"),fg="black")
t2.place(x=580,y=250)

t3=Label(root,text="Submitted By: ",font=("Monotype Corsiva",20,"bold"),fg="black")
t3.place(x=620,y=350)


t4=Label(root,text="Harsh Khurana",font=("Monotype Corsiva",20,"bold"),fg="black")
t4.place(x=620,y=400)

b1=Button(root,text="GO TO LOGIN SCREEN",font=(3),command=login_clicked)
b1.place(x=630,y=500)
root.mainloop()

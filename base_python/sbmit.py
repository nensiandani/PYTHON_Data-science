from tkinter import *
import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="demo")





def Registration():
    pass

top=Tk()

top.title("form")
#creating label
name=Label(top,text="name").place(x=30,y=50)
password=Label(top,text="password").place(x=30,y=65)

e1=Entry(top,width=20).place(x=100,y=50)
e2=Entry(top,width=20).place(x=100,y=70)

submit=Button(top,text="submit",command=Registration).place(x=50,y=120)
top.mainloop()

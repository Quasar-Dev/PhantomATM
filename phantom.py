from tkinter import *
import telnetlib
import getpass
import sys
import os

root = Tk()

# StringVar
US1 = StringVar()
PA1 = StringVar()

Username = US1.get()
Password = PA1.get()

IP = '151.80.186.121'
PORT = '666'

def loginInput():
    tn = telnetlib.Telnet(IP, PORT)

    tn.write((Username + r'\n').encode())
    tn.write((Password + r'\n').encode())

    print(tn.interact())

root.title("PHANTOM ATM")
root.minsize(width=420, height=100)
root.resizable(width=False, height=False)

label_0 = Label(root, text="Login",width=20,font=("bold", 15))
label_0.place(x=50,y=13)

label_1 = Label(root, text="Username", width=20)
label_1.place(x=35, y=63)

label_2 = Label(root, text="Password", width=20)
label_2.place(x=35, y=93)

entry_0 = Entry(root, textvar=Username, width=10)
entry_0.place(x=200, y=63)

entry_1 = Entry(root, textvar=Password, width=10, show="*")
entry_1.place(x=200, y=93)

button_1 = Button(root, text='Sign In', width=10, command=loginInput)
button_1.place(x=145, y=130)

root.mainloop()

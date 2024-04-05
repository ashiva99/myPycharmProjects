import random
from tkinter import *
import string

def generate_password():
    password=[]
    for i in range(6):
        digit=random.choice(string.digits)
        password.append(digit)
    y="".join(str(x)for x in password)
    lbl.config(text=y)

root=Tk()
root.geometry("250x200")
btn=Button(root,text="Generate Password",command=generate_password)
btn.grid(row=2,column=2)
lbl=Label(root,font=("times",15,"bold"))
lbl.grid(row=4,column=2)
root.mainloop()
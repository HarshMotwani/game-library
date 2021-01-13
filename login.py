import tkinter as tk
import os
import csv
from tkinter import messagebox

window = tk.Tk()

window.title('Login') 
window.geometry('300x200+100+100')

def option():
    with open("login_credentials.csv", "r") as csv_file:
        data = csv.reader(csv_file, delimiter=",")
        for i in data:
            if i[1] == e1.get() and i[2] == e2.get():
                window.destroy()
                os.system('option.py')
    e1.delete(0, "end")
    e2.delete(0, "end")
    messagebox.showwarning("Wrong Credentials!!!", "Your User Name or Password is incorrect. Please Try Again!!!") 
    
def signup():
    window.destroy()
    os.system('signup.py')

l1 = tk.Label(window, text="User Name :-")
l1.place(x=20, y=60)

l2 = tk.Label(window, text="Password :-")
l2.place(x=20, y=90)

l3 = tk.Label(window, text="LogIN")
l3.place(x=120, y=10)

e1 = tk.Entry(window)
e1.place(x=120, y=60)

e2 = tk.Entry(window, show="*")
e2.place(x=120, y=90)

b1 = tk.Button(window, text ="LogIn", command=option)
b1.place(x=70, y=130)

b2 = tk.Button(window, text ="SignUp", command=signup)
b2.place(x=170, y=130)

window.mainloop()
import tkinter as tk
import os
import csv


window = tk.Tk()

window.title('Login') 
window.geometry('300x200+100+100')

def option():
    with open("login_credentials.csv", "a", newline="") as csv_file:
        data = csv.writer(csv_file)
        data.writerow([e1.get(), e2.get(), e3.get()])
    window.destroy()
    os.system('option.py')

def back():
    window.destroy()
    os.system('login.py')


l1 = tk.Label(window, text="Name :-")
l1.place(x=20, y=50)

l2 = tk.Label(window, text="User Name :-")
l2.place(x=20, y=80)

l3 = tk.Label(window, text="Password :-")
l3.place(x=20, y=110)

l4 = tk.Label(window, text="SignUP")
l4.place(x=120, y=10)

e1 = tk.Entry(window)
e1.place(x=120, y=50)

e2 = tk.Entry(window)
e2.place(x=120, y=80)

e3 = tk.Entry(window, show="*")
e3.place(x=120, y=110)

b1 = tk.Button(window, text ="SignUp", command=option)
b1.place(x=70, y=150)

b2 = tk.Button(window, text ="Back", command=back)
b2.place(x=170, y=150)

window.mainloop()
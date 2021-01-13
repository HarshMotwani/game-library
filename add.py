import tkinter as tk
import os

window = tk.Tk()

window.title('Login') 
window.geometry('300x200+100+100')

def back():
    window.destroy()
    os.system('option.py')

l1 = tk.Label(window, text="Enter your game forlder Location :-")
l1.place(x=0, y=65)

l2 = tk.Label(window, text="Add Game")
l2.place(x=110, y=10)

e1 = tk.Entry(window)
e1.place(x=190, y=65)

b1 = tk.Button(window, text ="Add Game")
b1.place(x=70, y=130)

b2 = tk.Button(window, text ="Back", command=back)
b2.place(x=170, y=130)

window.mainloop()
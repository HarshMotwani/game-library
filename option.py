import tkinter as tk
import os

window = tk.Tk()

window.title('Option')
window.geometry('300x200+100+100')

def library():
    window.destroy()
    os.system('library.py')

def addgame():
    window.destroy()
    os.system("add.py")

def logout():
    window.destroy()
    os.system('login.py')

b1 = tk.Button(window, text ="Library", command=library)
b1.place(x=50, y=85)

b2 = tk.Button(window, text ="Add Game", command=addgame)
b2.place(x=180, y=85)

b3 = tk.Button(window, text ="LogOut", command=logout)
b3.place(x=246, y=3)

l1 = tk.Label(window, text="Main Menu")
l1.place(x=110, y=10)

window.mainloop()
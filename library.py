import tkinter as tk
import os
from PIL import Image, ImageTk

window = tk.Tk()

window.title('Library') 
window.geometry('300x200+100+100')

def back():
    window.destroy()
    os.system('option.py')

def play():
    window.destroy()
    os.system('g1.py')



lf1 = tk.LabelFrame(window, text="Dodge Ball", width=270, height=150)
lf1.place(x=10, y=10)

PIL_image = Image.open("sample.png")
PIL_image.thumbnail((100, 100))
img = ImageTk.PhotoImage(PIL_image)

lf_l1 = tk.Label(lf1, image=img)
lf_l1.grid(row=1, column=1, columnspan=2)

m1 = tk.Message(lf1, text="Dodge incoming projectiles to increase score without getting hit 5 times.")
m1.grid(row=1, column=3, columnspan=2)

b1 = tk.Button(lf1, text="Play", command=play)
b1.grid(row=3, column=1, columnspan=2)

b2 = tk.Button(lf1, text="Review")
b2.grid(row=3, column=3, columnspan=2)

b3 = tk.Button(window, text ="Back", command=back)
b3.place(x=250, y=150)
window.mainloop()
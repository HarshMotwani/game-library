import tkinter as tk
import os
from PIL import Image, ImageTk

window = tk.Tk() 
window.title('ICON') 
window.geometry('200x200+100+100')

PIL_image = Image.open("icon.png")
PIL_image.thumbnail((180, 180))
img = ImageTk.PhotoImage(PIL_image)

lf = tk.Label(window, image=img)
lf.place(x=10, y=10)

window.after(3000, lambda: window.destroy())

window.mainloop()

os.system('login.py')
# import csv
# from tkinter import messagebox

# with open("login_credentials.csv") as csv_file:
#     data = csv.reader(csv_file, delimiter=",")
#     # print(len(list(data)))
#     for i in data:
#         print(type(i[1]))

# import tkinter as tk
# from tkinter import messagebox 
  
# root = tk.Tk() 
# root.geometry("300x200") 
  
# w = tk.Label(root, text ='GeeksForGeeks', font = "50")  
# w.pack() 
  
# tk.messagebox.showinfo("showinfo", "Information") 
# root.mainloop()



import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('300x200+100+100')

make_frame = tk.LabelFrame(root, text="Sample Image", width=500, height=500, bg="white")
make_frame.pack()

stim_filename = "sample.png"

# # create the PIL image object:
PIL_image = Image.open(stim_filename)

width = 100
height = 100

# You may prefer to use Image.thumbnail instead
# Set use_resize to False to use Image.thumbnail
use_resize = False

if use_resize:
    # Image.resize returns a new PIL.Image of the specified size
    PIL_image_small = PIL_image.resize((width,height))
else:
    # Image.thumbnail converts the image to a thumbnail, in place
    PIL_image_small = PIL_image
    PIL_image_small.thumbnail((width,height))

# now create the ImageTk PhotoImage:
img = ImageTk.PhotoImage(PIL_image_small)
in_frame = tk.Label(make_frame, image = img)
in_frame.pack()

root.mainloop()
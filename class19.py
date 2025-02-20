from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image Viewer")
root.geometry("400x400")

uploade = Image.open("th.jpeg")

image = ImageTk.PhotoImage(uploade)

label = Label(root, image=image, height=350, width=300)
label.place(x=50, y=0)
label12 = Label(root, text='this is how u add image to tkinter ')
label12.place(x=50, y=350)

root.mainloop()
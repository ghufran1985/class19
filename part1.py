from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('200x200')

def msg():
    messaf  = messagebox.askquestion('window name', 'stop virus found ')

button = Button(root, text='scan for virus', command=msg)
button.place(x=50, y=80)

root.mainloop()
from tkinter import *

root = Tk()
root.geometry('400x300')
root.title('main')

def topwin():
    top = Toplevel()
    top.geometry('180x100')
    top.title('top window')
    l2 = Label(top, text='this is top window')
    l2.pack()

    top.mainloop()

l = Label(root, text='this is main window')
btn = Button(root, text='open another wondow', command=topwin)

l.pack()
btn.pack()

root.mainloop()
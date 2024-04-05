from tkinter import *


def run():
    root = Toplevel()

    frame = Frame(root, bg='blue', bd=5)
    frame.pack()

    label = Label(frame, text='This is a label', fg='white', bg='blue')
    label.pack()

    root.mainloop()
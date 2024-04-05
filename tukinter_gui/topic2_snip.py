from tkinter import *

def run():
    new_window = Toplevel()

    label1 = Label(new_window, text='Label 1')
    label1.grid(row=0, column=0)

    label2 = Label(new_window, text='Label 2')
    label2.grid(row=0, column=1)

    entry1 = Entry(new_window)
    entry1.grid(row=1, columnspan=2)

    new_window.mainloop()
from tkinter import *

def run():
    new_window = Toplevel()

    label1 = Label(new_window, text='Label 1')
    label1.pack()

    button1 = Button(new_window, text='Button 1')
    button1.pack()

    new_window.mainloop()
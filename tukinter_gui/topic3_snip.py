from tkinter import *

def run():
    new_window = Toplevel()

    label1 = Label(new_window, text='Label 1')
    label1.place(x=50, y=50)

    button1 = Button(new_window, text='Button 1')
    button1.place(x=100, y=100)

    new_window.mainloop()
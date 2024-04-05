from tkinter import *

def button_click():
    print('Button clicked!')

def run():
    new_window = Toplevel()

    button = Button(new_window, text='Click me!', command=button_click)
    button.pack()

    new_window.mainloop()
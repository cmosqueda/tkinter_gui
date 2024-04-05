# import the tkinter module
from tkinter import *

def run():

    # create root window
    new_window = Toplevel()

    # create a label widget with "Hello, World" text
    helloWorldLbl = Label(new_window, text='Hello, World!')

    # Use a 'pack' geometry manager to display your label widget
    helloWorldLbl.pack()

    # start tkinter event loop
    new_window.mainloop()
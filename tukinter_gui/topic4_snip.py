from tkinter import *

def run():
    new_window = Toplevel()

    #create a label widget with text
    label = Label(new_window, text='Hello, World!')

    #customize label widget properties
    label.config(font=('Arial', '16'), fg='blue', bg='white')

    #pack the label
    label.pack()

    new_window.mainloop()
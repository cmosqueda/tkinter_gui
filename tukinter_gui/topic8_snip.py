from tkinter import *

def run():
    root = Toplevel()

    canvas = Canvas(root, width=400, height=300)
    canvas.pack()

    canvas.create_rectangle(50, 50, 200, 150, fill='blue')

    root.mainloop()
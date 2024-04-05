from tkinter import *
from tkinter import ttk

def run():
    root = Toplevel()

    notebook = ttk.Notebook(root)

    #create pages
    page1 = Frame(notebook)
    page2 = Frame(notebook)

    #add pages to the notebook
    notebook.add(page1, text='Page 1')
    notebook.add(page2, text='Page 2')

    #add content to pages
    label1 = Label(page1, text='This is page 1')
    label1.pack(pady=10)
    label2 = Label(page2, text='This is page 2')
    label2.pack(pady=10)

    #display notebook
    notebook.pack()

    root.mainloop()
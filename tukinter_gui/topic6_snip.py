from tkinter import *

def on_button_click():
    #get the text entered in the entry widget
    entry_text = entry.get()
    print('Entered text:', entry_text)

def run():
    root = Toplevel()
    
    #create entry widget
    entry = Entry(root)
    entry.pack()

    button = Button(root, text='Submit', command=on_button_click)
    button.pack()

    root.mainloop()
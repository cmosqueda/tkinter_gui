# # import the tkinter module
# from tkinter import *

# # create root window
# root = Tk()

# # create a label widget with "Hello, World" text
# helloWorldLbl = Label(root, text='Hello, World!')

# # Use a 'pack' geometry manager to display your label widget
# helloWorldLbl.pack()

# # start tkinter event loop
# root.mainloop()

# import tkinter as tk
# from tkinter import ttk

# window = tk.Tk()
# window.title("Text Widget in Notebook")

# notebook = ttk.Notebook(window)

# tab = ttk.Frame(notebook)
# notebook.add(tab, text="Tab 1")

# text_widget = tk.Text(tab)
# text_widget.pack(fill="both", expand=True)

# notebook.pack()
# window.mainloop()


# import tkinter as tk
# from tkinter import ttk

# window = tk.Tk()
# window.title("Insert Data from File")

# notebook = ttk.Notebook(window)

# tab = ttk.Frame(notebook)
# notebook.add(tab, text="Tab 1")

# text_widget = tk.Text(tab)
# text_widget.pack(fill="both", expand=True)

# file_path = "topic0_snippet.txt"  # Update with your file path
# with open(file_path, "r") as file:
#     file_contents = file.read()

# text_widget.insert("1.0", file_contents)

# notebook.pack()
# window.mainloop()


# import tkinter as tk
# from tkinter import ttk

# window = tk.Tk()
# window.title("Expand Text Widget with Grid Layout")

# notebook = ttk.Notebook(window)

# tab = ttk.Frame(notebook)
# notebook.add(tab, text="Tab 1")

# text_widget = tk.Text(tab)
# text_widget.grid(row=0, column=0, sticky="nsew")

# tab.grid_rowconfigure(0, weight=1)
# tab.grid_columnconfigure(0, weight=1)

# notebook.pack(fill="both", expand=True)
# window.mainloop()


import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Main Window")

def open_new_window():
    new_window = tk.Toplevel(window)
    new_window.title("New Window")
    # Customize the new window as desired
    # ...

    # Add widgets and functionality to the new window
    # ...

    new_window.mainloop()

open_button = tk.Button(window, text="Open New Window", command=open_new_window)
open_button.pack()

window.mainloop()

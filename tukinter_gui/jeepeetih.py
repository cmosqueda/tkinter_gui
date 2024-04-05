# import tkinter as tk

# def show_frame():
#     selected_index = listbox.curselection()
#     if selected_index:
#         index = selected_index[0]
#         frame = frames[index]
#         frame.tkraise()

# root = tk.Tk()

# listbox = tk.Listbox(root)
# listbox.pack()

# # Create different frames
# frame1 = tk.Frame(root, bg="red")
# frame2 = tk.Frame(root, bg="blue")
# frame3 = tk.Frame(root, bg="green")

# frames = [frame1, frame2, frame3]

# # Add items to the listbox
# listbox.insert(tk.END, "Frame 1")
# listbox.insert(tk.END, "Frame 2")
# listbox.insert(tk.END, "Frame 3")

# # Bind the show_frame function to the ListboxSelect event
# listbox.bind("<<ListboxSelect>>", lambda event: show_frame())

# # Show the initial frame
# frame1.pack()

# root.mainloop()


# from tkinter import *

# ws = Tk() 
# ws.title('Python Guides') 
# ws.geometry('400x300')

# var = StringVar()

# def showSelected():
#     countries = []
#     cname = lb.curselection()
#     for i in cname:
#         op = lb.get(i)
#         countries.append(op)
#     for val in countries:
#         print(val)

# show = Label(ws, text = "Select Your Country", font = ("Times", 14), padx = 10, pady = 10)
# show.pack() 
# lb = Listbox(ws, selectmode = "multiple")
# lb.pack(padx = 10, pady = 10, expand = YES, fill = "both") 

# x =["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Australia", "Brazil", "Canada", "China", "Iceland", "Israel", "United States", "Zimbabwe"]

# for item in range(len(x)): 
# 	lb.insert(END, x[item]) 
# 	lb.itemconfig(item, bg="#bdc1d6") 

# Button(ws, text="Show Selected", command=showSelected).pack()
# ws.mainloop() 


import tkinter as tk

root = tk.Tk()

# Create a scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a canvas widget
canvas = tk.Canvas(root, yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Configure the scrollbar to control the canvas
scrollbar.config(command=canvas.yview)

# Add content to the canvas
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

# Add some widgets to the frame
for i in range(30):
    label = tk.Label(frame, text="Item {}".format(i))
    label.pack(pady=10)

# Update the scroll region
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()


import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Create a notebook widget
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, sticky="nsew")

# Create a frame for the notebook's content
content_frame = ttk.Frame(notebook)
content_frame.grid(row=0, column=0, sticky="nsew")

# Create a canvas widget within the frame
canvas = tk.Canvas(content_frame)
canvas.grid(row=0, column=0, sticky="nsew")

# Create a scrollbar for the canvas
scrollbar = tk.Scrollbar(content_frame, command=canvas.yview)
scrollbar.grid(row=0, column=0, sticky="nsew")

# Configure the canvas to use the scrollbar
canvas.config(yscrollcommand=scrollbar.set)

# Create a new frame as the container for the notebook pages
container = ttk.Frame(canvas)
canvas.create_window((0, 0), window=container, anchor=tk.NW)

# Add some notebook pages (frames) to the container
page1 = ttk.Frame(container)
page2 = ttk.Frame(container)
page3 = ttk.Frame(container)

notebook.add(page1, text="Page 1")
notebook.add(page2, text="Page 2")
notebook.add(page3, text="Page 3")

# Update the scroll region
container.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()


# import tkinter as tk

# def change_button_color(event):
#     # Change the button color
#     button.config(bg="red", fg="white")

# root = tk.Tk()

# # Create a button
# button = tk.Button(root, text="Click Me!")

# # Bind the function to the button's click event
# button.bind("<Button-1>", change_button_color)

# button.pack()

# root.mainloop()

# import tkinter as tk

# def on_enter(event):

#     btn = event.widget
#     # Change the button color when the mouse enters
#     if btn == button1:
#         button1.config(bg="red", fg="white")
#     elif btn == button2:
#         button2.config(bg='blue', fg='white')
#     else:
#         print('null')

# def on_leave(event):

#     btn = event.widget
#     # Change the button color when the mouse leaves
#     if btn == button1:
#         button1.config(bg="SystemButtonFace", fg="black")
#     elif btn == button2:
#         button2.config(bg="SystemButtonFace", fg="black")
#     else:
#         print('null')


# root = tk.Tk()

# # Create a button
# button1 = tk.Button(root, text="Hover Me!")

# # Bind the functions to the button's events
# button1.bind("<Enter>", on_enter)
# button1.bind("<Leave>", on_leave)

# button1.pack()

# button2 = tk.Button(root, text='Hover Me!')

# button2.bind("<Enter>", on_enter)
# button2.bind("<Leave>", on_leave)

# button2.pack()


# root.mainloop()

# # code nila bogart
#         # ==========SHOW-ORDERS-WINDOW-SCROLLBAR========== #
#         cont_frame = Frame(show_win)
#         cont_frame.pack(fill=BOTH, expand=1)
#         cont_canvas = Canvas(cont_frame)
#         cont_canvas.pack(side=LEFT, fill=BOTH, expand=1)
#         cont_scrollbar = ttk.Scrollbar(cont_frame, orient=VERTICAL, command=cont_canvas.yview)
#         cont_scrollbar.pack(side=RIGHT, fill=Y)
#         cont_canvas.configure(yscrollcommand=cont_scrollbar.set)
#         cont_canvas.bind('<Configure>', lambda e: cont_canvas.configure(scrollregion=cont_canvas.bbox('all')))
#         secondcont_frame = Frame(cont_canvas)
#         cont_canvas.create_window((0, 0), window=secondcont_frame, anchor='nw')

import tkinter as tk

window = tk.Tk()
window.title("Scrollbar with Frame")

frame = tk.Frame(window)
frame.pack(fill=tk.BOTH, expand=True)

# Add widgets to the frame

scrollbar = tk.Scrollbar(window, command=frame.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

frame.configure(yscrollcommand=scrollbar.set)

window.mainloop()

from tkinter import *
from functools import partial


# expression = StringVar()


def clicked(num):
    expression.set(expression.get()+num)

def evaluate():
    result = eval(expression.get())

    expression.set(result)

def clear():
    expression.set('')

# main = Tk()
# main.title('My Calculator')

# expression = StringVar()

# def run():





# global expression
def run():
    main = Tk()
    main.title('My Calculator')

    expression = StringVar()

    calcuLbl = Label(main, text='My Calculator')
    calcuLbl.grid(row=0, column=1, columnspan = 2)

    calcuEntry = Entry(main, width=30, text = expression, borderwidth=3)
    calcuEntry.grid(row=1, column=0, columnspan = 4)

    oneBtn = Button(main, text='1', font=('Helvetica',11), width=5, height=3, command = partial(clicked, '1'))
    twoBtn = Button(main, text='2', font=('Helvetica',11), width=5, height=3, command = partial(clicked, '2'))
    threeBtn = Button(main, text='3', font=('Helvetica',11), width=5, height=3, command = partial(clicked, '3'))
    plusBtn = Button(main, text='+', font=('Helvetica',11), width=5, height=3, fg='#0073ed', command = partial(clicked, '+'))

    oneBtn.grid(row=2, column=0)
    twoBtn.grid(row=2, column=1)
    threeBtn.grid(row=2, column=2)
    plusBtn.grid(row=2, column=3)


    fourBtn = Button(main, text='4', font=('Helvetica',11), width=5, height=3, command = partial(clicked, '4'))
    fiveBtn = Button(main, text='5', font=('Helvetica',11), width=5, height=3, command = partial(clicked, '5'))
    sixBtn = Button(main, text='6', font=('Helvetica',11), width=5, height=3, command = partial(clicked, '6'))
    minusBtn = Button(main, text='-', font=('Helvetica',11), width=5, height=3, fg='#0073ed', command = partial(clicked, '-'))

    fourBtn.grid(row=3, column=0)
    fiveBtn.grid(row=3, column=1)
    sixBtn.grid(row=3, column=2)
    minusBtn.grid(row=3, column=3)


    sevenBtn = Button(main, text='7', font=('Helvetica',11), width=5, height=3, command = partial(clicked, '7'))
    eightBtn = Button(main, text='8', font=('Helvetica',11), width=5, height=3, command = partial(clicked, '8'))
    nineBtn = Button(main, text='9', font=('Helvetica',11), width=5, height=3, command = partial(clicked, '9'))
    multiBtn = Button(main, text='', font=('Helvetica',11), width=5, height=3, fg='#0073ed', command = partial(clicked, ''))

    sevenBtn.grid(row=4, column=0)
    eightBtn.grid(row=4, column=1)
    nineBtn.grid(row=4, column=2)
    multiBtn.grid(row=4, column=3)


    zeroBtn = Button(main, text='0', font=('Helvetica',11), width=5, height=3, command = partial(clicked, '0'))
    equalBtn = Button(main, text='=', font=('Helvetica',11), bg='#6ab8f7', fg='white', width=5, height=3, command = evaluate)
    clearBtn = Button(main, text='C', font=('Helvetica',11), bg='#f75757', fg='white', width=5, height=3, command = clear)
    divBtn = Button(main, text='/', font=('Helvetica',11), width=5, height=3, fg='#0073ed', command = partial(clicked, '/'))

    zeroBtn.grid(row=5, column=0)
    equalBtn.grid(row=5, column=1)
    clearBtn.grid(row=5, column=2)
    divBtn.grid(row=5, column=3)


    main.mainloop()



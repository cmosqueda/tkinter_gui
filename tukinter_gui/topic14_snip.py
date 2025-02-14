from tkinter import *



#functions
def add():
    #temp = [idStr.get(), nameStr.get(), posStr.get()]
    #employeeList.append(temp)

    emp_details = idStr.get()+","+nameStr.get()+","+posStr.get()+"\n"

    file = open("employee.txt", "a+")

    file.write(emp_details)

    file.close()

    #set entry boxes after submit
    idStr.set('')
    nameStr.set('')
    posStr.set('')

def showAdd():
    mainFrame.grid(row=0, column=0, rowspan=6)

def showEmp():
    with open("employee.txt") as f:
        emp = f.readlines()

    showFrame.grid(row=6, column=0)

    count = 1
    for i in emp:
        e = i.split(",")
        print(e)
        
        
        idDispLbl = Label(showFrame, text=e[0]).grid(row=count, column=0)
        nameDispLbl = Label(showFrame, text=e[1]).grid(row=count, column=1, columnspan=2)
        posDispLbl = Label(showFrame, text=e[2].strip()).grid(row=count, column=3, columnspan=2)

        count+=1

def run():
    main = Tk()

    #employeeList = []

    #StringVar to get text input
    idStr = StringVar()
    nameStr = StringVar()
    posStr = StringVar()

    mainFrame = Frame(main)
    #mainFrame.grid(row=0, column=0, rowspan=6) >>>> gibalhin sa showAdd function

    showFrame = Frame(main)

    titleLbl = Label(mainFrame, text="Welcome to XYZ Company, Enter Employee Details")
    titleLbl.grid(row=0, column=0, columnspan=5)

    idLbl = Label(mainFrame, text="Employee ID: ").grid(row=1, column=0, columnspan=2, sticky="w")
    nameLbl = Label(mainFrame, text="Employee Name: ").grid(row=2, column=0, columnspan=2, sticky="w")
    posLbl = Label(mainFrame, text="Employee Position: ").grid(row=3, column=0, columnspan=2, sticky="w")

    idEntry = Entry(mainFrame, text=idStr).grid(row=1, column=2, columnspan=3)
    nameEntry = Entry(mainFrame, text=nameStr).grid(row=2, column=2, columnspan=3)
    posEntry = Entry(mainFrame, text=posStr).grid(row=3, column=2, columnspan=3)

    submitBtn = Button(mainFrame, text="Submit", command=add).grid(row=4, column=2)
    #showBtn = Button(mainFrame, text="Show", command=showEmp).grid(row=5, column=2) >>> gibalhin ang function sa line 68


    #show frame
    idShowLbl = Label(showFrame, text="ID").grid(row=0, column=0)
    nameShowLbl = Label(showFrame, text="Name").grid(row=0, column=1, columnspan=2)
    posShowLbl = Label(showFrame, text="Position").grid(row=0, column=3, columnspan=2)


    #menubar
    menuBar = Menu(main)

    actionMenu = Menu(menuBar, tearoff=0)
    actionMenu.add_command(label="Add Employee", command=showAdd)
    actionMenu.add_command(label="Show Employees", command=showEmp)

    menuBar.add_cascade(label="Action", menu=actionMenu)

    main.config(menu=menuBar)

    main.mainloop()
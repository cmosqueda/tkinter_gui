from tkinter import *
from tkinter import ttk
# from PIL import Image, ImageTk

#import separate py files to run for code snippets
import topic0_snip
import topic1_snip
import topic2_snip
import topic3_snip
import topic4_snip
import topic5_snip
import topic6_snip
import topic7_snip
import topic8_snip
import topic9_snip
import topic10_snip
import topic11_snip
import topic12_snip

import topic14_snip
import topic15_snip


class Application:
    def __init__(self, main):
        # Tk.__init__(self, main)
        self.main = main
        self.main.geometry('520x340')
        # self.main.resizable(False, False)
        self.main.title('TUkinter')
        self.main.iconbitmap("tu_icon_blue.ico")
        

        self.initialize_ui()    #diri mahitabo tanan

        self.allTopics()    #tawgon niya tanan frames sa topics


    def initialize_ui(self):

        ############### MENU BAR ###############
        self.menuBar = Menu(self.main)

        #commands in Topics cascade
        self.actionMenu = Menu(self.menuBar, tearoff=0)
        self.actionMenu.add_command(label='Go to topics', command=lambda: self.showFrame(self.topicsFrame))
        # self.actionMenu.add_command(label='Youtube tutorials', command=0)
        # self.actionMenu.add_command(label='Website resources', command=0)
        # self.actionMenu.add_command(label='IDE recommendations', command=0)
        self.actionMenu.add_separator()
        self.actionMenu.add_command(label='Go back', command=lambda: self.showFrame(self.welcomeFrame))

        #add Actions cascade in menuBar
        self.menuBar.add_cascade(label='Actions', menu=self.actionMenu)


        #configure menuBar
        self.main.config(menu=self.menuBar)


        ############### WELCOME FRAME ###############
        self.welcomeFrame = Frame(self.main)
        self.welcomeFrame.grid(row=0, column=0, columnspan=7, rowspan=10)
        #welcomeFrame will show up as default

        #insert logo here

        # self.tukinterLogo = Image.open('tukinter_text_logo.png')
        # self.resizedLogo = self.tukinterLogo.resize((200, 120))

        # self.tukinter_logo_img = ImageTk.PhotoImage(self.resizedLogo)

        # self.tukinterWelcomeLogo = Label(self.welcomeFrame, image=self.tukinter_logo_img)

        # self.tukinterWelcomeLogo.grid(row=0, column=1, columnspan=6, pady=15, sticky='nsew')


        self.welcomeTitle = Label(self.welcomeFrame,
                                    text='Welcome to TUkinter!',
                                    font=('Helvetica, 15'),
                                    fg='blue')
        self.welcomeTitle.grid(row=1, column=1, columnspan=6, pady=40, sticky='nsew')
        

        self.welcomeText = Label(self.welcomeFrame,
                                    text="TUkinter is a simple tutorial application for tkinter that is designed using python's tkinter library. The contents of this tutorial application will likely focus on covering the basics of using tkinter for GUI development. This project will come handy especially to beginners who are learning tkinter for the first time, as well as instructors teaching python's tkinter.", 
                                    wraplength=480,
                                    font=('Helvetica', '10'))
        self.welcomeText.grid(row=2, column=1, columnspan=6, padx=20, pady=10, sticky='n')


        ############### TOPICS FRAME ###############
        self.topicsFrame = Frame(self.main)
        # self.topicsFrame.grid(row=0, column=0, columnspan=7, rowspan=10)
        #topicsFrame will only show when called by Topics command from actionMenu

        self.topicsTitle = Label(self.topicsFrame,
                                    text='Choose any topic you want to learn:',
                                    font=('Helvetica', '14'))
        self.topicsTitle.grid(row=0, column=0, columnspan=7, pady=5)

        #create listbox to store all topics
        self.topics_listBox = Listbox(self.topicsFrame,
                                        selectmode=BROWSE,
                                        relief=FLAT,
                                        font=('Helvetica', '12'))
        self.topics_listBox.grid(row=1, column=0, columnspan=4, ipadx=140, ipady=18, padx=25, pady=5)

        #create topic values
        self.topics = ['Getting started with Tkinter',
                        'Geometry Managers: Pack Layout',
                        'Geometry Managers: Grid Layout',
                        'Geometry Managers: Place Layout',
                        'Label widget',
                        'Button widget',
                        'Entry widget',
                        'Frame widget',
                        'Canvas widget',
                        'Menu widget',
                        'Listbox widget',
                        'Scrollbar widget',
                        'Notebook widget',
                        'File I/O',
                        'A simple employee data managemet system',
                        'A simple calculator application']

        #iterate every topic
        for topic in range(len(self.topics)):
            self.topics_listBox.insert(END, self.topics[topic])

        # print(self.topics[0])   #getting started with tkinter


        #create view topic button
        self.viewTopicBtn = Button(self.topicsFrame,
                                    text='View topic',
                                    font=('Helvetica', '10'),
                                    command=self.showTopic)
        self.viewTopicBtn.bind('<Enter>', self.btn_on_enter)
        self.viewTopicBtn.bind('<Leave>', self.btn_on_leave)
        self.viewTopicBtn.grid(row=2, column=3, padx=80, pady=5, ipadx=10, sticky='nsew')



        # pass

    ############### function to display and forget frames ###############
    def showFrame(self, frame):
        #destroy all other frames first
        for child in self.main.winfo_children():
            if child != frame:
                child.grid_forget()

        #display selected frame depending on what's clicked in the menu
        if frame == self.topicsFrame:
            self.topicsFrame.grid(row=0, column=0, columnspan=7, rowspan=10)
        elif frame == self.welcomeFrame:
            self.welcomeFrame.grid(row=0, column=0, columnspan=7, rowspan=10)
        else:
            print('No frame is selected')


    #function to display selected topic
    def showTopic(self):
        #forget sa tanan active nga frames
        for child in self.main.winfo_children():
            child.grid_forget()

        # #use curselection method to retrieve indices of selected items

        self.topicVal = []
        topic_title = self.topics_listBox.curselection()
        for i in topic_title:
            select = self.topics_listBox.get(i)
            self.topicVal.append(select)

        for val in self.topicVal:
            # print(f'Topic {val}')
            #ay sge icheck nlang niya ang string oi

            if val == 'Getting started with Tkinter':
                self.topic0Frame.grid(row=0, column=0)      #GETTING STARTED WITH TKINTER
                print('Getting started with Tkinter')
            elif val == 'Geometry Managers: Pack Layout':
                self.topic1Frame.grid(row=0, column=0)      #GEOMERTY MANAGER: PACK LAYOUT
                print('Geometry Managers: Pack Layout')
            elif val == 'Geometry Managers: Grid Layout':
                self.topic2Frame.grid(row=0, column=0)      #GEOMETRY MANAGER: GRID LAYOUT
                print('Geometry Managers: Grid Layout')
            elif val == 'Geometry Managers: Place Layout':
                self.topic3Frame.grid(row=0, column=0)      #GEOMETRY MANAGER: PLACE LAYOUT
                print('Geometry Managers: Place Layout')
            elif val == 'Label widget':
                self.topic4Frame.grid(row=0, column=0)      #LABEL WIDGET
                print('Label widget')
            elif val == 'Button widget':
                self.topic5Frame.grid(row=0, column=0)      #BUTTON WIDGET
                print('Button widget')
            elif val == 'Entry widget':
                self.topic6Frame.grid(row=0, column=0)      #ENTRY WIDGET
                print('Entry widget')
            elif val == 'Frame widget':
                self.topic7Frame.grid(row=0, column=0)      #FRAME WIDGET
                print('Frame widget')
            elif val == 'Canvas widget':
                self.topic8Frame.grid(row=0, column=0)     #CANVAS WIDGET
                print('Canvas widget')
            elif val == 'Menu widget':
                self.topic9Frame.grid(row=0, column=0)     #MENU WIDGET
                print('Menu widget')
            elif val == 'Listbox widget':
                self.topic10Frame.grid(row=0, column=0)     #LISTBOX WIDGET
                print('Listbox widget')
            elif val == 'Scrollbar widget':
                self.topic11Frame.grid(row=0, column=0)     #SCROLLBAR WIDGET
                print('Scrollbar widget')
            elif val == 'Notebook widget':
                self.topic12Frame.grid(row=0, column=0)     #NOTEBOOK WIDGET
                print('Notebook widget')
            elif val == 'File I/O':
                self.topic13Frame.grid(row=0, column=0)     #FILE I/O
                print('File I/O')
            elif val == 'A simple employee data managemet system':
                self.topic14Frame.grid(row=0, column=0)             #'A simple employee data managemet system'
                print('A simple employee data managemet system')
            elif val == 'A simple calculator application':
                self.topic15Frame.grid(row=0, column=0)
                print('A simple calculator application')
            else:
                print('Null')


    #function para pag hover sa button kay machange ang color eyy
    #on event
    def btn_on_enter(self, event):
        self.btn = event.widget

        if self.btn == self.viewTopicBtn:
            self.viewTopicBtn.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn0:
            self.goBackBtn0.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn1:
            self.goBackBtn1.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn2:
            self.goBackBtn2.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn3:
            self.goBackBtn3.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn4:
            self.goBackBtn4.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn5:
            self.goBackBtn5.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn6:
            self.goBackBtn6.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn7:
            self.goBackBtn7.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn8:
            self.goBackBtn8.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn9:
            self.goBackBtn9.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn10:
            self.goBackBtn10.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn11:
            self.goBackBtn11.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn12:
            self.goBackBtn12.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn13:
            self.goBackBtn13.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn14:
            self.goBackBtn14.config(bg='#2688ED', fg='white')
        elif self.btn == self.goBackBtn15:
            self.goBackBtn15.config(bg='#2688ED', fg='white')
        else:
            print('null')


    def btn_on_leave(self, event):
        self.btn == event.widget

        if self.btn == self.viewTopicBtn:
            self.viewTopicBtn.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn0:
            self.goBackBtn0.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn1:
            self.goBackBtn1.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn2:
            self.goBackBtn2.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn3:
            self.goBackBtn3.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn4:
            self.goBackBtn4.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn5:
            self.goBackBtn5.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn6:
            self.goBackBtn6.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn7:
            self.goBackBtn7.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn8:
            self.goBackBtn8.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn9:
            self.goBackBtn9.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn10:
            self.goBackBtn10.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn11:
            self.goBackBtn11.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn12:
            self.goBackBtn12.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn13:
            self.goBackBtn13.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn14:
            self.goBackBtn14.config(bg='SystemButtonFace', fg='black')
        elif self.btn == self.goBackBtn15:
            self.goBackBtn15.config(bg='SystemButtonFace', fg='black')
        else:
            print('null')



    ############### function to display topics ###############
    def allTopics(self):

        ############### GETTING STARTED WITH TKINTER ###############
        #self.topic0Frame = 'GETTING STARTED WITH TKINTER'
        self.topic0Frame = Frame(self.main)
        # self.topic0Frame.grid(row=0, column=0, columnspan=7, rowspan=10)

        

        self.goBackBtn0 = Button(self.topic0Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn0.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn0.bind('<Leave>', self.btn_on_leave)
        self.goBackBtn0.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic0FrameTitle = Label(self.topic0Frame,
                                        text='Getting started with Tkinter',
                                        font=('Helvetica', '12'))
        self.topic0FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)


        #create notebook widget
        self.topic0noteBook = ttk.Notebook(self.topic0Frame)

        self.topic0tab1 = Frame(self.topic0noteBook)
        self.topic0tab2 = Frame(self.topic0noteBook)

        self.topic0noteBook.add(self.topic0tab1, text='Topic')
        self.topic0noteBook.add(self.topic0tab2, text='Sample Code Snippet')

        self.topic0noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)
        # self.topic0noteBook.pack(fill='both', expand=True)

        # Label(self.topic0tab1, text='What is Tkinter?').grid(row=0, column=0)

        #magbutang tag canvas diri
        
        
        #TAB 1

        #create canvas
        self.topic0tab1Canvas = Canvas(self.topic0tab1)
        self.topic0tab1Canvas.grid(row=0, column=0, sticky='nsew', ipadx=40)

        #create scrollbar
        self.topic0tab1Scroll = Scrollbar(self.topic0tab1, orient=VERTICAL, command=self.topic0tab1Canvas.yview)
        self.topic0tab1Scroll.grid(row=0, column=1, rowspan=10, sticky='nsew')

        #configure canvas
        self.topic0tab1Canvas.configure(yscrollcommand=self.topic0tab1Scroll.set)
        self.topic0tab1Canvas.bind('<Configure>', lambda e: self.topic0tab1Canvas.configure(scrollregion=self.topic0tab1Canvas.bbox('all')))

        #create another frame inside the canvas
        self.topic0tab1secondFrame = Frame(self.topic0tab1Canvas)

        #add the new frame to a window in the canvas
        self.topic0tab1Canvas.create_window((0,0), window=self.topic0tab1secondFrame, anchor='nw')
        
        #i-read ang text files para sa contents
        with open('getting_started.txt') as topic0content:
            self.topic0ContentTxt = topic0content.read()
            
        self.topic0ContentLbl = Label(self.topic0tab1secondFrame,
                                      text=self.topic0ContentTxt,
                                      wraplength=430,
                                      font=('Helvetica', '11'),
                                      justify='left')
        self.topic0ContentLbl.grid(row=0, column=0, columnspan=7, padx=10, pady=10)
        
        
        
        #TAB 2

        Label(self.topic0tab2, text='Code snippet to run a simple "Hello World" program in Tkinter GUI.').grid(row=0, column=0, columnspan=7)
        
        #create text widget to display code snippet
        self.topic0TxtWidget = Text(self.topic0tab2,
                                        font=('Helvetica', '10'),
                                        state='normal')
        self.topic0TxtWidget.grid(row=1, column=0, sticky='nsew')


        with open('topic0_snippet.txt') as topic0:
            self.topic0snipTxt = topic0.read()
            # print(self.topic0snipTxt)
        

        self.topic0TxtWidget.insert(END, self.topic0snipTxt)
        self.topic0TxtWidget.config(state='disabled', height=11, width=68, wrap='word')

        self.topic0tab2RunBtn = Button(self.topic0tab2,
                                        text='Run code snippet',
                                        command=lambda: self.run_snippet('Topic 0'))
        self.topic0tab2RunBtn.grid(row=2, column=0, sticky='nsew')





        ############### GEOMETRY MANAGERS: PACK LAYOUT ###############
        # self.topic1Frame = 'GEOMETRY MANAGERS: PACK LAYOUT'
        self.topic1Frame = Frame(self.main)
        # self.topic1Frame.grid(row=0, column=0)


        self.goBackBtn1 = Button(self.topic1Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn1.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn1.bind('<Leave>', self.btn_on_leave)
        self.goBackBtn1.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic1FrameTitle = Label(self.topic1Frame,
                                        text='Geometry Managers: Pack Layout',
                                        font=('Helvetica', '12'))
        self.topic1FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic1noteBook = ttk.Notebook(self.topic1Frame)

        self.topic1tab1 = Frame(self.topic1noteBook)
        self.topic1tab2 = Frame(self.topic1noteBook)

        self.topic1noteBook.add(self.topic1tab1, text='Topic')
        self.topic1noteBook.add(self.topic1tab2, text='Sample Code Snippet')

        self.topic1noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        # Label(self.topic1tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        
        #TAB 1

        #create canvas
        self.topic1tab1Canvas = Canvas(self.topic1tab1)
        self.topic1tab1Canvas.grid(row=0, column=0, sticky='nsew', ipadx=40)

        #create scrollbar
        self.topic1tab1Scroll = Scrollbar(self.topic1tab1, orient=VERTICAL, command=self.topic1tab1Canvas.yview)
        self.topic1tab1Scroll.grid(row=0, column=1, sticky='nsew')

        #configure canvas
        self.topic1tab1Canvas.configure(yscrollcommand=self.topic1tab1Scroll.set)
        self.topic1tab1Canvas.bind('<Configure>', lambda e: self.topic1tab1Canvas.configure(scrollregion=self.topic1tab1Canvas.bbox('all')))

        #create another frame inside the canvas
        self.topic1tab1secondFrame = Frame(self.topic1tab1Canvas)

        #add the new frame to a window in the canvas
        self.topic1tab1Canvas.create_window((0,0), window=self.topic1tab1secondFrame, anchor='nw')
        
        
        #i-read ang text files para sa contents
        with open('geometry_managers_pack.txt') as topic1content:
            self.topic1ContentTxt = topic1content.read()
            
        self.topic1ContentLbl = Label(self.topic1tab1secondFrame,
                                      text=self.topic1ContentTxt,
                                      wraplength=430,
                                      font=('Helvetica', '11'),
                                      justify='left')
        self.topic1ContentLbl.grid(row=0, column=0, columnspan=7, padx=10, pady=10)
        
        
        #TAB 2
        Label(self.topic1tab2, text='"Pack" Geometry Manager sample code snippet.').grid(row=0, column=0, columnspan=7)

        #create text widget to display code snippet
        self.topic1TxtWidget = Text(self.topic1tab2,
                                        font=('Helvetica', '10'),
                                        state='normal')
        self.topic1TxtWidget.grid(row=1, column=0, sticky='nsew')


        with open('topic1_snippet.txt') as topic1:
            self.topic1snipTxt = topic1.read()
            # print(self.topic0snipTxt)
        

        self.topic1TxtWidget.insert(END, self.topic1snipTxt)
        self.topic1TxtWidget.config(state='disabled', height=11, width=68, wrap='word')

        self.topic1tab2RunBtn = Button(self.topic1tab2,
                                        text='Run code snippet',
                                        command=lambda: self.run_snippet('Topic 1'))
        self.topic1tab2RunBtn.grid(row=2, column=0, sticky='nsew')



        ############### GEOMETRY MANAGERS: GRID LAYOUT ###############
        #self.topic2Frame = 'GEOMETRY MANAGERS: GRID LAYOUT'
        self.topic2Frame = Frame(self.main)
        # self.topic2Frame.grid(row=0, column=0)


        self.goBackBtn2 = Button(self.topic2Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn2.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn2.bind('<Leave>', self.btn_on_leave)
        self.goBackBtn2.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic2FrameTitle = Label(self.topic2Frame,
                                        text='Geometry Managers: Grid Layout',
                                        font=('Helvetica', '12'))
        self.topic2FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic2noteBook = ttk.Notebook(self.topic2Frame)

        self.topic2tab1 = Frame(self.topic2noteBook)
        self.topic2tab2 = Frame(self.topic2noteBook)

        self.topic2noteBook.add(self.topic2tab1, text='Topic')
        self.topic2noteBook.add(self.topic2tab2, text='Sample Code Snippet')

        self.topic2noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        # Label(self.topic2tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        
        #TAB 1

        #create canvas
        self.topic2tab1Canvas = Canvas(self.topic2tab1)
        self.topic2tab1Canvas.grid(row=0, column=0, sticky='nsew', ipadx=40)

        #create scrollbar
        self.topic2tab1Scroll = Scrollbar(self.topic2tab1, orient=VERTICAL, command=self.topic2tab1Canvas.yview)
        self.topic2tab1Scroll.grid(row=0, column=1, sticky='nsew')

        #configure canvas
        self.topic2tab1Canvas.configure(yscrollcommand=self.topic2tab1Scroll.set)
        self.topic2tab1Canvas.bind('<Configure>', lambda e: self.topic2tab1Canvas.configure(scrollregion=self.topic2tab1Canvas.bbox('all')))

        #create another frame inside the canvas
        self.topic2tab1secondFrame = Frame(self.topic2tab1Canvas)

        #add the new frame to a window in the canvas
        self.topic2tab1Canvas.create_window((0,0), window=self.topic2tab1secondFrame, anchor='nw')
        
        #i-read ang text files para sa contents
        with open('geometry_managers_grid.txt') as topic2content:
            self.topic2ContentTxt = topic2content.read()
            
        self.topic2ContentLbl = Label(self.topic2tab1secondFrame,
                                      text=self.topic2ContentTxt,
                                      wraplength=430,
                                      font=('Helvetica', '11'),
                                      justify='left')
        self.topic2ContentLbl.grid(row=0, column=0, columnspan=7, padx=10, pady=10)
        
        
        #TAB 2
        Label(self.topic2tab2, text='"Grid" Geometry Manager sample code snippet.').grid(row=0, column=0, columnspan=7)

        #create text widget to display code snippet
        self.topic2TxtWidget = Text(self.topic2tab2,
                                        font=('Helvetica', '10'),
                                        state='normal')
        self.topic2TxtWidget.grid(row=1, column=0, sticky='nsew')


        with open('topic2_snippet.txt') as topic2:
            self.topic2snipTxt = topic2.read()
            # print(self.topic0snipTxt)
        

        self.topic2TxtWidget.insert(END, self.topic2snipTxt)
        self.topic2TxtWidget.config(state='disabled', height=11, width=68, wrap='word')

        self.topic2tab2RunBtn = Button(self.topic2tab2,
                                        text='Run code snippet',
                                        command=lambda: self.run_snippet('Topic 2'))
        self.topic2tab2RunBtn.grid(row=2, column=0, sticky='nsew')



        ############### GEOMETRY MANAGERS: PLACE LAYOUT ###############
        # self.topic3Frame = 'GEOMETRY MANAGERS: PLACE LAYOUT'
        self.topic3Frame = Frame(self.main)
        # self.topic3Frame.grid(row=0, column=0)


        self.goBackBtn3 = Button(self.topic3Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn3.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn3.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn3.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic3FrameTitle = Label(self.topic3Frame,
                                        text='Geometry Managers: Place Layout',
                                        font=('Helvetica', '12'))
        self.topic3FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic3noteBook = ttk.Notebook(self.topic3Frame)

        self.topic3tab1 = Frame(self.topic3noteBook)
        self.topic3tab2 = Frame(self.topic3noteBook)

        self.topic3noteBook.add(self.topic3tab1, text='Topic')
        self.topic3noteBook.add(self.topic3tab2, text='Sample Code Snippet')

        self.topic3noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        # Label(self.topic3tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        
        #TAB 1

        #create canvas
        self.topic3tab1Canvas = Canvas(self.topic3tab1)
        self.topic3tab1Canvas.grid(row=0, column=0, sticky='nsew', ipadx=40)

        #create scrollbar
        self.topic3tab1Scroll = Scrollbar(self.topic3tab1, orient=VERTICAL, command=self.topic3tab1Canvas.yview)
        self.topic3tab1Scroll.grid(row=0, column=1, sticky='nsew')

        #configure canvas
        self.topic3tab1Canvas.configure(yscrollcommand=self.topic3tab1Scroll.set)
        self.topic3tab1Canvas.bind('<Configure>', lambda e: self.topic3tab1Canvas.configure(scrollregion=self.topic3tab1Canvas.bbox('all')))

        #create another frame inside the canvas
        self.topic3tab1secondFrame = Frame(self.topic3tab1Canvas)

        #add the new frame to a window in the canvas
        self.topic3tab1Canvas.create_window((0,0), window=self.topic3tab1secondFrame, anchor='nw')
        
        #i-read ang text files para sa contents
        with open('geometry_managers_place.txt') as topic3content:
            self.topic3ContentTxt = topic3content.read()
            
        self.topic3ContentLbl = Label(self.topic3tab1secondFrame,
                                      text=self.topic3ContentTxt,
                                      wraplength=430,
                                      font=('Helvetica', '11'),
                                      justify='left')
        self.topic3ContentLbl.grid(row=0, column=0, columnspan=7, padx=10, pady=10)

        #TAB 2
        Label(self.topic3tab2, text='"Place" Geometry Manager code snippet.').grid(row=0, column=0, columnspan=7)

        #create text widget to display code snippet
        self.topic3TxtWidget = Text(self.topic3tab2,
                                        font=('Helvetica', '10'),
                                        state='normal')
        self.topic3TxtWidget.grid(row=1, column=0, sticky='nsew')


        with open('topic3_snippet.txt') as topic3:
            self.topic3snipTxt = topic3.read()
            # print(self.topic0snipTxt)
        

        self.topic3TxtWidget.insert(END, self.topic3snipTxt)
        self.topic3TxtWidget.config(state='disabled', height=11, width=68, wrap='word')

        self.topic3tab2RunBtn = Button(self.topic3tab2,
                                        text='Run code snippet',
                                        command=lambda: self.run_snippet('Topic 3'))
        self.topic3tab2RunBtn.grid(row=2, column=0, sticky='nsew')



        ############### WIDGETS ###############
        # GI WALA NA ANG WIDGETS



        ############### LABEL WIDGET ###############
        # self.topic4Frame = 'LABEL WIDGET'
        self.topic4Frame = Frame(self.main)
        # self.topic4Frame.grid(row=0, column=0)


        self.goBackBtn4 = Button(self.topic4Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn4.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn4.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn4.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic4FrameTitle = Label(self.topic4Frame,
                                        text='Label widget',
                                        font=('Helvetica', '12'))
        self.topic4FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic4noteBook = ttk.Notebook(self.topic4Frame)

        self.topic4tab1 = Frame(self.topic4noteBook)
        self.topic4tab2 = Frame(self.topic4noteBook)

        self.topic4noteBook.add(self.topic4tab1, text='Topic')
        self.topic4noteBook.add(self.topic4tab2, text='Sample Code Snippet')

        self.topic4noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        # Label(self.topic4tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        
        #TAB 1

        #create canvas
        self.topic4tab1Canvas = Canvas(self.topic4tab1)
        self.topic4tab1Canvas.grid(row=0, column=0, sticky='nsew', ipadx=40)

        #create scrollbar
        self.topic4tab1Scroll = Scrollbar(self.topic4tab1, orient=VERTICAL, command=self.topic4tab1Canvas.yview)
        self.topic4tab1Scroll.grid(row=0, column=1, sticky='nsew')

        #configure canvas
        self.topic4tab1Canvas.configure(yscrollcommand=self.topic4tab1Scroll.set)
        self.topic4tab1Canvas.bind('<Configure>', lambda e: self.topic4tab1Canvas.configure(scrollregion=self.topic4tab1Canvas.bbox('all')))

        #create another frame inside the canvas
        self.topic4tab1secondFrame = Frame(self.topic4tab1Canvas)

        #add the new frame to a window in the canvas
        self.topic4tab1Canvas.create_window((0,0), window=self.topic4tab1secondFrame, anchor='nw')
        
        
        #i-read ang text files para sa contents
        with open('label_widget.txt') as topic4content:
            self.topic4ContentTxt = topic4content.read()
            
        self.topic4ContentLbl = Label(self.topic4tab1secondFrame,
                                      text=self.topic4ContentTxt,
                                      wraplength=430,
                                      font=('Helvetica', '11'),
                                      justify='left')
        self.topic4ContentLbl.grid(row=0, column=0, columnspan=7, padx=10, pady=10)
        
        
        #TAB 2
        Label(self.topic4tab2, text='"Label" widget sample code snippet.').grid(row=0, column=0, columnspan=7)

        #create text widget to display code snippet
        self.topic4TxtWidget = Text(self.topic4tab2,
                                        font=('Helvetica', '10'),
                                        state='normal')
        self.topic4TxtWidget.grid(row=1, column=0, sticky='nsew')


        with open('topic4_snippet.txt') as topic4:
            self.topic4snipTxt = topic4.read()
            # print(self.topic0snipTxt)
        

        self.topic4TxtWidget.insert(END, self.topic4snipTxt)
        self.topic4TxtWidget.config(state='disabled', height=11, width=68, wrap='word')

        self.topic4tab2RunBtn = Button(self.topic4tab2,
                                        text='Run code snippet',
                                        command=lambda: self.run_snippet('Topic 4'))
        self.topic4tab2RunBtn.grid(row=2, column=0, sticky='nsew')



        ############### BUTTON WIDGET ###############
        # self.topic5Frame = 'BUTTON WIDGET'
        self.topic5Frame = Frame(self.main)
        # self.topic5Frame.grid(row=0, column=0)


        self.goBackBtn5 = Button(self.topic5Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn5.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn5.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn5.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic5FrameTitle = Label(self.topic5Frame,
                                        text='Button widget',
                                        font=('Helvetica', '12'))
        self.topic5FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic5noteBook = ttk.Notebook(self.topic5Frame)

        self.topic5tab1 = Frame(self.topic5noteBook)
        self.topic5tab2 = Frame(self.topic5noteBook)

        self.topic5noteBook.add(self.topic5tab1, text='Topic')
        self.topic5noteBook.add(self.topic5tab2, text='Sample Code Snippet')

        self.topic5noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        # Label(self.topic5tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        
        #TAB 1

        #create canvas
        self.topic5tab1Canvas = Canvas(self.topic5tab1)
        self.topic5tab1Canvas.grid(row=0, column=0, sticky='nsew', ipadx=40)

        #create scrollbar
        self.topic5tab1Scroll = Scrollbar(self.topic5tab1, orient=VERTICAL, command=self.topic5tab1Canvas.yview)
        self.topic5tab1Scroll.grid(row=0, column=1, sticky='nsew')

        #configure canvas
        self.topic5tab1Canvas.configure(yscrollcommand=self.topic5tab1Scroll.set)
        self.topic5tab1Canvas.bind('<Configure>', lambda e: self.topic5tab1Canvas.configure(scrollregion=self.topic5tab1Canvas.bbox('all')))

        #create another frame inside the canvas
        self.topic5tab1secondFrame = Frame(self.topic5tab1Canvas)

        #add the new frame to a window in the canvas
        self.topic5tab1Canvas.create_window((0,0), window=self.topic5tab1secondFrame, anchor='nw')
        
        
        #i-read ang text files para sa contents
        with open('button_widget.txt') as topic5content:
            self.topic5ContentTxt = topic5content.read()
            
        self.topic5ContentLbl = Label(self.topic5tab1secondFrame,
                                      text=self.topic5ContentTxt,
                                      wraplength=430,
                                      font=('Helvetica', '11'),
                                      justify='left')
        self.topic5ContentLbl.grid(row=0, column=0, columnspan=7, padx=10, pady=10)
        
        
        #TAB 2
        Label(self.topic5tab2, text='"Button" widget sample code snippet.').grid(row=0, column=0, columnspan=7)

        #create text widget to display code snippet
        self.topic5TxtWidget = Text(self.topic5tab2,
                                        font=('Helvetica', '10'),
                                        state='normal')
        self.topic5TxtWidget.grid(row=1, column=0, sticky='nsew')


        with open('topic5_snippet.txt') as topic5:
            self.topic5snipTxt = topic5.read()
            # print(self.topic0snipTxt)
        

        self.topic5TxtWidget.insert(END, self.topic5snipTxt)
        self.topic5TxtWidget.config(state='disabled', height=11, width=68, wrap='word')

        self.topic5tab2RunBtn = Button(self.topic5tab2,
                                        text='Run code snippet',
                                        command=lambda: self.run_snippet('Topic 5'))
        self.topic5tab2RunBtn.grid(row=2, column=0, sticky='nsew')


        ############### ENTRY WIDGET ###############
        # self.topic6Frame = 'ENTRY WIDGET'
        self.topic6Frame = Frame(self.main)
        # self.topic6Frame.grid(row=0, column=0)


        self.goBackBtn6 = Button(self.topic6Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn6.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn6.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn6.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic6FrameTitle = Label(self.topic6Frame,
                                        text='Entry widget',
                                        font=('Helvetica', '12'))
        self.topic6FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic6noteBook = ttk.Notebook(self.topic6Frame)

        self.topic6tab1 = Frame(self.topic6noteBook)
        self.topic6tab2 = Frame(self.topic6noteBook)

        self.topic6noteBook.add(self.topic6tab1, text='Topic')
        self.topic6noteBook.add(self.topic6tab2, text='Sample Code Snippet')

        self.topic6noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        # Label(self.topic6tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        
        #TAB 1

        #create canvas
        self.topic6tab1Canvas = Canvas(self.topic6tab1)
        self.topic6tab1Canvas.grid(row=0, column=0, sticky='nsew', ipadx=40)

        #create scrollbar
        self.topic6tab1Scroll = Scrollbar(self.topic6tab1, orient=VERTICAL, command=self.topic6tab1Canvas.yview)
        self.topic6tab1Scroll.grid(row=0, column=1, sticky='nsew')

        #configure canvas
        self.topic6tab1Canvas.configure(yscrollcommand=self.topic6tab1Scroll.set)
        self.topic6tab1Canvas.bind('<Configure>', lambda e: self.topic6tab1Canvas.configure(scrollregion=self.topic6tab1Canvas.bbox('all')))

        #create another frame inside the canvas
        self.topic6tab1secondFrame = Frame(self.topic6tab1Canvas)

        #add the new frame to a window in the canvas
        self.topic6tab1Canvas.create_window((0,0), window=self.topic6tab1secondFrame, anchor='nw')
        
        
        #i-read ang text files para sa contents
        with open('entry_widget.txt') as topic6content:
            self.topic6ContentTxt = topic6content.read()
            
        self.topic6ContentLbl = Label(self.topic6tab1secondFrame,
                                      text=self.topic6ContentTxt,
                                      wraplength=430,
                                      font=('Helvetica', '11'),
                                      justify='left')
        self.topic6ContentLbl.grid(row=0, column=0, columnspan=7, padx=10, pady=10)
        
        
        #TAB 2
        Label(self.topic6tab2, text='"Entry" widget sample code snippet').grid(row=0, column=0, columnspan=7)


        #create text widget to display code snippet
        self.topic6TxtWidget = Text(self.topic6tab2,
                                        font=('Helvetica', '10'),
                                        state='normal')
        self.topic6TxtWidget.grid(row=1, column=0, sticky='nsew')


        with open('topic6_snippet.txt') as topic6:
            self.topic6snipTxt = topic6.read()
            # print(self.topic0snipTxt)
        

        self.topic6TxtWidget.insert(END, self.topic6snipTxt)
        self.topic6TxtWidget.config(state='disabled', height=11, width=68, wrap='word')

        self.topic6tab2RunBtn = Button(self.topic6tab2,
                                        text='Run code snippet',
                                        command=lambda: self.run_snippet('Topic 6'))
        self.topic6tab2RunBtn.grid(row=2, column=0, sticky='nsew')


        ############### FRAME WIDGET ###############
        # self.topic7Frame = 'FRAME WIDGET'
        self.topic7Frame = Frame(self.main)
        # self.topic7Frame.grid(row=0, column=0)


        self.goBackBtn7 = Button(self.topic7Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn7.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn7.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn7.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic7FrameTitle = Label(self.topic7Frame,
                                        text='Frame widget',
                                        font=('Helvetica', '12'))
        self.topic7FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic7noteBook = ttk.Notebook(self.topic7Frame)

        self.topic7tab1 = Frame(self.topic7noteBook)
        self.topic7tab2 = Frame(self.topic7noteBook)

        self.topic7noteBook.add(self.topic7tab1, text='Topic')
        self.topic7noteBook.add(self.topic7tab2, text='Sample Code Snippet')

        self.topic7noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        # Label(self.topic7tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        
        #TAB 1

        #create canvas
        self.topic7tab1Canvas = Canvas(self.topic7tab1)
        self.topic7tab1Canvas.grid(row=0, column=0, sticky='nsew', ipadx=40)

        #create scrollbar
        self.topic7tab1Scroll = Scrollbar(self.topic7tab1, orient=VERTICAL, command=self.topic7tab1Canvas.yview)
        self.topic7tab1Scroll.grid(row=0, column=1, sticky='nsew')

        #configure canvas
        self.topic7tab1Canvas.configure(yscrollcommand=self.topic7tab1Scroll.set)
        self.topic7tab1Canvas.bind('<Configure>', lambda e: self.topic7tab1Canvas.configure(scrollregion=self.topic7tab1Canvas.bbox('all')))

        #create another frame inside the canvas
        self.topic7tab1secondFrame = Frame(self.topic7tab1Canvas)

        #add the new frame to a window in the canvas
        self.topic7tab1Canvas.create_window((0,0), window=self.topic7tab1secondFrame, anchor='nw')
        

        #i-read ang text files para sa contents
        with open('frame_widget.txt') as topic7content:
            self.topic7ContentTxt = topic7content.read()
            
        self.topic7ContentLbl = Label(self.topic7tab1secondFrame,
                                      text=self.topic7ContentTxt,
                                      wraplength=430,
                                      font=('Helvetica', '11'),
                                      justify='left')
        self.topic7ContentLbl.grid(row=0, column=0, columnspan=7, padx=10, pady=10)
        
        #TAB 2
        Label(self.topic7tab2, text='"Frame" widget sample code snippet.').grid(row=0, column=0, columnspan=7)

        #create text widget to display code snippet
        self.topic7TxtWidget = Text(self.topic7tab2,
                                        font=('Helvetica', '10'),
                                        state='normal')
        self.topic7TxtWidget.grid(row=1, column=0, sticky='nsew')


        with open('topic7_snippet.txt') as topic7:
            self.topic7snipTxt = topic7.read()
            # print(self.topic0snipTxt)
        

        self.topic7TxtWidget.insert(END, self.topic7snipTxt)
        self.topic7TxtWidget.config(state='disabled', height=11, width=68, wrap='word')

        self.topic7tab2RunBtn = Button(self.topic7tab2,
                                        text='Run code snippet',
                                        command=lambda: self.run_snippet('Topic 7'))
        self.topic7tab2RunBtn.grid(row=2, column=0, sticky='nsew')


        ############### CANVAS WIDGET ###############
        # self.topic8Frame = 'CANVAS WIDGET'
        self.topic8Frame = Frame(self.main)
        # self.topic8Frame.grid(row=0, column=0)


        self.goBackBtn8 = Button(self.topic8Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn8.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn8.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn8.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic8FrameTitle = Label(self.topic8Frame,
                                        text='Canvas widget',
                                        font=('Helvetica', '12'))
        self.topic8FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic8noteBook = ttk.Notebook(self.topic8Frame)

        self.topic8tab1 = Frame(self.topic8noteBook)
        self.topic8tab2 = Frame(self.topic8noteBook)

        self.topic8noteBook.add(self.topic8tab1, text='Topic')
        self.topic8noteBook.add(self.topic8tab2, text='Sample Code Snippet')

        self.topic8noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        # Label(self.topic8tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        
        #TAB 1

        #create canvas
        self.topic8tab1Canvas = Canvas(self.topic8tab1)
        self.topic8tab1Canvas.grid(row=0, column=0, sticky='nsew', ipadx=40)

        #create scrollbar
        self.topic8tab1Scroll = Scrollbar(self.topic8tab1, orient=VERTICAL, command=self.topic8tab1Canvas.yview)
        self.topic8tab1Scroll.grid(row=0, column=1, sticky='nsew')

        #configure canvas
        self.topic8tab1Canvas.configure(yscrollcommand=self.topic8tab1Scroll.set)
        self.topic8tab1Canvas.bind('<Configure>', lambda e: self.topic8tab1Canvas.configure(scrollregion=self.topic8tab1Canvas.bbox('all')))

        #create another frame inside the canvas
        self.topic8tab1secondFrame = Frame(self.topic8tab1Canvas)

        #add the new frame to a window in the canvas
        self.topic8tab1Canvas.create_window((0,0), window=self.topic8tab1secondFrame, anchor='nw')
        
        #i-read ang text files para sa contents
        with open('canvas_widget.txt') as topic8content:
            self.topic8ContentTxt = topic8content.read()
            
        self.topic8ContentLbl = Label(self.topic8tab1secondFrame,
                                      text=self.topic8ContentTxt,
                                      wraplength=430,
                                      font=('Helvetica', '11'),
                                      justify='left')
        self.topic8ContentLbl.grid(row=0, column=0, columnspan=7, padx=10, pady=10)
        
        
        #TAB 2
        Label(self.topic8tab2, text='"Canvas" widget sample code snippet.').grid(row=0, column=0, columnspan=7)

        #create text widget to display code snippet
        self.topic8TxtWidget = Text(self.topic8tab2,
                                        font=('Helvetica', '10'),
                                        state='normal')
        self.topic8TxtWidget.grid(row=1, column=0, sticky='nsew')


        with open('topic8_snippet.txt') as topic8:
            self.topic8snipTxt = topic8.read()
            # print(self.topic0snipTxt)
        

        self.topic8TxtWidget.insert(END, self.topic8snipTxt)
        self.topic8TxtWidget.config(state='disabled', height=11, width=68, wrap='word')

        self.topic8tab2RunBtn = Button(self.topic8tab2,
                                        text='Run code snippet',
                                        command=lambda: self.run_snippet('Topic 8'))
        self.topic8tab2RunBtn.grid(row=2, column=0, sticky='nsew')



        ############### MENU WIDGET ###############
        # self.topic9Frame = 'CANVAS WIDGET'
        self.topic9Frame = Frame(self.main)
        # self.topic9Frame.grid(row=0, column=0)


        self.goBackBtn9 = Button(self.topic9Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn9.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn9.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn9.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic9FrameTitle = Label(self.topic9Frame,
                                        text='Menu widget',
                                        font=('Helvetica', '12'))
        self.topic9FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic9noteBook = ttk.Notebook(self.topic9Frame)

        self.topic9tab1 = Frame(self.topic9noteBook)
        self.topic9tab2 = Frame(self.topic9noteBook)

        self.topic9noteBook.add(self.topic9tab1, text='Topic')
        self.topic9noteBook.add(self.topic9tab2, text='Sample Code Snippet')

        self.topic9noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        # Label(self.topic9tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        

        #TAB 1

        #create canvas
        self.topic9tab1Canvas = Canvas(self.topic9tab1)
        self.topic9tab1Canvas.grid(row=0, column=0, sticky='nsew', ipadx=40)

        #create scrollbar
        self.topic9tab1Scroll = Scrollbar(self.topic9tab1, orient=VERTICAL, command=self.topic9tab1Canvas.yview)
        self.topic9tab1Scroll.grid(row=0, column=1, sticky='nsew')

        #configure canvas
        self.topic9tab1Canvas.configure(yscrollcommand=self.topic9tab1Scroll.set)
        self.topic9tab1Canvas.bind('<Configure>', lambda e: self.topic9tab1Canvas.configure(scrollregion=self.topic9tab1Canvas.bbox('all')))

        #create another frame inside the canvas
        self.topic9tab1secondFrame = Frame(self.topic9tab1Canvas)

        #add the new frame to a window in the canvas
        self.topic9tab1Canvas.create_window((0,0), window=self.topic9tab1secondFrame, anchor='nw')
        
        
        
        #i-read ang text files para sa contents
        with open('menu_widget.txt') as topic9content:
            self.topic9ContentTxt = topic9content.read()
            
        self.topic9ContentLbl = Label(self.topic9tab1secondFrame,
                                      text=self.topic9ContentTxt,
                                      wraplength=430,
                                      font=('Helvetica', '11'),
                                      justify='left')
        self.topic9ContentLbl.grid(row=0, column=0, columnspan=7, padx=10, pady=10)


        # #TAB 2
        # Label(self.topic9tab2, text='"Menu" widget sample code snippet', width=67, height=16).grid(row=0, column=0)

        #create notebook widget
        # self.topic9noteBook = ttk.Notebook(self.topic9Frame)

        # self.topic9tab1 = Frame(self.topic9noteBook)
        # self.topic9tab2 = Frame(self.topic9noteBook)

        # self.topic9noteBook.add(self.topic9tab1, text='Topic')
        # self.topic9noteBook.add(self.topic9tab2, text='Sample Code Snippet')

        # self.topic9noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        # Label(self.topic9tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        
        
        
        #tab 2
        Label(self.topic9tab2, text='"Menu" widget sample code snippet.').grid(row=0, column=0, columnspan=7)

        #create text widget to display code snippet
        self.topic9TxtWidget = Text(self.topic9tab2,
                                        font=('Helvetica', '10'),
                                        state='normal')
        self.topic9TxtWidget.grid(row=1, column=0, sticky='nsew')


        with open('topic9_snippet.txt') as topic9:
            self.topic9snipTxt = topic9.read()
            # print(self.topic0snipTxt)
        

        self.topic9TxtWidget.insert(END, self.topic9snipTxt)
        self.topic9TxtWidget.config(state='disabled', height=11, width=68, wrap='word')

        self.topic9tab2RunBtn = Button(self.topic9tab2,
                                        text='Run code snippet',
                                        command=lambda: self.run_snippet('Topic 9'))
        self.topic9tab2RunBtn.grid(row=2, column=0, sticky='nsew')


        ############### LISTBOX WIDGET ###############
        # self.topic10Frame = 'LISTBOX WIDGET'
        self.topic10Frame = Frame(self.main)
        # self.topic10Frame.grid(row=0, column=0)


        self.goBackBtn10 = Button(self.topic10Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn10.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn10.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn10.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic10FrameTitle = Label(self.topic10Frame,
                                        text='Listbox widget',
                                        font=('Helvetica', '12'))
        self.topic10FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic10noteBook = ttk.Notebook(self.topic10Frame)

        self.topic10tab1 = Frame(self.topic10noteBook)
        self.topic10tab2 = Frame(self.topic10noteBook)

        self.topic10noteBook.add(self.topic10tab1, text='Topic')
        self.topic10noteBook.add(self.topic10tab2, text='Sample Code Snippet')

        self.topic10noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        # Label(self.topic10tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)

        #TAB 1

        #create canvas
        self.topic10tab1Canvas = Canvas(self.topic10tab1)
        self.topic10tab1Canvas.grid(row=0, column=0, sticky='nsew', ipadx=40)

        #create scrollbar
        self.topic10tab1Scroll = Scrollbar(self.topic10tab1, orient=VERTICAL, command=self.topic10tab1Canvas.yview)
        self.topic10tab1Scroll.grid(row=0, column=1, sticky='nsew')

        #configure canvas
        self.topic10tab1Canvas.configure(yscrollcommand=self.topic10tab1Scroll.set)
        self.topic10tab1Canvas.bind('<Configure>', lambda e: self.topic10tab1Canvas.configure(scrollregion=self.topic10tab1Canvas.bbox('all')))

        #create another frame inside the canvas
        self.topic10tab1secondFrame = Frame(self.topic10tab1Canvas)

        #add the new frame to a window in the canvas
        self.topic10tab1Canvas.create_window((0,0), window=self.topic10tab1secondFrame, anchor='nw')
        
        
        #i-read ang text files para sa contents
        with open('listbox_widget.txt') as topic10content:
            self.topic10ContentTxt = topic10content.read()
            
        self.topic10ContentLbl = Label(self.topic10tab1secondFrame,
                                      text=self.topic10ContentTxt,
                                      wraplength=430,
                                      font=('Helvetica', '11'),
                                      justify='left')
        self.topic10ContentLbl.grid(row=0, column=0, columnspan=7, padx=10, pady=10)
        
        #TAB 2
        Label(self.topic10tab2, text='"Listbox" widget sample code snippet.').grid(row=0, column=0, columnspan=7)


        #create text widget to display code snippet
        self.topic10TxtWidget = Text(self.topic10tab2,
                                        font=('Helvetica', '10'),
                                        state='normal')
        self.topic10TxtWidget.grid(row=1, column=0, sticky='nsew')


        with open('topic10_snippet.txt') as topic10:
            self.topic10snipTxt = topic10.read()
            # print(self.topic0snipTxt)
        

        self.topic10TxtWidget.insert(END, self.topic10snipTxt)
        self.topic10TxtWidget.config(state='disabled', height=11, width=68, wrap='word')

        self.topic10tab2RunBtn = Button(self.topic10tab2,
                                        text='Run code snippet',
                                        command=lambda: self.run_snippet('Topic 10'))
        self.topic10tab2RunBtn.grid(row=2, column=0, sticky='nsew')



        ############### SCROLLBAR WIDGET ###############
        # self.topic11Frame = 'SCROLLBAR WIDGET'
        self.topic11Frame = Frame(self.main)
        # self.topic11Frame.grid(row=0, column=0)


        self.goBackBtn11 = Button(self.topic11Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn11.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn11.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn11.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic11FrameTitle = Label(self.topic11Frame,
                                        text='Scrollbar widget',
                                        font=('Helvetica', '12'))
        self.topic11FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic11noteBook = ttk.Notebook(self.topic11Frame)

        self.topic11tab1 = Frame(self.topic11noteBook)
        self.topic11tab2 = Frame(self.topic11noteBook)

        self.topic11noteBook.add(self.topic11tab1, text='Topic')
        self.topic11noteBook.add(self.topic11tab2, text='Sample Code Snippet')

        self.topic11noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        # Label(self.topic11tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        
        #TAB 1

        #create canvas
        self.topic11tab1Canvas = Canvas(self.topic11tab1)
        self.topic11tab1Canvas.grid(row=0, column=0, sticky='nsew', ipadx=40)

        #create scrollbar
        self.topic11tab1Scroll = Scrollbar(self.topic11tab1, orient=VERTICAL, command=self.topic11tab1Canvas.yview)
        self.topic11tab1Scroll.grid(row=0, column=1, sticky='nsew')

        #configure canvas
        self.topic11tab1Canvas.configure(yscrollcommand=self.topic11tab1Scroll.set)
        self.topic11tab1Canvas.bind('<Configure>', lambda e: self.topic11tab1Canvas.configure(scrollregion=self.topic11tab1Canvas.bbox('all')))

        #create another frame inside the canvas
        self.topic11tab1secondFrame = Frame(self.topic11tab1Canvas)

        #add the new frame to a window in the canvas
        self.topic11tab1Canvas.create_window((0,0), window=self.topic11tab1secondFrame, anchor='nw')
        
        #i-read ang text files para sa contents
        with open('scrollbar_widget.txt') as topic11content:
            self.topic11ContentTxt = topic11content.read()
            
        self.topic11ContentLbl = Label(self.topic11tab1secondFrame,
                                      text=self.topic11ContentTxt,
                                      wraplength=430,
                                      font=('Helvetica', '11'),
                                      justify='left')
        self.topic11ContentLbl.grid(row=0, column=0, columnspan=7, padx=10, pady=10)
        
        
        #TAB 2
        Label(self.topic11tab2, text='"Scrollbar" widget sample code snippet.').grid(row=0, column=0, columnspan=7)

        #create text widget to display code snippet
        self.topic11TxtWidget = Text(self.topic11tab2,
                                        font=('Helvetica', '10'),
                                        state='normal')
        self.topic11TxtWidget.grid(row=1, column=0, sticky='nsew')


        with open('topic11_snippet.txt') as topic11:
            self.topic11snipTxt = topic11.read()
            # print(self.topic0snipTxt)
        

        self.topic11TxtWidget.insert(END, self.topic11snipTxt)
        self.topic11TxtWidget.config(state='disabled', height=11, width=68, wrap='word')

        self.topic11tab2RunBtn = Button(self.topic11tab2,
                                        text='Run code snippet',
                                        command=lambda: self.run_snippet('Topic 11'))
        self.topic11tab2RunBtn.grid(row=2, column=0, sticky='nsew')


        ############### NOTEBOOK WIDGET ###############
        # self.topic12Frame = 'NOTEBOOK WIDGET'
        self.topic12Frame = Frame(self.main)
        # self.topic12Frame.grid(row=0, column=0)


        self.goBackBtn12 = Button(self.topic12Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn12.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn12.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn12.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic12FrameTitle = Label(self.topic12Frame,
                                        text='Notebook widget',
                                        font=('Helvetica', '12'))
        self.topic12FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic12noteBook = ttk.Notebook(self.topic12Frame)

        self.topic12tab1 = Frame(self.topic12noteBook)
        self.topic12tab2 = Frame(self.topic12noteBook)

        self.topic12noteBook.add(self.topic12tab1, text='Topic')
        self.topic12noteBook.add(self.topic12tab2, text='Sample Code Snippet')

        self.topic12noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        # Label(self.topic12tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        

        #TAB 1

        #create canvas
        self.topic12tab1Canvas = Canvas(self.topic12tab1)
        self.topic12tab1Canvas.grid(row=0, column=0, sticky='nsew', ipadx=40)

        #create scrollbar
        self.topic12tab1Scroll = Scrollbar(self.topic12tab1, orient=VERTICAL, command=self.topic12tab1Canvas.yview)
        self.topic12tab1Scroll.grid(row=0, column=1, sticky='nsew')

        #configure canvas
        self.topic12tab1Canvas.configure(yscrollcommand=self.topic12tab1Scroll.set)
        self.topic12tab1Canvas.bind('<Configure>', lambda e: self.topic12tab1Canvas.configure(scrollregion=self.topic12tab1Canvas.bbox('all')))

        #create another frame inside the canvas
        self.topic12tab1secondFrame = Frame(self.topic12tab1Canvas)

        #add the new frame to a window in the canvas
        self.topic12tab1Canvas.create_window((0,0), window=self.topic12tab1secondFrame, anchor='nw')
        
        
        #i-read ang text files para sa contents
        with open('notebook_widget.txt') as topic12content:
            self.topic12ContentTxt = topic12content.read()
            
        self.topic12ContentLbl = Label(self.topic12tab1secondFrame,
                                      text=self.topic12ContentTxt,
                                      wraplength=430,
                                      font=('Helvetica', '11'),
                                      justify='left')
        self.topic12ContentLbl.grid(row=0, column=0, columnspan=7, padx=10, pady=10)
        
        #TAB 2
        Label(self.topic12tab2, text='"Notebook" widget sample code snippet.').grid(row=0, column=0, columnspan=7)

        #create text widget to display code snippet
        self.topic12TxtWidget = Text(self.topic12tab2,
                                        font=('Helvetica', '10'),
                                        state='normal')
        self.topic12TxtWidget.grid(row=1, column=0, sticky='nsew')


        with open('topic12_snippet.txt') as topic12:
            self.topic12snipTxt = topic12.read()
            # print(self.topic0snipTxt)
        

        self.topic12TxtWidget.insert(END, self.topic12snipTxt)
        self.topic12TxtWidget.config(state='disabled', height=11, width=68, wrap='word')

        self.topic12tab2RunBtn = Button(self.topic12tab2,
                                        text='Run code snippet',
                                        command=lambda: self.run_snippet('Topic 12'))
        self.topic12tab2RunBtn.grid(row=2, column=0, sticky='nsew')


        ############### FILE I/O ###############
        # self.topic13Frame = 'FILE I/O'
        self.topic13Frame = Frame(self.main)
        # self.topic13Frame.grid(row=0, column=0)


        self.goBackBtn13 = Button(self.topic13Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn13.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn13.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn13.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic13FrameTitle = Label(self.topic13Frame,
                                        text='FILE I/O',
                                        font=('Helvetica', '12'))
        self.topic13FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic13noteBook = ttk.Notebook(self.topic13Frame)

        self.topic13tab1 = Frame(self.topic13noteBook)
        # self.topic13tab2 = Frame(self.topic13noteBook)

        self.topic13noteBook.add(self.topic13tab1, text='Topic')
        # self.topic13noteBook.add(self.topic13tab2, text='Sample Code Snippet')

        self.topic13noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        # Label(self.topic13tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        
        #TAB 1

        #create canvas
        self.topic13tab1Canvas = Canvas(self.topic13tab1)
        self.topic13tab1Canvas.grid(row=0, column=0, sticky='nsew', ipadx=40)

        #create scrollbar
        self.topic13tab1Scroll = Scrollbar(self.topic13tab1, orient=VERTICAL, command=self.topic13tab1Canvas.yview)
        self.topic13tab1Scroll.grid(row=0, column=1, sticky='nsew')

        #configure canvas
        self.topic13tab1Canvas.configure(yscrollcommand=self.topic13tab1Scroll.set)
        self.topic13tab1Canvas.bind('<Configure>', lambda e: self.topic13tab1Canvas.configure(scrollregion=self.topic13tab1Canvas.bbox('all')))

        #create another frame inside the canvas
        self.topic13tab1secondFrame = Frame(self.topic13tab1Canvas)

        #add the new frame to a window in the canvas
        self.topic13tab1Canvas.create_window((0,0), window=self.topic13tab1secondFrame, anchor='nw')
        
        #i-read ang text files para sa contents
        with open('file_io.txt') as topic13content:
            self.topic13ContentTxt = topic13content.read()
            
        self.topic13ContentLbl = Label(self.topic13tab1secondFrame,
                                      text=self.topic13ContentTxt,
                                      wraplength=430,
                                      font=('Helvetica', '11'),
                                      justify='left')
        self.topic13ContentLbl.grid(row=0, column=0, columnspan=7, padx=10, pady=15)
        
        # Label(self.topic13tab2, text='This is tab 2', width=67, height=16).grid(row=0, column=0)



        ############### A SIMPLE EMPLOYEE DATA MANAGEMENT SYSTEM ###############
        # self.topic14Frame = 'A SIMPLE EMPLOYEE DATA MANAGEMENT SYSTEM'
        self.topic14Frame = Frame(self.main)
        # self.topic14Frame.grid(row=0, column=0)


        self.goBackBtn14 = Button(self.topic14Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn14.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn14.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn14.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic14FrameTitle = Label(self.topic14Frame,
                                        text='A simple employee data managemet system',
                                        font=('Helvetica', '12'))
        self.topic14FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic14noteBook = ttk.Notebook(self.topic14Frame)

        # self.topic14tab1 = Frame(self.topic14noteBook)
        self.topic14tab2 = Frame(self.topic14noteBook)

        # self.topic14noteBook.add(self.topic14tab1, text='Topic')
        self.topic14noteBook.add(self.topic14tab2, text='Sample Code Snippet')

        self.topic14noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        # Label(self.topic14tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        

        #TAB 1

        #create canvas
        # self.topic14tab1Canvas = Canvas(self.topic14tab1)
        # self.topic14tab1Canvas.grid(row=0, column=0, sticky='nsew', ipadx=40)

        # #create scrollbar
        # self.topic14tab1Scroll = Scrollbar(self.topic14tab1, orient=VERTICAL, command=self.topic14tab1Canvas.yview)
        # self.topic14tab1Scroll.grid(row=0, column=1, sticky='nsew')

        # #configure canvas
        # self.topic14tab1Canvas.configure(yscrollcommand=self.topic14tab1Scroll.set)
        # self.topic14tab1Canvas.bind('<Configure>', lambda e: self.topic14tab1Canvas.configure(scrollregion=self.topic14tab1Canvas.bbox('all')))

        # #create another frame inside the canvas
        # self.topic14tab1secondFrame = Frame(self.topic14tab1Canvas)

        # #add the new frame to a window in the canvas
        # self.topic14tab1Canvas.create_window((0,0), window=self.topic14tab1secondFrame, anchor='nw')
        
        # #i-read ang text files para sa contents
        # with open('employee_management.txt') as topic14content:
        #     self.topic14ContentTxt = topic14content.read()
            
        # self.topic14ContentLbl = Label(self.topic14tab1secondFrame,
        #                               text=self.topic14ContentTxt,
        #                               wraplength=430,
        #                               font=('Helvetica', '11'),
        #                               justify='left')
        # self.topic14ContentLbl.grid(row=0, column=0, columnspan=7, padx=10, pady=15)
        
        #TAB 2
        Label(self.topic14tab2, text='A simple employee data management system').grid(row=0, column=0, columnspan=7)

        #create text widget to display code snippet
        self.topic14TxtWidget = Text(self.topic14tab2,
                                        font=('Helvetica', '10'),
                                        state='normal')
        self.topic14TxtWidget.grid(row=1, column=0, sticky='nsew')


        with open('topic14_snippet.txt') as topic14:
            self.topic14snipTxt = topic14.read()
            # print(self.topic0snipTxt)
        

        self.topic14TxtWidget.insert(END, self.topic14snipTxt)
        self.topic14TxtWidget.config(state='disabled', height=11, width=68, wrap='word')
        
        # self.topic14tab2RunBtn = Button(self.topic14tab2,
        #                                 text='Run code snippet',
        #                                 command=lambda: self.run_snippet('Topic 14'))
        # self.topic14tab2RunBtn.grid(row=2, column=0, sticky='nsew')


        
        ############### A SIMPLE CALCULATOR APPLICATION ###############
        # self.topic15Frame = 'A SIMPLE CALCULATOR APPLICATION'
        self.topic15Frame = Frame(self.main)
        # self.topic15Frame.grid(row=0, column=0)


        self.goBackBtn15 = Button(self.topic15Frame,
                                    text='Back to topics',
                                    command=lambda: self.showFrame(self.topicsFrame))
        self.goBackBtn15.bind('<Enter>', self.btn_on_enter)
        self.goBackBtn15.bind('<Leave>', self.btn_on_leave)                                    
        self.goBackBtn15.grid(row=0, column=0, columnspan=2, ipadx=5, padx=5, pady=7)


        self.topic15FrameTitle = Label(self.topic15Frame,
                                        text='A simple calculator application',
                                        font=('Helvetica', '12'))
        self.topic15FrameTitle.grid(row=0, column=1, columnspan=6, sticky='nsew', padx=75)

        #create notebook widget
        self.topic15noteBook = ttk.Notebook(self.topic15Frame)

        # self.topic15tab1 = Frame(self.topic15noteBook)
        self.topic15tab2 = Frame(self.topic15noteBook)

        # self.topic15noteBook.add(self.topic15tab1, text='Topic')
        self.topic15noteBook.add(self.topic15tab2, text='Sample Code Snippet')

        self.topic15noteBook.grid(row=1, column=0, columnspan=7, sticky='nsew', padx=20, pady=5)

        # Label(self.topic15tab1, text='This is tab 1', width=67, height=16).grid(row=0, column=0)
        
        #TAB 1

        #create canvas
        # self.topic15tab1Canvas = Canvas(self.topic15tab1)
        # self.topic15tab1Canvas.grid(row=0, column=0, sticky='nsew', ipadx=40)

        # #create scrollbar
        # self.topic15tab1Scroll = Scrollbar(self.topic15tab1, orient=VERTICAL, command=self.topic15tab1Canvas.yview)
        # self.topic15tab1Scroll.grid(row=0, column=1, sticky='w')

        # #configure canvas
        # self.topic15tab1Canvas.configure(yscrollcommand=self.topic15tab1Scroll.set)
        # self.topic15tab1Canvas.bind('<Configure>', lambda e: self.topic15tab1Canvas.configure(scrollregion=self.topic15tab1Canvas.bbox('all')))

        # #create another frame inside the canvas
        # self.topic15tab1secondFrame = Frame(self.topic15tab1Canvas)

        # #add the new frame to a window in the canvas
        # self.topic15tab1Canvas.create_window((0,0), window=self.topic15tab1secondFrame, anchor='nw')
        
        #TAB 2
        Label(self.topic15tab2, text='Simple Calculator Application').grid(row=0, column=0, columnspan=7)

        #create text widget to display code snippet
        self.topic15TxtWidget = Text(self.topic15tab2,
                                        font=('Helvetica', '10'),
                                        state='normal')
        self.topic15TxtWidget.grid(row=1, column=0, sticky='nsew')


        with open('topic15_snippet.txt') as topic15:
            self.topic15snipTxt = topic15.read()
            # print(self.topic0snipTxt)
        

        self.topic15TxtWidget.insert(END, self.topic15snipTxt)
        self.topic15TxtWidget.config(state='disabled', height=11, width=68, wrap='word')

        # self.topic15tab2RunBtn = Button(self.topic15tab2,
        #                                 text='Run code snippet',
        #                                 command=lambda: self.run_snippet('Topic 15'))
        # self.topic15tab2RunBtn.grid(row=2, column=0, sticky='nsew')


    #create a function that can display hyperlinks and redirects user to youtube tkinter tutorials



    #create function to run separate py files tkinter
    def run_snippet(self, topic):
        if topic == 'Topic 0':
            topic0_snip.run()
        elif topic == 'Topic 1':
            topic1_snip.run()
        elif topic == 'Topic 2':
            topic2_snip.run()
        elif topic == 'Topic 3':
            topic3_snip.run()
        elif topic == 'Topic 4':
            topic4_snip.run()
        elif topic == 'Topic 5':
            topic5_snip.run()
        elif topic == 'Topic 6':
            topic6_snip.run()
        elif topic == 'Topic 7':
            topic7_snip.run()
        elif topic == 'Topic 8':
            topic8_snip.run()
        elif topic == 'Topic 9':
            topic9_snip.run()
        elif topic == 'Topic 10':
            topic10_snip.run()
        elif topic == 'Topic 11':
            topic11_snip.run()
        elif topic == 'Topic 12':
            topic12_snip.run()

        #walay snippet sa topic 13 FILE I/O 

        elif topic == 'Topic 14':
            topic14_snip.run()
        elif topic == 'Topic 15':
            topic15_snip.run()

        else:
            print('None')






def main():
    main = Tk()
    tukinter = Application(main)
    main.mainloop()


if __name__ == '__main__':
    main()
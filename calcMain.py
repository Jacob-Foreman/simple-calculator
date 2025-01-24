from tkinter import *
from tkinter import ttk

"""
Author Jacob Foreman
Date 1/23/25

Description: A basic calculator using the tkinter library to create the widgets
This calculator will have a total of 24 buttons
"""
#Both Display and Button frames are withing mainframe
class calcMainUI:

    def __init__(self, root):
        root.title("Calculator")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.mainframe = ttk.Frame(root)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0,weight=1)
        self.mainframe.rowconfigure(0,weight=0)
        self.mainframe.rowconfigure(1,weight=1)

        #Display Frame
        self.displayframe = ttk.Frame(self.mainframe)
        self.displayframe.grid(column=0,row=0, sticky=(N,W,E))
        self.displayframe.columnconfigure(0, weight=1)
        self.displayframe.rowconfigure(0,weight=0)

        self.calc_io_label = ttk.Label(self.displayframe, text = "0",width=21, anchor="e",font=("Courier",20),relief="groove")
        self.calc_io_label.grid(column=0,row=0, sticky=(W,E))
        


        #Button Frame
        self.buttonFrame = ttk.Frame(self.mainframe)
        self.buttonFrame.grid(column=0, row=1, sticky=(N,W,E))
        self.buttonFrame.columnconfigure(0,weight=1)
        self.buttonFrame.rowconfigure(0,weight=1)
        #6X4 Grid
        for i in range(6):
            for j in range(4):
                self.buttonFrame.rowconfigure(i,weight=1)
                self.buttonFrame.columnconfigure(j,weight=1)


        self.percentile_button = ttk.Button(self.buttonFrame,text="%")
        self.percentile_button.grid(column=0,row=0,padx=2,pady=2,sticky=(N,S,W,E))

        self.clear_entry_button = ttk.Button(self.buttonFrame,text="CE")
        self.clear_entry_button.grid(column=1,row=0,padx=2,pady=2,sticky=(N,S,W,E))

        self.clear_button = ttk.Button(self.buttonFrame,text="C")
        self.clear_button.grid(column=2,row=0,padx=2,pady=2,sticky=(N,S,W,E))

        self.delete_button = ttk.Button(self.buttonFrame,text="Del")
        self.delete_button.grid(column=3,row=0,padx=2,pady=2,sticky=(N,S,W,E))










       
       

       
        
   

root = Tk()
root.geometry("350x500")
root.minsize(width=350,height=500)
calcMainUI(root)
root.mainloop()

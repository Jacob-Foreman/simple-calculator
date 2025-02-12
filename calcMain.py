from tkinter import *
from tkinter import ttk
from functions import *

"""
Author Jacob Foreman
Date 1/23/25

Description: A basic calculator using the tkinter library to create the widgets
This calculator will have a total of 24 buttons
"""

root = Tk()


#Both Display and Button frames are withing mainframe
class calcMainUI:

    def __init__(self, root):   
        self.root = root
        root.title("Calculator")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.mainframe = ttk.Frame(root)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0,weight=1)
        self.mainframe.rowconfigure(0,weight=0)
        self.mainframe.rowconfigure(1,weight=1)

        #Display Frame
        self.displayframe = ttk.Frame(self.mainframe, style='sleek.TFrame')
        self.displayframe.grid(column=0,row=0, sticky=(N,W,E))
        self.displayframe.columnconfigure(0, weight=1)
        self.displayframe.rowconfigure(0,weight=0)

        self.calc_io_label = ttk.Label(self.displayframe, text = "0",width=21, anchor="e",font=("Courier",20),relief="groove")
        self.calc_io_label.grid(column=0,row=0, sticky=(W,E))
        


        #Button Frame
        self.buttonFrame = ttk.Frame(self.mainframe, style='sleek.TFrame')
        self.buttonFrame.grid(column=0, row=1, sticky=(N,S,W,E))
        self.buttonFrame.columnconfigure(0,weight=1)
        self.buttonFrame.rowconfigure(0,weight=1)
        #6X4 Grid

        #resize grid when window is expanded
        for i in range(6):
            for j in range(4):
                self.buttonFrame.rowconfigure(i,weight=1)
                self.buttonFrame.columnconfigure(j,weight=1)

        #row 1
        self.clear_entry_button = Button(self.buttonFrame,text="CE",bg="#C0C0C0",fg="Black",command = lambda : clearAll(self))
        self.clear_entry_button.grid(column=0,row=0,padx=1,pady=1,sticky=(N,S,W,E))

        self.left_parentheses_button = Button(self.buttonFrame,text="(",bg="#C0C0C0",fg="Black",command =lambda : addSymbol(self,"("))
        self.left_parentheses_button.grid(column=1,row=0,padx=1,pady=1,sticky=(N,S,W,E))

        self.right_parentheses_button = Button(self.buttonFrame,text=")",bg="#C0C0C0",fg="Black",command = lambda : addSymbol(self,")"))
        self.right_parentheses_button.grid(column=2,row=0,padx=1,pady=1,sticky=(N,S,W,E))

        self.delete_button = Button(self.buttonFrame,text="Del",bg="#C0C0C0",fg="Black",command = lambda : clearEntry(self))
        self.delete_button.grid(column=3,row=0,padx=1,pady=1,sticky=(N,S,W,E))


        #row 2
        self.reciprocal_button = Button(self.buttonFrame,text="1/x",bg="#C0C0C0",fg="Black",command=lambda: fractional(self,self.calc_io_label.cget("text")))
        self.reciprocal_button.grid(column=0,row=1,padx=1,pady=1,sticky=(N,S,W,E))

        self.squared_button = Button(self.buttonFrame,text="x^2",bg="#C0C0C0",fg="Black",command=lambda: squared(self,self.calc_io_label.cget("text")))
        self.squared_button.grid(column=1,row=1,padx=1,pady=1,sticky=(N,S,W,E))

        self.square_root_button = Button(self.buttonFrame,text="√x",bg="#C0C0C0",fg="Black",command=lambda: squareRoot(self, self.calc_io_label.cget("text")))
        self.square_root_button.grid(column=2,row=1,padx=1,pady=1,sticky=(N,S,W,E))

        self.division_button = Button(self.buttonFrame,text="/",bg="#C0C0C0",fg="Black",command= lambda : addSymbol(self,"/"))
        self.division_button.grid(column=3,row=1,padx=1,pady=1,sticky=(N,S,W,E))

        
        #row 3
        self.seven_button = Button(self.buttonFrame,text="7",bg="#C0C0C0",fg="Black",command=lambda: appendDigit(self,7))
        self.seven_button.grid(column=0,row=2,padx=1,pady=1,sticky=(N,S,W,E))

        self.eight_button = Button(self.buttonFrame,text="8",bg="#C0C0C0",fg="Black",command=lambda: appendDigit(self,8))
        self.eight_button.grid(column=1,row=2,padx=1,pady=1,sticky=(N,S,W,E))

        self.nine_button = Button(self.buttonFrame,text="9",bg="#C0C0C0",fg="Black",command=lambda: appendDigit(self,9))
        self.nine_button.grid(column=2,row=2,padx=1,pady=1,sticky=(N,S,W,E))

        self.multiply_button = Button(self.buttonFrame,text="x",bg="#C0C0C0",fg="Black",command= lambda : addSymbol(self,"x"))
        self.multiply_button.grid(column=3,row=2,padx=1,pady=1,sticky=(N,S,W,E))


        #row 4
        self.four_button = Button(self.buttonFrame,text="4",bg="#C0C0C0",fg="Black",command=lambda: appendDigit(self,4))
        self.four_button.grid(column=0,row=3,padx=1,pady=1,sticky=(N,S,W,E))

        self.five_button = Button(self.buttonFrame,text="5",bg="#C0C0C0",fg="Black",command=lambda: appendDigit(self,5))
        self.five_button.grid(column=1,row=3,padx=1,pady=1,sticky=(N,S,W,E))

        self.six_button = Button(self.buttonFrame,text="6",bg="#C0C0C0",fg="Black",command=lambda: appendDigit(self,6))
        self.six_button.grid(column=2,row=3,padx=1,pady=1,sticky=(N,S,W,E))

        self.minus_button = Button(self.buttonFrame,text="-",bg="#C0C0C0",fg="Black",command= lambda : addSymbol(self, "-"))
        self.minus_button.grid(column=3,row=3,padx=1,pady=1,sticky=(N,S,W,E))


        #row 5
        self.one_button = Button(self.buttonFrame,text="1",bg="#C0C0C0",fg="Black",command=lambda: appendDigit(self,1))
        self.one_button.grid(column=0,row=4,padx=1,pady=1,sticky=(N,S,W,E))

        self.two_button = Button(self.buttonFrame,text="2",bg="#C0C0C0",fg="Black",command=lambda: appendDigit(self,2))
        self.two_button.grid(column=1,row=4,padx=1,pady=1,sticky=(N,S,W,E))

        self.three_button = Button(self.buttonFrame,text="3",bg="#C0C0C0",fg="Black",command=lambda: appendDigit(self,3))
        self.three_button.grid(column=2,row=4,padx=1,pady=1,sticky=(N,S,W,E))

        self.plus_button = Button(self.buttonFrame,text="+",bg="#C0C0C0",fg="Black",command= lambda: addSymbol(self, "+"))
        self.plus_button.grid(column=3,row=4,padx=1,pady=1,sticky=(N,S,W,E))


        #row 6
        self.sign_button = Button(self.buttonFrame,text="+/-",bg="#C0C0C0",fg="Black",command=signSwitch)
        self.sign_button.grid(column=0,row=5,padx=1,pady=1,sticky=(N,S,W,E))

        self.zero_button = Button(self.buttonFrame,text="0",bg="#C0C0C0",fg="Black",command=lambda: appendDigit(self,0))
        self.zero_button.grid(column=1,row=5,padx=1,pady=1,sticky=(N,S,W,E))

        self.decimal_button = Button(self.buttonFrame,text=".",bg="#C0C0C0",fg="Black",command=lambda: addSymbol(self,"."))
        self.decimal_button.grid(column=2,row=5,padx=1,pady=1,sticky=(N,S,W,E))

        self.equals_button = Button(self.buttonFrame,text="=",bg="#C0C0C0",fg="Black",command=lambda: equals(self, self.calc_io_label.cget("text")))
        self.equals_button.grid(column=3,row=5,padx=1,pady=1,sticky=(N,S,W,E))


        self.root.bind("<Key>",self.on_key_press)#binds keys to the window

    def on_key_press(self,event):
        if event.keysym == "1":
            appendDigit(self,'1')
        if event.keysym =="KP_1":
            appendDigit(self,'1')

        if event.keysym == "2":
            appendDigit(self,'2')
        if event.keysym =="KP_2":
            appendDigit(self,'2')

        if event.keysym == "3":
            appendDigit(self,'3')
        if event.keysym =="KP_3":
            appendDigit(self,'3')

        if event.keysym == "4":
            appendDigit(self,'4')
        if event.keysym =="KP_4":
            appendDigit(self,'4')

        if event.keysym == "5":
            appendDigit(self,'5')
        if event.keysym =="KP_5":
            appendDigit(self,'5')

        if event.keysym == "6":
            appendDigit(self,'6')
        if event.keysym =="KP_6":
            appendDigit(self,'6')

        if event.keysym == "7":
            appendDigit(self,'7')
        if event.keysym =="KP_7":
            appendDigit(self,'7')

        if event.keysym == "8":
            appendDigit(self,'8')
        if event.keysym =="KP_8":
            appendDigit(self,'8')

        if event.keysym == "9":
            appendDigit(self,'9')
        if event.keysym =="KP_9":
            appendDigit(self,'9')

        if event.keysym == "0":
            appendDigit(self,'0')
        if event.keysym =="KP_0":
            appendDigit(self,'0')
        
        if event.keysym == "plus":
            addSymbol(self,'+')
        if event.keysym =="KP_Add":
            addSymbol(self,'+')
        
        if event.keysym == "minus":
            addSymbol(self,"-")
        if event.keysym == "KP_Subtract":
            addSymbol(self, "-")
        
        if event.keysym =="equal":
            equals(self,self.calc_io_label.cget("text"))
        if event.keysym =="Return":
            equals(self,self.calc_io_label.cget("text"))
        if event.keysym =="KP_Enter":
            equals(self,self.calc_io_label.cget("text"))
        
        if event.keysym == "asterisk":
            addSymbol(self,"x")
        if event.keysym == "KP_Multiply":
            addSymbol(self,"x")

        if event.keysym == "slash":
            addSymbol(self,"/")
        if event.keysym == "KP_Divide":
            addSymbol(self,"/")

        if event.keysym == "period":
            addSymbol(self,".")
        if event.keysym == "KP_Decimal":
            addSymbol(self,".")
        
        if event.keysym == "BackSpace":
            clearEntry(self)
            
        

sleek_Frame_Style = ttk.Style()
sleek_Frame_Style.configure("sleek.TFrame",background="Black")     
root.geometry("350x200")
root.minsize(width=350,height=200)
calcMainUI(root)
root.mainloop()

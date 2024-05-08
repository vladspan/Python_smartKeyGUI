from tkinter import *


class Tipkovnica(LabelFrame):
    def __init__(self, parent, text):
        LabelFrame.__init__(self, parent, text = text)
        self.entryPIN = Entry(self, width=25, borderwidth=3)
        self.entryPIN.grid(row=0, column=0, columnspan=3, padx=20, pady=10)
        self.button0 = Button(self, text='0',bg="yellow", command=lambda: self.button_add(0))
        #ßbutton0.configure(bg="yellow",fg="#131414")
        button1 = Button(self, text='1' ,command=lambda: self.button_add(1))
        button2 = Button(self, text='2', command=lambda: self.button_add(2))
        button3 = Button(self, text='3', command=lambda: self.button_add(3))
        button4 = Button(self, text='4', command=lambda: self.button_add(4))
        button5 = Button(self, text='5', command=lambda: self.button_add(5))
        button6 = Button(self, text='6', command=lambda: self.button_add(6))
        button7 = Button(self, text='7', command=lambda: self.button_add(7))
        button8 = Button(self, text='8', command=lambda: self.button_add(8))
        button9 = Button(self, text='9', command=lambda: self.button_add(9))
        buttonC = Button(self, text='C', command=self.clear)
        buttonE = Button(self, text='E', command= lambda: self.entry())

        button1.grid(row=1, column=0, padx=5, pady=5, ipadx=20, ipady=20)
        button2.grid(row=1, column=1, padx=5, pady=5, ipadx=20, ipady=20)
        button3.grid(row=1, column=2, padx=5, pady=5, ipadx=20, ipady=20)
        button4.grid(row=2, column=0, padx=5, pady=5, ipadx=20, ipady=20)
        button5.grid(row=2, column=1, padx=5, pady=5, ipadx=20, ipady=20)
        button6.grid(row=2, column=2, padx=5, pady=5, ipadx=20, ipady=20)
        button7.grid(row=3, column=0, padx=5, pady=5, ipadx=20, ipady=20)
        button8.grid(row=3, column=1, padx=5, pady=5, ipadx=20, ipady=20)
        button9.grid(row=3, column=2, padx=5, pady=5, ipadx=20, ipady=20)
        self.button0.grid(row=4, column=1, padx=5, pady=5, ipadx=20, ipady=20)
        buttonC.grid(row=4, column=0, padx=5, pady=5, ipadx=20, ipady=20)
        buttonE.grid(row=4, column=2, padx=5, pady=5, ipadx=20, ipady=20)

    def button_add(self, number):
        curr = self.entryPIN.get()
        self.entryPIN.delete(0, END)
        self.entryPIN.insert(0, curr+str(number))

    def clear(self):
        self.entryPIN.delete(0, END)    

    def entry(self):
        return self.entryPIN.get()
        




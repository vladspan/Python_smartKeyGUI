from tkinter import*
from admin import *


class Izmjena(LabelFrame):
    def __init__(self, parent, text):
        LabelFrame.__init__(self, parent, text=text)

        self.nazivAdminIme = Label(self, text='Admin username')
        self.nazivAdminIme.grid(row=1, column=0)
        self.unosAdminIme = Entry(self, width=25, borderwidth=3)
        self.unosAdminIme.grid(row=2, column=0)

        self.nazivAdminSifra = Label(self, text='Admin sifra')
        self.nazivAdminSifra.grid(row=1, column=1)
        self.unosAdminSifra = Entry(self, width=25, borderwidth=3)
        self.unosAdminSifra.grid(row=2, column=1)

        self.aktivacijaPravaButton = Button(self, text='Admin login', command=self.aktivacijaPrava)
        self.aktivacijaPravaButton.grid(row=3, columnspan=2)

    
    def aktivacijaPrava(self):
        if self.unosAdminIme.get() == 'admin' and self.unosAdminSifra.get() == '1234':
            adminProzor = Tk()

            self.a = AdminLogin(adminProzor, text='Admin postavke')
            self.a.grid(row=0, column=0)

            adminProzor.mainloop() 
        else:
            self.falseLogin = Label(self, text='Pogrešan unos!')
            self.falseLogin.grid(row=4, columnspan=2)
            self.after(3000, lambda: self.falseLogin.config(text=''))
            self.after(1000, lambda: self.clearEntryAdmin())      

    def clearEntryAdmin(self):
        self.unosAdminIme.delete(0, END)
        self.unosAdminSifra.delete(0, END)
    


if __name__ == '__main__':
    h = Tk()
    a = Frame(h)
    a.grid(rowspan=3, columnspan=3)
    test = Izmjena(a, 'miro')
    test.grid(row=1, column=1)
    h.mainloop()


    

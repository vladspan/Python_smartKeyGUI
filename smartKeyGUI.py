from tkinter import*
from tipkovnica import*
from izmjenaKorisnika import*
import sqlite3

class SmartKey():
    def __init__(self):
        self.smartkey = Tk()

        self.baza = Frame(self.smartkey)
        self.baza.grid(row=0, column=0, rowspan=4, columnspan=4)

        self.vanjski_okivr = LabelFrame(self.baza, text='SmartKey')
        self.vanjski_okivr.grid(row=0, column=0, rowspan=4, columnspan=4)

        self.tip = Tipkovnica(self.vanjski_okivr,'Unos šifre')
        self.tip.grid(row=0, column=0)

        potvrdniButton = Button(self.vanjski_okivr, text='Potvdi ulaz', command=self.provjeraSifra)
        potvrdniButton.grid(row=1, column=0, ipadx=30, ipady=30, padx=5)

        clearButton = Button(self.vanjski_okivr, text='C', command=self.ocistiEkran)
        clearButton.grid(row=2, column=0, ipadx=30, ipady=30, padx=5)

        self.obavijest = Label(self.vanjski_okivr, text ='')
        self.obavijest.grid(row=3, column=0)

        self.opcijeButton = Button(self.vanjski_okivr, text= 'Postavke', command= self.adminPostavke)
        self.opcijeButton.grid(row=4, column=0)

        self.smartkey.mainloop()

    def provjeraSifra(self):
        self.uneseniKod = self.tip.entry()
        self.query_select_all = '''SELECT * FROM Korisnici'''
        self.database = 'Baza_korisnika.db'

        try:
            self.connection = sqlite3.connect(self.database)
            self.cursor = self.connection.cursor()

            self.cursor.execute(self.query_select_all)
            self.podaci = self.cursor.fetchall()

            self.connection.commit()
            self.cursor.close()

            self.is_logged_in = False
            ime = ''

            for podatak in self.podaci:
                if self.uneseniKod == podatak[3]:
                    self.is_logged_in = True
                    ime = podatak[1]
                    break

            if self.is_logged_in:      
                self.obavijest_text = f'Uspješan login.\nDobrodošao {ime}'
                self.obavijest.config(text=self.obavijest_text)
                self.smartkey.after(3000, lambda: self.obavijest.config(text=''))

            else:
                self.obavijest_text = 'Šifra je kriva. Pokušajte ponovo.'
                self.obavijest.config(text=self.obavijest_text)
                self.smartkey.after(3000, lambda: self.obavijest.config(text=''))
                                           
        except sqlite3.Error as e:
            print('Greška pri spajanju na bazu', e)
        
        finally:
            self.connection.close()
    
    def ocistiEkran(self):
        self.tip.clear()
        self.obavijest.config(text='')

    def adminPostavke(self):
        h = Tk()
        a = Frame(h)
        a.grid(rowspan=3, columnspan=3)
        test = Izmjena(a, 'Admin postavke')
        test.grid(row=1, column=1)
        h.mainloop()
           
if __name__ == '__main__':
    SmartKey()
    

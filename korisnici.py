from tkinter import *
from tipkovnica import*
import sqlite3
from izmjenaKorisnika import*


class Korisnici(LabelFrame):
    def __init__(self, parent, text):
        LabelFrame.__init__(self, parent, text= text)

        oznakaIme = Label(self, text='Ime')
        oznakaIme.grid(row=0, column=0)
        self.ime = Entry(self, borderwidth=2)
        self.ime.grid(row=1, column=0)

        oznakaPrezime = Label(self,text='Prezime')
        oznakaPrezime.grid(row=0, column=1)
        self.prezime = Entry(self, borderwidth=2)
        self.prezime.grid(row=1, column=1)

        oznakaSifra = Label(self,text='Šifra')
        oznakaSifra.grid(row=0, column=2)
        self.sifra = Entry(self, borderwidth=2 )
        self.sifra.grid(row=1, column=2)

        buttonDodajUbazu = Button(self, text='Dodaj novog korisnika', command=self.unosKorisnika)
        buttonDodajUbazu.grid(row=2, columnspan=3)

        '''
        buttonOcistiUnos= Button(self, text='Izmjeni podatke', command=self.izmjenaPodataka)
        buttonOcistiUnos.grid(row=2, column=1)
        '''

        self.database = 'Baza_korisnika.db'
    
    def unosKorisnika(self): 

        self.query_create = '''CREATE TABLE IF NOT EXISTS Korisnici (
                        id INTEGER PRIMARY KEY,
                        ime TEXT,
                        prezime TEXT,
                        sifra TEXT)'''
                    
        try:
            self.connection = sqlite3.connect(self.database)
            self.cursor = self.connection.cursor()
            self.cursor.execute(self.query_create)
            self.connection.commit()
            self.cursor.close()
          

        except sqlite3.Error as e:
            print('Greška pri spajanju na bazu', e)
        
        finally:
            self.connection.close()

        self.query_insert = ''' INSERT INTO Korisnici
                            (ime, prezime, sifra)
                            VALUES(?, ?, ?)'''
          
        try:
            self.connection = sqlite3.connect(self.database)
            self.cursor = self.connection.cursor()
            if self.ime.get() !='' and self.prezime.get() !='' and self.sifra.get() !='':
                
                self.cursor.execute(self.query_insert, (self.ime.get(), self.prezime.get(), self.sifra.get()))
                erroUpis = Label(self, text= 'Korisnik uspješno unesen!')
                erroUpis.grid(row=3, column=1)
                self.after(3000, lambda: erroUpis.config(text=''))
                self.after(1000, self.celarEntry())

            else:
                erroUpis = Label(self, text= 'Niste ispavno unijeli korisnika. Pokušajte ponovo.')
                erroUpis.grid(row=3, column=1)
                self.after(3000, lambda: erroUpis.config(text=''))
                self.after(1000, self.celarEntry())
               
            
            self.connection.commit()
            self.cursor.close()

        except sqlite3.Error as e:
            print('Greška pri spajanju na bazu', e)

        finally:
            self.connection.close()
    

    def izmjenaPodataka(self):
        self.izmjena = Tk()
        self.izmjena.grid(row=0, column=0)
        #self.izmjena.geometry('600x400')

       
        self.query_update_sifraPrezime = '''UPDATE Korisnici
                            SET prezime=?
                            WHERE sifra=?
                            '''
        
        self.okvirIzmjena = Frame(self.izmjena)
        self.okvirIzmjena.grid(row=0, column=0, rowspan=3, columnspan=3)

        self.oznakaIzmjena = LabelFrame(self.okvirIzmjena, text='Korisničke postavke')
        self.oznakaIzmjena.grid(row=0, column=0, rowspan=3, columnspan=3)

        self.odabirIzmeneNaziv = Label(self.okvirIzmjena, text='Admin ')

        self.klasaIzmjena = Izmjena(self.oznakaIzmjena, 'Promjena korisničkih podataka')
        self.klasaIzmjena.grid(row=0, column=0, rowspan=3, columnspan=3)

        self.izmjena.mainloop()
        
    def celarEntry(self):
        self.ime.delete(0, END)
        self.prezime.delete(0, END)
        self.sifra.delete(0, END)
    

            
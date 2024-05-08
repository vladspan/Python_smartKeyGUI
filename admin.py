from tkinter import*
from korisnici import*
from sqlite3 import*

class AdminLogin(LabelFrame):
    def __init__(self, parent, text):
        LabelFrame.__init__(self, parent, text = text)

        okvirDodajNovog = Frame(self)
        okvirDodajNovog.grid(row=0, column=0)

        self.klasaDodajNovog = Korisnici(okvirDodajNovog, 'Dodaj novog korisnika')
        self.klasaDodajNovog.grid(row=0, column=0)

        #dodaj razmak
        okvirSifra = LabelFrame(self, tex= 'Promjena šifre prema imenu')
        okvirSifra.grid(row=1, column=0, rowspan=2, columnspan=3)

        self.nazivIme = Label(okvirSifra, text='Unesi ime')
        self.nazivIme.grid(row=0, column=0, columnspan=1)

        self.unosIme = Entry(okvirSifra, width=25, borderwidth=3)
        self.unosIme.grid(row=1, column=0, columnspan=1)

        self.nazivSifra = Label(okvirSifra, text='Unesi novu šifru')
        self.nazivSifra.grid(row=0, column=1, columnspan=1)

        self.unosSifra = Entry(okvirSifra, width=25, borderwidth=3)
        self.unosSifra.grid(row=1, column=1, columnspan=1,)

        self.unosPromjeneSifre = Button(okvirSifra, text= 'Ažuriraj', command=self.promjenaSifre)
        self.unosPromjeneSifre.grid(row=2, columnspan=2)

        okvirPrezime = LabelFrame(self, tex= 'Promjena prezimena prema imenu')
        okvirPrezime.grid(row=4, column=0, rowspan=2, columnspan=3)

        self.nazivImena = Label(okvirPrezime, text='Unesi ime')
        self.nazivImena.grid(row=0, column=0, columnspan=1)

        self.unosImena = Entry(okvirPrezime, width=25, borderwidth=3)
        self.unosImena.grid(row=1, column=0, columnspan=1)

        self.nazivPrezime = Label(okvirPrezime, text='Unesi novo prezime')
        self.nazivPrezime.grid(row=0, column=1, columnspan=1)

        self.unosPrezime = Entry(okvirPrezime, width=25, borderwidth=3)
        self.unosPrezime.grid(row=1, column=1, columnspan=1,)

        self.unosPromjenePrezimena = Button(okvirPrezime, text= 'Ažuriraj', command=self.promjenaPrezimena)
        self.unosPromjenePrezimena.grid(row=2, columnspan=2)

        self.okvirLista = LabelFrame(self, text='Lista korisnika')
        self.okvirLista.grid(row=6, columnspan=4)

        self.listaKorisnik = Label(self.okvirLista, text='Ispiši listu korisnika')
        self.listaKorisnik.grid(row=1, column=0)

        self.gumbListaKorisnika = Button(self.okvirLista, text='Ispis liste korisnika', command=self.listaKorisnika)
        self.gumbListaKorisnika.grid(row=2, column=0)

        self.listbox = Listbox(self.okvirLista)
        self.listbox.grid(row=3, columnspan=4)
        '''
        scrollbar = Scrollbar(self.okvirLista, orient=VERTICAL, command=self.listbox.yview)
        scrollbar.grid(row=3, column=4, sticky='ns')
        self.listbox.config(yscrollcommand=scrollbar.set)
        '''

    def promjenaSifre(self):
        self.query_update_sifra = '''UPDATE Korisnici
                                      SET sifra=?
                                      WHERE ime=?
                                   '''
        self.database = 'Baza_korisnika.db'

        try:
            self.connection = sqlite3.connect(self.database)
            self.cursor = self.connection.cursor()
            self.cursor.execute(self.query_update_sifra, (self.unosSifra.get(), self.unosIme.get()))
            self.connection.commit()
            self.cursor.close()

        except sqlite3.Error as e:
            print('Greška pri radu s bazom:', e)

        finally:
            self.connection.close()


    def promjenaPrezimena(self):
        self.query_update_prezime = '''UPDATE Korisnici
                                       SET prezime=?
                                       WHERE ime=?
                                    '''
        self.database = 'Baza_korisnika.db'

        try:
            self.connection = sqlite3.connect(self.database)
            self.cursor = self.connection.cursor()
            self.cursor.execute(self.query_update_prezime, (self.unosPrezime.get(), self.unosImena.get()))
            self.connection.commit()
            self.cursor.close()

        except sqlite3.Error as e:
            print('Greška pri radu s bazom:', e)

        finally:
            self.connection.close()
    
    def listaKorisnika(self):
        self.query_select_all = 'SELECT * From Korisnici'
        self.database = 'Baza_korisnika.db'

        try: 
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()

            cursor.execute(self.query_select_all)
            podaciBaze = cursor.fetchall()

            connection.commit()

            self.listbox.delete(0, END)

            for ispis in podaciBaze:
                self.listbox.insert(END, f'ID:{ispis[0]} Ime:{ispis[1]} Prezime:{ispis[2]} Šifra:{ispis[3]}')

            '''
            x=0
            for ispis in podaciBaze:
                ispisOzanka = Label(self.okvirLista, text=f'ID: {ispis[0]}, IME: {ispis[1]}, PREZIME: {ispis[2]}, ŠIFRA: {ispis[3]}\n')
                ispisOzanka.grid(row=x, column=0)
                x+=1
            '''

            cursor.close()

        except sqlite3.Error as e:
            print('Greška pri spajanju', e)

        finally:
            connection.close()


      
         
if __name__ == '__main__':
    w = Tk()
    adminBaza = Frame(w)
    adminBaza.grid(rowspan=3, columnspan=6)
    test = AdminLogin(adminBaza, 'test')
    test.grid(row=0, column=0)
    w.mainloop()





       





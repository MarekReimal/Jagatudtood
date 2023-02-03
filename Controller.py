import os
from tkinter import INSERT, messagebox, END, filedialog

from Model import Model
from View import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self, self.model)  # kaasa controller ja model
        self.absolute_path = os.path.dirname(__file__)  # loeb asukoha kus asub projekti fail
        self.is_btn = None  # muutuja mis nuppu vajutati

    def click_btn_students(self):
        """
        Kui vajutad nupule Õpilased
        """
        # Tühjenda teksbox enne andmete lisamist
        self.view.tbx_students.delete('1.0', END)
        # Ava fail
        self.model.open_file()
        # Kontroll kas fail valiti, kui valiti siis täidab tekstboxi
        if self.model.file_path:
            # Loo list õpilaste nimedega
            self.is_btn = 'stn'  # muutuja kaasa mis nupp
            self.model.read_file(self.is_btn)  # loeb faili sisu listi
            # Kirjuta õpilaste nimed vormile tbx_students
            for line in self.model.students:  # kirjutab listi sisu tekstboxi
                self.view.tbx_students.insert(INSERT, line + '\n')  # Kirjutab teksboxi
        else:  # kui faili ei valitud siis annab teate
            messagebox.showinfo("Teavitus", "Õpilaste faili ei valitud")

    def click_btn_tasks(self):
        """
        Kui vajutad nupule tasks
        """
        # Tühjenda teksbox enne andmete lisamist
        self.view.tbx_tasks.delete('1.0', END)
        # Ava fail
        self.model.open_file()
        # Kontroll kas fail valiti, kui valiti siis täidab tekstboxi
        if self.model.file_path:
            # Loo list õpilaste nimedega
            self.is_btn = 'tsk'  # muutuja kaasa, mis nupp
            self.model.read_file(self.is_btn)  # loeb faili sisu
            # Kirjuta õpilaste nimed vormile tbx_students
            for line in self.model.tasks:  # kirjutab faili sisu tekstboxi
                self.view.tbx_tasks.insert(INSERT, line + '\n')  # Kirjutab teksboxi
        else:  # kui faili ei valitud siis annab teate
            messagebox.showinfo('Teavitus', 'Ülesannete faili ei valitud')

    def click_btn_mix_tasks(self):
        """
        Kui vajutad nupule Jaga ülesanded
        """
        # Tühjenda teksbox enne andmete lisamist
        self.view.tbx_mixedtasks.delete('1.0', END)

        # Kontroll, kas ülesandeid jätkub kõigile õpilastele
        self.model.set_tasks()  # kontroll kas ülesandeid on piisavalt kõigile õpilastele
        if self.model.is_tasks:  # kui ülesandeid jätkub siis
            self.model.mix_tasks_for_students()  # jagab ülesanded õpilastele
            for line in self.model.students_tasks:
                self.view.tbx_mixedtasks.insert(INSERT, line + '\n')  # Kirjutab textboksi õpilased ja nende ül.
        else:  # kui ülesandeid ei jätku kõigile õpilastele, siis
            # teavita kasutajat et ülesandeid on vähem
            messagebox.showinfo('Teavitus', 'Ülesandeid ei jätku kõigile')

    def click_btn_save(self):
        # hea selgitus save as : https://www.plus2net.com/python/tkinter-filedialog-asksaveasfile.php
        # Save AS dialoog
        f = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=[('AllFiles', '*.*'),
                                                                                   ('txt file', '*.txt'),
                                                                                   ('csv file', '*.csv')],
                                     initialdir=self.absolute_path, title='Salvesta ülesannetete fail')
        if f:  # kui failinimi on olemas siis
            tasks_save = str(self.view.tbx_mixedtasks.get(1.0, END))  # võtab tekstboksi sisu muutujasse
            f.write(tasks_save)  # kirjutab faili sisse
            f.close()  # sulgeb faili
        else:  # kui failinime ei ole siis teade
            messagebox.showinfo('Teavitus', 'Faili ei salvestatud')

    def main(self):
        """
        Käivitab GUI
        :return:
        """
        self.view.main()

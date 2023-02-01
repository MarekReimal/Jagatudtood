from tkinter import INSERT, messagebox

from Model import Model
from View import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self, self.model) # kaasa controller ja model

    def click_btn_students(self):
        """
        Kui vajutad nupule Õpilased
        """
        # Ava fail
        self.model.open_students_file()
        # Loo list õpilaste nimedega
        self.model.read_students_file()
        # Kirjuta õpilaste nimed vormile tbx_students
        for line in self.model.students:
            self.view.tbx_students.insert(INSERT, line + '\n')  # Kirjutab teksboxi

    def click_btn_tasks(self):
        """
        Kui vajutad nupule tasks
        """
        # Ava fail
        self.model.open_tasks_file()
        # Loo list õpilaste nimedega
        self.model.read_tasks_file()
        # Kirjuta õpilaste nimed vormile tbx_students
        for line in self.model.tasks:
            self.view.tbx_tasks.insert(INSERT, line + '\n')  # Kirjutab teksboxi

    def click_btn_mix_tasks(self):
        """
        Kui vajutad nupule Jaga ülesanded
        """
        # Kontroll, kas ülesandeid jätkub kõigile õpilastele
        self.model.set_tasks()
        if self.model.is_tasks:
            print('hstssth')
            self.model.mix_tasks_for_students()

            # TODO õpilase nimi + töö andmed ei lähe tekstboksi

        else:  # kui ülesandeid ei jätku kõigile õpilastele, siis
                # teavita kasutajat et ülesandeid on vähem
                messagebox.showinfo("showinfo", "Information")



    def main(self):
        self.view.main()
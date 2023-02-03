import random
from tkinter import filedialog


class Model:

    def __init__(self):
        self.file_path = None
        self.longest_name = 0  # kõige pikem nimi, andmete joondamiseks vaja
        self.students_tasks = []  # õpilased ja neile jagatud ülesanded
        self.students = []  # õpilased
        self.tasks = []  # ülesanded
        self.is_tasks = False  # True kui ülesandeid jätkub kõigile õpilastele

    def open_file(self):
        """
        kuvab dialoogi faili avamiseks
        :return:
        """
        # küsib faili avamist > väljund on faili kaloogi tee
        self.file_path = filedialog.askopenfilename()


    def read_file(self, is_btn):  # is_btn on stn või tsk
        self.longest_name = 0  # pikim nimi 0

        # valik kumb list tühjaks teha
        if is_btn == 'stn':  # vajutati õpilaste nuppu
            self.students = []  # list tühjaks
        elif is_btn == 'tsk':  # vajutati ül. nuppu
            self.tasks = []  # list tühjaks

        f = open(self.file_path, "r", encoding="utf-8")  # Avab faili lugemiseks
        for line in f:  # Loeb ridu failist ükshaaval
            line = line.strip()  # Lõikab rea küljest ära /n
            if is_btn == 'stn':  # vajutati õpilaste nuppu
                self.students.append(line)  # Kirjutab õpilaste nimed listi
                if len(line) > self.longest_name:  # võrdleb nimepikkust, kui on suurem siis
                    self.longest_name = len(line)  # kirjutab mällu pikema nime tähtede arvu
            elif is_btn == 'tsk':  # vajutati ül. nuppu
                self.tasks.append(line)  # Kirjutab tööde nimed listi
        f.close()  # sulgeb faili


    def mix_tasks_for_students(self):
        """
        Jagab ülesanded õpilastele
        :return:
        """
        self.students_tasks = []  # list tühjaks
        random.shuffle(self.tasks)  # segab listis andmed
        x = 0
        for s in self.students:  # liidab kaks listi
            # joondab listi pikima nime järgi
            self.students_tasks.append(str(s).ljust(self.longest_name + 2) + " - " + self.tasks[x])  # liidab kokku õpilase ja ülesande
            x += 1


    def set_tasks(self):
        """
        Kontroll kas ülesandeid jätkub igale õpilasele
        kui ülesandeid on vähem kui õpilasi, siis false ja teavitab kasutajat
        """
        if len(self.tasks) < len(self.students):  # kas ül. list on väiksem kui õpilaste list
            self.is_tasks = False
        else:
            self.is_tasks = True


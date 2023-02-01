import random
from tkinter import filedialog


class Model:

    def __init__(self):
        self.students_file = None
        self.tasks_file = None
        self.students_tasks= []
        self.students = []
        self.tasks = []
        self.is_tasks = False  # True kui ülesandeid jätkub kõigile õpilastele

    def open_students_file(self):
        # küsib õpilaste faili avamist > väljund on faili kaloogi tee
        # TODO lisa kontroll kas fail valiti
        self.students_file = filedialog.askopenfilename()

        #print(self.opilaste_faili_aadress)

    def read_students_file(self):
        self.students = []  # list tühjaks
        f = open(self.students_file, "r", encoding="utf-8")  # Avab faili lugemiseks
        for line in f:  # Loeb ridu failist ükshaaval
            line = line.strip()  # Lõikab rea küljest ära /n
            self.students.append(line)  # Kirjutab õpilaste nimed listi
        #print(self.students)

    def open_tasks_file(self):
        # küsib õpilaste faili avamist > väljund on faili kaloogi tee
        # TODO lisa kontroll kas fail valiti
        self.tasks_file = filedialog.askopenfilename()

    def read_tasks_file(self):
        self.tasks = []  # list tühjaks
        f = open(self.tasks_file, "r", encoding="utf-8")  # Avab faili lugemiseks
        for line in f:  # Loeb ridu failist ükshaaval
            line = line.strip()  # Lõikab rea küljest ära /n
            self.tasks.append(line)  # Kirjutab õpilaste nimed listi

    def mix_tasks_for_students(self):

        random.shuffle(self.tasks)
        x = 0
        for s in self.students:
            self.students_tasks.append(s + " - " + self.tasks[x])  # liidab kokku õpilase ja ülesande
            x += 1




    def set_tasks(self):
        """
        Kontroll kas ülesandeid jätkub igale õpilasele
        kui ülesandeid on vähem kui õpilasi, siis false ja teavitab kasutajat
        """
        if len(self.tasks) < len(self.students):
            self.is_tasks = False
        else:
            self.is_tasks = True
        print('self.is_tasks', self.is_tasks)
        # return self.is_tasks

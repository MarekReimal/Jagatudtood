from tkinter import *
from tkinter import ttk
import tkinter.font as tkfont  # tkfont on alias

class View(Tk):

    def __init__(self, controller, model):
        super().__init__()  # super on Tk
        self.controller = controller
        self.model = model

        # akna parameetrid
        self.geometry('800x500')
        self.title('Õpilased ja ülesanded')
        self.frame_top, self.frame_bottom = self.create_frames()
        self.btn_students, self.btn_tasks, self.btn_mix_tasks, self.btn_save_tasks = self.create_buttons()
        self.tbx_students, self.tbx_tasks, self.tbx_mixedtasks = self.create_textboxes()

        # kirjastiilide defineerimine
        self.big_font_style = tkfont.Font(family='Courier', size=18, weight='bold')  # tkfont vaja importida
        self.default_style_bold = tkfont.Font(family='Verdana', size=10, weight='bold')  # tkfont vaja importida
        self.default_style = tkfont.Font(family='Verdana', size=10)  # tkfont vaja importida

        #self.tbx_tasks.insert(INSERT, 'Tere')




    def create_frames(self):
        frame_top = Frame(self, bg='gray99', height=100)  #
        frame_bottom = Frame(self, bg='gray92')  #

        frame_top.pack(fill=BOTH)  # asetab ekraanile
        frame_bottom.pack(expand=True, fill=BOTH)  # asetab ekraanile
        return frame_top, frame_bottom

    def create_buttons(self):
        btn_students = Button(self.frame_top, text='Õpilased', height=2, width=18, command=self.controller.click_btn_students)
        btn_tasks = Button(self.frame_top, text='Ülesanded', height=2, width=18, command=self.controller.click_btn_tasks)
        btn_mix_tasks = Button(self.frame_top, text='Jaga ülesanded', height=2, width=18, command=self.controller.click_btn_mix_tasks)
        btn_save_tasks = Button(self.frame_top, text='Salvesta ülesanded', height=5, width=20)

        btn_students.grid(row=0)
        btn_tasks.grid(row=1)
        btn_mix_tasks.grid(row=2)
        btn_save_tasks.grid(row=1, column=1)
        return btn_students, btn_tasks, btn_mix_tasks, btn_save_tasks

    def create_textboxes(self):
        tbx_students = Text(self.frame_bottom, height=20, width=20)
        tbx_tasks = Text(self.frame_bottom, height=20, width=40)
        tbx_mixedtasks = Text(self.frame_bottom, height=20, width=40)

        tbx_students.grid(row=0, column=0)
        tbx_tasks.grid(row=0, column=1)
        tbx_mixedtasks.grid(row=0, column=2)

        return tbx_students, tbx_tasks, tbx_mixedtasks




    def main(self):
        self.mainloop()

from tkinter import *
from tkinter import ttk
import tkinter.font as tkfont  # tkfont on alias

class View(Tk):

    def __init__(self, controller, model):
        super().__init__()  # super on Tk
        self.controller = controller  # tuleb controllerist
        self.model = model  # tuleb kontrollerist

        # akna parameetrid
        self.geometry('1205x604')
        self.title('Õpilased ja ülesanded')

        # framid
        self.frame_top, self.frame_bottom = self.create_frames()
        # nupud
        self.btn_students, self.btn_tasks, self.btn_mix_tasks, self.btn_save_tasks = self.create_buttons()
        # tekstboxid
        self.tbx_students, self.tbx_tasks, self.tbx_mixedtasks = self.create_textboxes()

        #self.create_label()

        # kirjastiilide defineerimine
        self.big_font_style = tkfont.Font(family='Courier', size=18, weight='bold')  # tkfont vaja importida
        self.default_style_bold = tkfont.Font(family='Verdana', size=10, weight='bold')  # tkfont vaja importida
        self.default_style = tkfont.Font(family='Verdana', size=10)  # tkfont vaja importida



    def create_frames(self):
        frame_top = Frame(self, bg='gray82')  # , height=100
        frame_bottom = Frame(self, bg='gray82')  #

        frame_top.pack(fill=BOTH)  # asetab ekraanile
        frame_bottom.pack(expand=True, fill=BOTH)  # asetab ekraanile expand=True, fill=BOTH
        return frame_top, frame_bottom

    def create_buttons(self):
        btn_students = Button(self.frame_top, text='Vali õpilased', height=2, width=18, command=self.controller.click_btn_students)
        btn_tasks = Button(self.frame_top, text='Vali ülesanded', height=2, width=18, command=self.controller.click_btn_tasks)
        btn_mix_tasks = Button(self.frame_top, text='Jaga ülesanded', height=2, width=18, command=self.controller.click_btn_mix_tasks)
        btn_save_tasks = Button(self.frame_top, text='Salvesta ülesanded', height=9, width=20, command=self.controller.click_btn_save)


        btn_students.grid(row=0, padx=15, pady=10)
        btn_tasks.grid(row=1, padx=15, pady=0)
        btn_mix_tasks.grid(row=2, padx=15, pady=10)
        btn_save_tasks.grid(row=0, column=1, rowspan=4, padx=10, pady=5)
        return btn_students, btn_tasks, btn_mix_tasks, btn_save_tasks

    def create_textboxes(self):
        tbx_students = Text(self.frame_bottom, height=26, width=25)
        tbx_tasks = Text(self.frame_bottom, height=26, width=50)
        tbx_mixedtasks = Text(self.frame_bottom, height=26, width=70, wrap='none')

        tbx_students.grid(row=0, column=0, padx=5, pady=7)
        tbx_tasks.grid(row=0, column=1, rowspan=3, padx=5, pady=7)
        tbx_mixedtasks.grid(row=0, column=2, padx=5, pady=7)

        return tbx_students, tbx_tasks, tbx_mixedtasks

    #def create_label(self):
     #   lbl_keel = Label(self.frame_top, anchor='w', text='Vali keel')

      #  lbl_keel.grid(row=0, column=2)



    def main(self):
        """
        käivitab  GUI
        :return:
        """
        self.mainloop()

from tkinter import ttk, Radiobutton, IntVar, messagebox
from gui.setup import Setup

class Summarytable(Setup):


    def __init__(self, stat_analyzer):
        Setup.__init__(self, stat_analyzer)
        self.summarise_by = None


    def set_variable_to_summarise_by(self,column_name):
        self.summarise_by = column_name



    def do_setup(self):

        self.summarise_by = None
        # which variable to summarise by
        lbl = ttk.Label(master=self.frame,
                        text="Choose which variable to summarise by:")

        lbl.grid(row=0, column=0)
        objects = 0

        var = IntVar()

        for column in self.stat_analyzer.get_column_names():

            objects = objects + 1
            chk = Radiobutton(self.frame,
                                text=column,
                                variable=var,
                                value=objects,
                                command=lambda col=column: self.set_variable_to_summarise_by(col)
                                )

            chk.grid(row=objects, column = 0)

        # which variable to do summarystatistics

        lbl = ttk.Label(master=self.frame,
                        text='Choose which variable to summarise')
        lbl.grid(row=objects + 1, column=0)
        objects = objects + 1

        for colname in self.stat_analyzer.get_numeric_column_names():

            objects = objects + 1
            btn = ttk.Button(master=self.frame, text=colname,
                             command=lambda col=colname: self.analyze(col))
            btn.grid(row=objects, column=0)



    def analyze(self, column_name):

        if self.summarise_by is None:
            messagebox.showerror(message="Choose which variable to summarise by!")
            return

        self.display_result(self.stat_analyzer.summarytable(self.summarise_by,column_name))

from tkinter import ttk
from views.setup import Setup




class Frequencytable(Setup):

    def __init__(self,stat_analyzer):
        Setup.__init__(self,stat_analyzer)
        

    def do_setup(self):

        lbl = ttk.Label(master=self.frame, text='Choose which variable to tabulate')
        lbl.grid(row=0,column=0)
        
        for idx,column_name in enumerate(self.stat_analyzer.get_nonnumeric_column_names()):

            btn = ttk.Button( master=self.frame, text=column_name, command= lambda col=column_name: self.analyze(col) )
            btn.grid(row=idx+1,column=0)


    def analyze(self,column_name):
        print('Doing freqtable for {}'.format(column_name))
        self.display_result(self.stat_analyzer.summary(column_name))
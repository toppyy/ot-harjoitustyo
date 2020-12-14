from tkinter import ttk
from gui.setup import Setup
from gui.output_elements.table import Table
from gui.output_elements.header import Header

class Frequencytable(Setup):

    def initialize(self):
        """Creates the elements for this setup
        """

        lbl = ttk.Label(master=self.frame,
                        text='Choose which variable to tabulate')
        lbl.grid(row=0, column=0)

        column_types = self.stat_analyzer.get_column_types()

        for idx, colname in enumerate(self.stat_analyzer.get_column_names()):

            btn = ttk.Button(master=self.frame, text=colname,
                             command=lambda col=colname: self.analyze(col))
            btn.grid(row=idx+1, column=0)

            columntype = ttk.Label(master=self.frame, text=column_types[idx])
            columntype.grid(row=idx+1, column=1)

    def analyze(self, column_name):
        analysis_result = self.stat_analyzer.frequencytable(column_name)
        self.display_result(
            [
                Header(analysis_result[0]),
                Table(analysis_result[1])
            ]
        )

from tkinter import ttk
from gui.setup import Setup


class Summary(Setup):

    def initialize(self):
        """Creates the elements for this setup
        """

        lbl = ttk.Label(master=self.frame,
                        text='Choose which variable to summarise')
        lbl.grid(row=0, column=0)

        for idx, column_name in enumerate(self.stat_analyzer.get_numeric_column_names()):

            btn = ttk.Button(master=self.frame, text=column_name,
                             command=lambda col=column_name: self.analyze(col))
            btn.grid(row=idx+1, column=0)

    def analyze(self, column_name):
        """Runs the analysis task for the chosen column

        Args:
            column_name: name of the column to be analyzed
        """

        self.display_result(self.stat_analyzer.summary(column_name))

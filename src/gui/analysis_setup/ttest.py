from tkinter import ttk, Entry, IntVar, messagebox
from gui.setup import Setup
from gui.output_elements.header import Header
from gui.output_elements.text  import Text


class Ttest(Setup):


    def __init__(self,**kwargs):
        """Constructor
        """
        self.pop_mean_entry = None
        Setup.__init__(self,**kwargs)



    def set_population_mean(self,mean):
        """Setter for population mean (to compare sample against)

        Args:
            mean: population mean
        """
        self.group_by = column_name



    def initialize(self):
        """Creates the elements for this setup
        """


        lbl = ttk.Label(master=self.frame,
                        text="Insert population mean:")

        lbl.grid(row=0, column=0)
        objects = 1

        self.pop_mean_entry = Entry(master=self.frame)
        self.pop_mean_entry.grid(row=objects,column=0)
        objects = objects + 1

        print(self.pop_mean_entry.get())

        # which variable to analyze variance

        lbl = ttk.Label(master=self.frame,
                        text='Choose which variable to test')
        lbl.grid(row=objects + 1, column=0)
        objects = objects + 1

        for colname in self.stat_analyzer.get_numeric_column_names():

            objects = objects + 1
            btn = ttk.Button(master=self.frame, text=colname,
                             command=lambda col=colname: self.analyze(col))
            btn.grid(row=objects, column=0)



    def analyze(self, column_name):

        pop_mean = self.pop_mean_entry.get()

        if pop_mean == "":
            messagebox.showerror(message="Insert population mean!")
            return

        try:
            pop_mean = float(pop_mean)
        except ValueError:
            messagebox.showerror(message="Enter a valid number as population mean!")
            return

        analysis_result = self.stat_analyzer.analyse(self.analysis,[column_name],pop_mean)
        header = column_name


        self.display_result([
            Header(header),
            Text('Mean: {}'.format(analysis_result[0])),
            Text('Population mean: {}'.format(analysis_result[1])),
            Text('T-statistic: {}'.format(analysis_result[2])),
            Text('P-value: {}'.format(analysis_result[3])),
            Text('Degrees of freedom: {}'.format(analysis_result[4])),
            Text('(test is two-way)')

        ])

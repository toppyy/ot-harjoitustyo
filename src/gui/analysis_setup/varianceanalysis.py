from tkinter import ttk, Radiobutton, IntVar, messagebox
from gui.setup import Setup
from gui.output_elements.header import Header
from gui.output_elements.text  import Text

class Varianceanalysis(Setup):


    def __init__(self,**kwargs):
        """Constructor
        """

        Setup.__init__(self,**kwargs)

        self.group_by = None

    def set_variable_to_group_by(self,column_name):
        """Setter for the variable to summarise by

        Args:
            column_name: name of the column to do summary statistics by
        """
        self.group_by = column_name



    def initialize(self):
        """Creates the elements for this setup
        """
        # which variable to summarise by

        lbl = ttk.Label(master=self.frame,
                        text="Choose which variable to group by:")

        lbl.grid(row=0, column=0)
        objects = 0

        var = IntVar()

        for column in self.stat_analyzer.get_nonnumeric_column_names():

            objects = objects + 1
            chk = Radiobutton(self.frame,
                                text=column,
                                variable=var,
                                value=objects,
                                command=lambda col=column: self.set_variable_to_group_by(col)
                                )

            chk.grid(row=objects, column = 0)

        # which variable to analyze variance

        lbl = ttk.Label(master=self.frame,
                        text='Choose which which variable to analyse')
        lbl.grid(row=objects + 1, column=0)
        objects = objects + 1

        for colname in self.stat_analyzer.get_numeric_column_names():

            objects = objects + 1
            btn = ttk.Button(master=self.frame, text=colname,
                             command=lambda col=colname: self.analyze(col))
            btn.grid(row=objects, column=0)



    def analyze(self, column_name):

        if self.group_by is None:
            messagebox.showerror(message="Choose which variable to group by!")
            return

        analysis_result = self.stat_analyzer.varianceanalysis(self.group_by,column_name)
        header = self.group_by + '\nvs.\n' + column_name


        self.display_result([
            Header(header),
            Text('Sum of squares between: {}'.format(analysis_result[0])),
            Text('Sum of squares within: {}'.format(analysis_result[1])),
            Text('Mean sum of squares between: {}'.format(analysis_result[2])),
            Text('Mean sum of squares within: {}'.format(analysis_result[3])),
            Text('F-statistic: {}'.format(analysis_result[4])),
            Text('P-value: {}'.format(analysis_result[5]))
        ])

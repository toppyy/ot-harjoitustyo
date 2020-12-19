from tkinter import ttk,  Checkbutton, IntVar, messagebox
from gui.setup import Setup


class Scatterplot(Setup):
    """Class for setting up scatterplot-analysis
    """

    def __init__(self,**kwargs):
        """Constructor
        """

        Setup.__init__(self,**kwargs)

        self.variables_to_plot = []

    def initialize(self):
        """Creates the setup for this analysis

        """

        lbl = ttk.Label(master=self.frame,
                        text="Choose which variable to summarise by:")

        lbl.grid(row=0, column=0)
        objects = 0



        for column in self.stat_analyzer.get_column_names():
            var = IntVar()
            objects = objects + 1
            chk = Checkbutton(self.frame,
                                text=column,
                                variable=var,
                                command=lambda col=column: self.set_columns_to_plot(col)
                                )

            chk.grid(row=objects, column = 0)

        btn = ttk.Button(master=self.frame,text='Plot!',command=self.analyze)
        btn.grid(row=objects+1,column=0)

    def analyze(self):
        """Calls the StatAnalyzer for analysis and displays output

        Args:
            column_name_a: one the of the columns to plot
            column_name_b: the other one the of the columns to plot
        """
        if len(self.variables_to_plot) is not 2:
            messagebox.showerror(message="Choose two variables!")
            return

        col_a = self.variables_to_plot[0]
        col_b = self.variables_to_plot[1]
        self.stat_analyzer.analyse(self.analysis,[col_a,col_b],self.analysis['plotlibrary'])



    def set_columns_to_plot(self,column_name):
        """Control which columns are to be plotted

        Args:
            column_name: name of column to add/remove
        """

        if column_name in self.variables_to_plot:
            self.variables_to_plot = [x for x in self.variables_to_plot if x != column_name]
        else:
            self.variables_to_plot.append(column_name)

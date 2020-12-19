from tkinter import ttk,  Radiobutton, IntVar, messagebox
from gui.setup import Setup


class Barplot(Setup):
    """Class for setting up Barplot-analysis
    """
    def __init__(self,**kwargs):
        """Constructor
        """

        Setup.__init__(self,**kwargs)
        self.variable_to_plot = None


    def set_column_to_plot(self,column_name):
        """Control which columns is plotted

        Args:
            column_name: name of column to plot
        """
        self.variable_to_plot = column_name

    def initialize(self):
        """Creates the setup for this analysis

        """

        lbl = ttk.Label(master=self.frame,
                        text="Choose which variable to create barplot for:")

        lbl.grid(row=0, column=0)
        objects = 0


        var = IntVar()
        for column in self.stat_analyzer.get_column_names():

            objects = objects + 1
            chk = Radiobutton(self.frame,
                                text=column,
                                variable=var,
                                value=objects,
                                command=lambda col=column: self.set_column_to_plot(col)
                                )

            chk.grid(row=objects, column = 0)

        btn = ttk.Button(master=self.frame,text='Plot!',command=self.analyze)
        btn.grid(row=objects+1,column=0)

    def analyze(self):
        """Calls the StatAnalyzer for analysis and displays output
        """
        if self.variable_to_plot is None:
            messagebox.showerror(message="Choose one variable!")
            return

        col = self.variable_to_plot
        self.stat_analyzer.analyse(self.analysis,[col],self.analysis['plotlibrary'])

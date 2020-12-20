from tkinter import ttk, Radiobutton, IntVar, messagebox, Listbox, MULTIPLE
from gui.setup import Setup
from gui.output_elements.header import Header
from gui.output_elements.text  import Text

class LinearRegression(Setup):


    def __init__(self,**kwargs):
        """Constructor
        """

        Setup.__init__(self,**kwargs)
        self.depended_variable = None
        self.regressor = None

    def set_dependent_variable(self,depended_variable):

        self.depended_variable = depended_variable

    def set_regressor(self,regressor):
        self.regressor = regressor

    def create_radiobuttons(self,texts,grid_row,callback):
        var = IntVar()

        for idx,buttontext in enumerate(texts):

            chk = Radiobutton(self.frame,
                                text=buttontext,
                                variable=var,
                                value=idx,
                                command=lambda val=buttontext: callback(val)
                                )

            chk.grid(row=grid_row+idx, column = 0)


    def initialize(self):
        """Creates the elements for this setup
        """

        numeric_columns = self.stat_analyzer.get_numeric_column_names()

        lbl = ttk.Label(master=self.frame,
                        text="Choose dependend variable:")

        lbl.grid(row=0, column=0)
        objects = 1

        self.create_radiobuttons(
            numeric_columns,
            objects,
            self.set_dependent_variable
        )
        objects = objects + len(numeric_columns)


        # which variable to analyze variance
        objects = objects + 2
        lbl = ttk.Label(master=self.frame,
                        text='Choose regressors:')
        lbl.grid(row=objects, column=0)
        objects = objects + 2

        self.create_radiobuttons(
            numeric_columns,
            objects,
            self.set_regressor
        )
        objects = objects + len(numeric_columns)

        # Regress button
        btn = ttk.Button(
                        master=self.frame,
                        text='Regress!',
                        command=lambda: self.analyze())
        btn.grid(row=objects, column=0)

    def get_column_name_by_idx(self,idx):
        """Get name for a specific index

        Args:
            index of column whose name is of interest
        """

        names = self.stat_analyzer.get_numeric_column_names()

        return names[idx]


    def analyze(self):


        if self.depended_variable is None or self.regressor is None:
            messagebox.showerror(message="Choose dependent variable!")
            return

        if self.depended_variable == self.regressor:
            messagebox.showerror(message="Dependent and regressor are the same?")
            return

        slope, intercept, r_value, p_value, std_err  = self.stat_analyzer.analyse(
            self.analysis,
            [self.depended_variable,self.regressor]
        )

        header = self.depended_variable + '\nvs.\n' + self.regressor

        output = [
            Header(header),
            Text('Slope: {}'.format(slope)),
            Text('Intercept: {}'.format(intercept)),
            Text('R-value: {}'.format(r_value)),
            Text('P-value: {}'.format(p_value)),
            Text('Standard error: {}'.format(std_err))
        ]


        self.display_result(output)

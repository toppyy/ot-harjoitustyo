from tkinter import ttk


class Homeview:

    def __init__(self,root,analyses,show_setup,stat_analyzer,show_error):
        """Constructor

        Args:
            root: The window to bind this view to
            analyses: List (names) of analysis tasks to display buttons for
            show_setup: function to call when analysis task is chosen
        """
        self.root = root
        self.analyses = analyses
        self.show_setup = show_setup
        self.stat_analyzer = stat_analyzer
        self.show_error = show_error
        self.initialize()

    def initialize(self):
        """Create elements for this view
        """

        self.frame = ttk.Frame(master=self.root)

        for idx, text in enumerate(self.analyses.keys()):
            btn = ttk.Button(
                                master=self.frame,
                                text=text,
                                command=lambda text=text: self.consider_setup(text)
                            )
            btn.grid(row=idx+1, column=0,padx=20,pady=4)

    def destroy(self):
        """Destroy the frame
        """
        self.frame.destroy()

    def pack(self):
        """Pack the frame
        """
        self.frame.pack()


    def consider_setup(self,column_name):
        """Starts setup if stat analyzer has a dataset to analyze

        Args:
            column_name: name of the column to analyze

        """

        if self.stat_analyzer.has_dataset():
            self.show_setup(column_name)

        else:
            err_msg = 'Error: No dataset.\n'
            err_msg = err_msg + 'Try loading the example dataset.\n(File -> Load exampledata)'

            self.show_error(err_msg)

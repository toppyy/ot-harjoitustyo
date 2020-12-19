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

        for idx, key in enumerate(self.analyses.keys()):

            analysis = self.analyses[key]

            btn = ttk.Button(
                                master=self.frame,
                                text=analysis['displayname'],
                                command=lambda key=key: self.consider_setup(key)
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


    def consider_setup(self,analysiskey):
        """Starts setup if stat analyzer has a dataset to analyze

        Args:
            analysiskey: key of the analysis

        """

        if self.stat_analyzer.has_dataset():
            self.show_setup(self.analyses[analysiskey])

        else:
            err_msg = 'Error: No dataset.\n'
            err_msg = err_msg + 'Try loading the example dataset.\n(File -> Load exampledata)'

            self.show_error(err_msg)

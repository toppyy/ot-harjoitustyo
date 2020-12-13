from tkinter import ttk, Tk

from gui.output import Output


class Setup:
    """Generic parent class for views setting up analysis tasks
    """

    #def __init__(self, stat_analyzer, window, show_error):
    def __init__(self,**kwargs):
        """Constructor

        Args:
            stat_analyzer: reference to an instance of class StatAnalyzer
            window: window to bind frame to
            show_error: function to call when error occurs with error message
        """
        self.frame = None
        self.window = kwargs['window']

        self.stat_analyzer = kwargs['stat_analyzer']
        self.show_error = kwargs['show_error']

        self.frame = ttk.Frame(master=self.window)
        self.initialize()

    def display_result(self, result):
        """Display results by create an instance of Output-class

        Args:
            result: Results of the analysis task
        """
        Output(result).pack()

    def destroy(self):
        """Close
        """
        self.frame.destroy()

    def pack(self):
        """Create
        """
        self.frame.pack()

    def initialize(self):
        """Initialize setup view for a particular setup
        """
        pass

    def analyze(self, column_name=None):
        """Perform analysis

        Args:
            column_name: Name of column to analyze
        """
        pass

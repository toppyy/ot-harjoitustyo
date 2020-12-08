from tkinter import ttk, Tk

from gui.output import Output


class Setup:
    """Generic parent class for views setting up analysis tasks
    """

    def __init__(self, stat_analyzer):
        """Constructor

        Args:
            stat_analyzer: reference to an instance of class StatAnalyzer
        """
        self.frame = None
        self.initialize()
        self.stat_analyzer = stat_analyzer
        self.do_setup()

    def initialize(self):
        """Create view
        """

        window = Tk()
        window.title("Analysis setup")

        self.frame = ttk.Frame(master=window)

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

    def do_setup(self):
        """Initialize setup view
        """
        pass

    def analyze(self, column_name=None):
        """Perform analysis

        Args:
            column_name: Name of column to analyze
        """
        pass

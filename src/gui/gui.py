from tkinter import ttk

from gui.analysis.summary import Summary
from gui.analysis.frequency_table import Frequencytable
from gui.error import Error
from misc.load_exampledata import load_exampledata


class GUI:

    def __init__(self, root, StatAnalyzer):
        self.root = root
        self.stat_analyzer = StatAnalyzer

    def start(self):
        frame = ttk.Frame(master=self.root)

        available_commands = self.stat_analyzer.get_available_commands()

        for idx, text in enumerate(available_commands):
            btn = ttk.Button(master=frame, text=text,
                             command=lambda text=text: self.init_setup(text))
            btn.grid(row=idx+1, column=0)

        frame.pack()

    def init_setup(self,analysis_name):

        if not self.stat_analyzer.has_dataset():

            if analysis_name == 'Load example-data':
                self.stat_analyzer.set_dataset(load_exampledata())
                return

            Error('Error: No dataset.\n Try loading the example dataset.').throw()
            return

        if analysis_name == 'Summary':
            setup = Summary(self.stat_analyzer)
            setup.pack()

        if analysis_name == 'Frequency table':
            setup = Frequencytable(self.stat_analyzer)
            setup.pack()

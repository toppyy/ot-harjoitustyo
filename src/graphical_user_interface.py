from tkinter import ttk
from misc.init_setup import init_setup

class GUI:

    def __init__(self, root, StatAnalyzer):
        self.root = root
        self.stat_analyzer = StatAnalyzer

    def start(self):
        frame = ttk.Frame(master=self.root)

        available_commands = self.stat_analyzer.get_available_commands()

        for idx, text in enumerate(available_commands):
            btn = ttk.Button(master=frame, text=text,
                             command=lambda text=text: self.do_command(text))
            btn.grid(row=idx+1, column=0)

        frame.pack()

    def do_command(self, analysis_name):

        init_setup(analysis_name, self.stat_analyzer)

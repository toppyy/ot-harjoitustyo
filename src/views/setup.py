from tkinter import ttk, Tk

from views.output import Output


class Setup:

    def __init__(self, stat_analyzer):
        self.frame = None
        self.initialize()
        self.stat_analyzer = stat_analyzer
        self.do_setup()

    def initialize(self):

        window = Tk()
        window.title("Analysis setup")

        self.frame = ttk.Frame(master=window)

    def display_result(self, result):
        Output(result).pack()

    def destroy(self):
        self.frame.destroy()

    def pack(self):
        self.frame.pack()

    def do_setup(self):
        pass

    def analyze(self):
        pass
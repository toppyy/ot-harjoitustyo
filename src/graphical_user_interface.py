from tkinter import Tk, ttk
from misc.init_setup import init_setup
from views.commands import Commands
from views.setup import Setup


class GUI:

    def __init__(self, root, StatAnalyzer):
        self.root = root
        self.stat_analyzer = StatAnalyzer

    def start(self):
        self.current_view = Commands(self.root, self.do_command)
        self.current_view.pack()

    def do_command(self, analysis_name):

        init_setup(analysis_name, self.stat_analyzer)
        return

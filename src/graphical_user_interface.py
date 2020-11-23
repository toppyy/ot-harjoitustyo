from tkinter import Tk, ttk, StringVar
from file_access import FileAccess
from dataset import Dataset
from views.commands import Commands
from views.setup    import Setup
from misc.init_setup import init_setup




class GUI:

    def __init__(self, root, StatAnalyzer):
        self.root = root
        self.stat_analyzer = StatAnalyzer
        self.file_access_object = FileAccess()
        

    def start(self):
        self.current_view = Commands(self.root, self.do_analysis)
        self.current_view.pack()

    def do_analysis(self,analysis_name):
        init_setup(analysis_name,self.stat_analyzer)
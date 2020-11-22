from tkinter import Tk, ttk, StringVar
from file_access import FileAccess
from dataset import Dataset
from views.commands import Commands
from misc.display_analysis import display_analysis


class GUI:

    def __init__(self, root, StatAnalyzer):
        self.root = root
        self.stat_analyzer = StatAnalyzer
        self.file_access_object = FileAccess()
        

    def start(self):
        self.current_view = Commands(self.root,self.stat_analyzer, display_analysis)
        self.current_view.pack()

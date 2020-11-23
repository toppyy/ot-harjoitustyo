from misc.init_setup import init_setup
from views.commands import Commands

class GUI:

    def __init__(self, root, StatAnalyzer):
        self.root = root
        self.stat_analyzer = StatAnalyzer

    def start(self):
        view = Commands(self.root, self.do_command)
        view.pack()

    def do_command(self, analysis_name):

        init_setup(analysis_name, self.stat_analyzer)

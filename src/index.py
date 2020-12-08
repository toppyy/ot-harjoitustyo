import sys

from stat_analyzer import StatAnalyzer
from gui.gui import GUI

arguments = sys.argv

stat_analyzer = StatAnalyzer(None)
ui = GUI(stat_analyzer)

# If running with argument "dev". Load example data
if len(arguments) > 1 and arguments[1] == 'dev':
    ui.load_exampledata()

ui.start()

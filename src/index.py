import sys

from stat_analyzer import StatAnalyzer
from gui.gui import GUI
from misc.load_file_as_dataset import load_exampledata

arguments = sys.argv

DATASET = None

# If running with argument "dev". Load example data
if len(arguments) > 1 and arguments[1] == 'dev':
    DATASET = load_exampledata()


stat_analyzer = StatAnalyzer(DATASET)


ui = GUI(stat_analyzer)
ui.start()

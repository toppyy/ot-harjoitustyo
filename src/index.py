
import sys
from tkinter import Tk

from stat_analyzer import StatAnalyzer
from graphical_user_interface import GUI
from misc.load_exampledata import load_exampledata

arguments = sys.argv

DATASET = None

# If running with argument "dev". Load example data
if len(arguments) > 1 and arguments[1] == 'dev':
    DATASET = load_exampledata()


stat_analyzer = StatAnalyzer(DATASET)

window = Tk()
window.title("Stat analyzer")

ui = GUI(window, stat_analyzer)
ui.start()

window.mainloop()

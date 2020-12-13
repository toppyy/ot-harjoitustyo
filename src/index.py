import sys
from tkinter import Tk

from stat_analyzer import StatAnalyzer
from gui.gui import GUI

arguments = sys.argv

stat_analyzer = StatAnalyzer(None)

window = Tk()
window.title("Stat analyzer")

ui = GUI(window,stat_analyzer)

# If running with argument "dev". Load example data
if len(arguments) > 1 and arguments[1] == 'dev':
    ui.load_exampledata()

ui.start()

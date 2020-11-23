
import sys
from tkinter import Tk, ttk

from stat_analyzer import StatAnalyzer
from graphical_user_interface import GUI
from views.output import Output
from misc.load_exampledata import load_exampledata

arguments = sys.argv

data = None

# If running with argument "dev". Load example data
if len(arguments)>1 and arguments[1] == 'dev':
    data = load_exampledata()
    #data = Dataset( FileAccess().read_csv('./data/tyovoimakunnittain.csv', ";", '"') )
    #data.create()


stat_analyzer = StatAnalyzer(data)

window = Tk()
window.title("Stat analyzer")

ui = GUI(window,stat_analyzer)
ui.start()

window.mainloop()
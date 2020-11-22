
import sys

from stat_analyzer import StatAnalyzer
from graphical_user_interface import GUI
from file_access import FileAccess
from dataset import Dataset
from tkinter import Tk, ttk
from views.output import Output

arguments = sys.argv

data = Dataset( FileAccess().read_csv('./data/tyovoimakunnittain.csv', ";", '"') )
data.create()
stat_analyzer = StatAnalyzer(data)

window = Tk()
window.title("TkInter example")

ui = GUI(window,stat_analyzer)
ui.start()

window.mainloop()
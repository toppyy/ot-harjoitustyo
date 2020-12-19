import sys
from tkinter import Tk

from dataset_repository import DatasetRepository
from misc.db_connection import get_database_connection
from stat_analyzer import StatAnalyzer
from analyses_config import get_analyses_config
from gui.gui import GUI

arguments = sys.argv

stat_analyzer = StatAnalyzer(dataset=None,analyses = get_analyses_config() )
dataset_repository = DatasetRepository(get_database_connection())

window = Tk()
window.title("Stat analyzer")

ui = GUI(window,stat_analyzer, dataset_repository)

# If running with argument "dev". Load example data
if len(arguments) > 1 and arguments[1] == 'dev':
    ui.load_exampledata()

ui.start()

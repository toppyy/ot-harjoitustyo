from gui.analysis.summary import Summary
from gui.analysis.frequency_table import Frequencytable
from gui.error import Error
from misc.load_exampledata import load_exampledata


def init_setup(analysis_name, stat_analyzer):

    if not stat_analyzer.has_dataset():

        if analysis_name == 'Load example-data':
            stat_analyzer.set_dataset(load_exampledata())
            return

        Error('Error: No dataset.\n Try loading the example dataset.').throw()
        return

    if analysis_name == 'Summary':
        setup = Summary(stat_analyzer)
        setup.pack()

    if analysis_name == 'Frequency table':
        setup = Frequencytable(stat_analyzer)
        setup.pack()

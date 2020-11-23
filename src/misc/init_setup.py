from views.setup import Setup
from views.analysis.summary import Summary
from views.analysis.frequency_table import Frequencytable


def init_setup(analysis_name,stat_analyzer):

    if analysis_name == 'Summary':
        setup = Summary(stat_analyzer)
        setup.pack()


    if analysis_name == 'Frequency table':
        setup = Frequencytable(stat_analyzer)
        setup.pack()
    
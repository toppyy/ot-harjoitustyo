import matplotlib.pyplot as plt

from analyses.summary           import summary
from analyses.frequencytable    import frequencytable
from analyses.summarytable      import summarytable
from analyses.scatterplot       import scatterplot
from analyses.barplot           import barplot
from analyses.varianceanalysis  import varianceanalysis
from analyses.ttest             import ttest
from analyses.linear_regression import linear_regression

from gui.analysis_setup.summary             import Summary
from gui.analysis_setup.frequencytable      import Frequencytable
from gui.analysis_setup.summarytable        import Summarytable
from gui.analysis_setup.scatterplot         import Scatterplot
from gui.analysis_setup.barplot             import Barplot
from gui.analysis_setup.varianceanalysis    import Varianceanalysis
from gui.analysis_setup.ttest               import Ttest
from gui.analysis_setup.linear_regression   import LinearRegression

def get_analyses_config():
    """Function to act as a central repository for analysis tasks

    Returns:
        A dictionary consisting of analysis tasks.
    """

    analyses  = {
        'summary':    {
            'displayname': 'Summary',
            'setup': Summary,
            'analyse': summary
        },
        'freqtable':  {
            'displayname': 'Frequency table',
            'setup': Frequencytable,
            'analyse': frequencytable
        },
        'summarytable': {
            'displayname': 'Summarytable',
            'setup': Summarytable,
            'analyse': summarytable
        },
        'barplot': {
            'displayname': 'Barplot',
            'setup': Barplot,
            'analyse': barplot,
            'plotlibrary': plt
        },
        'scatterplot': {
            'displayname': 'Scatterplot',
            'setup': Scatterplot,
            'analyse': scatterplot,
            'plotlibrary': plt
        },
        'anova':  {
            'displayname': 'Variance analysis (ANOVA)',
            'setup': Varianceanalysis,
            'analyse': varianceanalysis
        },
        'ttest':  {
            'displayname': 'T-test',
            'setup': Ttest,
            'analyse': ttest
        },
        'linearregression': {
            'displayname': 'Linear regression',
            'setup': LinearRegression,
            'analyse': linear_regression
        }
    }
    return analyses

import matplotlib.pyplot as plt

from analyses.summary        import summary
from analyses.frequencytable import frequencytable
from analyses.summarytable   import summarytable
from analyses.scatterplot    import scatterplot
from analyses.barplot        import barplot

from gui.analysis_setup.summary           import Summary
from gui.analysis_setup.frequencytable    import Frequencytable
from gui.analysis_setup.summarytable      import Summarytable
from gui.analysis_setup.scatterplot       import Scatterplot
from gui.analysis_setup.barplot           import Barplot

class StatAnalyzer:
    """Class for controlling the statistical analysis tasks
    """

    def __init__(self, dataset=None):
        """Constructor for class

        Args:
            dataset: An instance of class Dataset
        """
        self.dataset = dataset

    def set_dataset(self, dataset):
        """Setter for dataset

        Args:
            dataset: An instance of class Dataset
        """
        self.dataset = dataset

    def get_available_analyses(self):
        """Lists available analyses and binds them to setup views

        Returns:
            dict: Possible analyses
        """

        analyses = {
            "Summary": Summary,
            "Frequency table": Frequencytable,
            "Summary table": Summarytable,
            "Scatterplot": Scatterplot,
            "Barplot": Barplot
        }

        return analyses

    def summary(self, column):
        """Run summary-analysis tasks

        Args:
            column: Name of column to analyze

        Returns:
            Output of summary-analysis
        """
        data = self.dataset.get_column(column)
        return summary(data)

    def frequencytable(self, column):
        """Run frequency table-analysis tasks

        Args:
            column: Name of column to analyze

        Returns:
            Output of frequency table-analysis
        """
        data = self.dataset.get_column(column)
        return frequencytable(data)

    def barplot(self,column):
        """Create barplot

        Args:
            column: Name of column to plot

        Returns:
            Output of barplot (none)
        """
        data = self.dataset.get_column(column)
        return barplot(data, plt)

    def summarytable(self, column_to_summarise_by,column_to_summarise):
        """Run summary table-analysis tasks

        Args:
            column: Name of column to analyze

        Returns:
            Output of summary table-analysis
        """
        data_summarise_by   = self.dataset.get_column(column_to_summarise_by)
        data_summarise      = self.dataset.get_column(column_to_summarise)
        return summarytable(data_summarise_by,data_summarise)

    def scatterplot(self, column_name_a, column_name_b):
        """Create scatterplot

        Args:
            column: Name of column to plot

        Returns:
            Output of scatterplot (none)
        """
        column_a   = self.dataset.get_column(column_name_a)
        column_b    = self.dataset.get_column(column_name_b)

        return scatterplot(column_a,column_b,plt)

    def get_column_names(self):
        """Getter for column names of associated dataset

        Returns:
            list: Column names in dataset
        """
        return self.dataset.get_column_names()

    def get_column_types(self):
        """Getter for columns types of associated dataset

        Returns:
            list: Column types (strings)
        """
        return self.dataset.get_column_types()

    def get_numeric_column_names(self):
        """Returns names of columns that are numeric (not a string)

        Returns:
            list: A subset of column names
        """
        return self.dataset.get_numeric_column_names()

    def get_nonnumeric_column_names(self):
        """Returns names of columns that are not numeric

        Returns:
            list: A subset of column names
        """
        return self.dataset.get_nonnumeric_column_names()

    def has_dataset(self):
        """Getter for dataset information

        Returns:
            Boolean: True, if dataset is set
        """
        return self.dataset is not None

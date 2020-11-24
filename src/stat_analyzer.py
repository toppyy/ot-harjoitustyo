from analyses.summary import summary
from analyses.frequencytable import frequencytable


class StatAnalyzer:

    def __init__(self, dataset=None):
        self.dataset = dataset

    def set_dataset(self, dataset):
        self.dataset = dataset

    def summary(self, column):
        data = self.dataset.get_column(column)
        return summary(data)

    def frequencytable(self, column):
        data = self.dataset.get_column(column)
        return frequencytable(data)

    def get_column_names(self):
        return self.dataset.get_column_names()

    def get_column_types(self):
        return self.dataset.get_column_types()

    def get_numeric_column_names(self):
        return self.dataset.get_numeric_column_names()

    def get_nonnumeric_column_names(self):
        return self.dataset.get_nonnumeric_column_names()

    def has_dataset(self):
        return self.dataset is not None


    def get_available_commands(self):
        return ['Frequency table', 'Summary', 'Load example-data']


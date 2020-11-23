import re
from math_helper.mean   import mean
from math_helper.median import median
from analyses.summary import summary


class StatAnalyzer:

    def __init__(self, dataset=None):
        self.dataset = dataset

    def set_dataset(self, dataset):
        self.dataset = dataset

    def summary(self,column):
        data = self.dataset.get_column(column)
        return summary(data)

    def get_column_names(self):
        return self.dataset.get_column_names()

    def get_numeric_column_names(self):
        return self.dataset.get_numeric_column_names()


    def get_nonnumeric_column_names(self):
        return self.dataset.get_nonnumeric_column_names()

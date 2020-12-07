from analyses.summary        import summary
from analyses.frequencytable import frequencytable
from analyses.summarytable   import summarytable
from analyses.scatterplot    import scatterplot

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

    def summarytable(self, column_to_summarise_by,column_to_summarise):
        data_summarise_by   = self.dataset.get_column(column_to_summarise_by)
        data_summarise      = self.dataset.get_column(column_to_summarise)
        return summarytable(data_summarise_by,data_summarise)

    def scatterplot(self, column_name_a, column_name_b):
        column_a   = self.dataset.get_column(column_name_a)
        column_b    = self.dataset.get_column(column_name_b)

        return scatterplot(column_a,column_b)

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

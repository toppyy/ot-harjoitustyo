
class StatAnalyzer:
    """Class for executing analysis tasks on data
    """

    def __init__(self, dataset=None, analyses=None):
        """Constructor for class

        Args:
            dataset: An instance of class Dataset
        """
        self.dataset = dataset
        self.analyses = analyses


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

        return self.analyses

    def analyse(self, analysis, columns, *args):
        """Run analysis tasks

        Args:
            analysis
            columns: list of column_names. The data for these columns is passed forward
            args: additional arguments to pass to analyse function

        Returns:
            Output of analysis task
        """
        analyse_function = analysis['analyse']
        data = []
        for column in columns:
            data.append(self.dataset.get_column(column))

        if len(args)>0:
            return analyse_function(*data,*list(args))

        return analyse_function(*data)


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

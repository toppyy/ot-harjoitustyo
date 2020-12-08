from misc.convert_to import convert_to
from misc.guess_datatype import guesstype


class Dataset:
    """Class to provide access to data and metadata

    Attributes:
        rows: rows in the dataset (passed from read_csv)
        data: a dictionary for storing the data
        column_names: names of the columns in the dataset
        column_types: column datatypes as strings
    """
    def __init__(self, rows):
        """Constructor for class

        Args:
            rows (list): A list representing the rows in the dataset
        """
        self.rows = rows
        self.dataset = None
        self.column_names = None
        self.column_types = []
        self.gui = None


    def create_column_names(self,has_header):
        """List column names by either generating them or taking them from the data

        Args:
            has_header (bool): True, if the dataset has a header row

        Returns:
            list: list of column names
        """

        column_names = ['col'+str(idx)
                             for idx in range(0, len(self.rows[0]))]
        if has_header:
            column_names = self.rows.pop(0)

        return column_names

    def create(self, has_header=True, gui=None):
        """ Stores the data as columns instead of rows and stores column names
            Data is stored in a dict. The key is the column name.

        Args:
            has_header (bool, optional): True if the dataset has a header row. Defaults to True.
            gui: Reference to the main class controlling the GUI
        """

        self.gui = gui

        if self.rows is None:
            return

        self.column_names = self.create_column_names(has_header)

        columnstore = [[] for header in self.column_names]

        for row in self.rows:
            for column_idx in range(0,len(self.column_names)):
                columnstore[column_idx].append(row[column_idx])

        self.dataset = {}

        for col_idx, column in enumerate(columnstore):

            guessingrows = 5
            coltype = guesstype(column[0:guessingrows])

            column_name = self.column_names[col_idx]

            data_and_coltype = self.convert_to( column, coltype, column_name )

            self.dataset[column_name] = data_and_coltype["data"]
            self.column_types.append(data_and_coltype["coltype"])

    def convert_to(self,data,target_type,column_name):
        """Tries to do data conversion

        Args:
            data: A list of data to be converted
            target_type: The type of data to be converted to
            column_name: Name of column that is under conversion

        Returns:
            dict: Object that has the converted data and data type after conversion
        """

        try:
            return {
                "data": convert_to(data,target_type),
                "coltype": target_type
            }
        except ValueError:

            error_msg = 'Error converting column {} to {}'.format(column_name,target_type)
            error_msg = error_msg + '\nReturning column as str.'

            self.gui.show_warning(error_msg)

            result_type='str'

        return {
            "data": data,
            "coltype": result_type
        }



    def get_column(self, column_name):
        """Returns data and name for requested column

        Args:
            column_name (string): Name of column data was requested for

        Returns:
            dict: Object holding the data and name of requested column
        """

        return {
            "column_name": column_name,
            "data": self.dataset[column_name]
        }

    def get_column_names(self):
        """Getter for column names

        Returns:
            list: Column names in dataset
        """
        return self.column_names

    def get_rowcount(self):
        """Getter for number of rows in the dataset

        Returns:
            int: Number of rows
        """
        return len(self.rows)

    def get_column_types(self):
        """Getter for columns types

        Returns:
            list: Column types (strings)
        """
        return self.column_types

    def get_numeric_column_names(self):
        """Returns names of columns that are numeric (not a string)

        Returns:
            list: A subset of column names
        """
        colnames = self.column_names
        return [name for idx, name in enumerate(colnames) if self.column_types[idx] != 'str']

    def get_nonnumeric_column_names(self):
        """Returns names of columns that are not numeric

        Returns:
            list: A subset of column names
        """
        numeric_cols = self.get_numeric_column_names()
        return [colname for colname in self.column_names if colname not in numeric_cols]

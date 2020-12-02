from misc.convert_to import convert_to
from misc.guess_datatype import guesstype


class Dataset:
    def __init__(self, rows):
        self.rows = rows
        self.dataset = None
        self.columnstore = {}
        self.column_names = None
        self.column_types = []


    def create_column_names(self,has_header):

        column_names = ['col'+str(idx)
                             for idx in range(0, len(self.rows[0]))]
        if has_header:
            column_names = self.rows.pop(0)

        return column_names

    def create(self, has_header=True):

        # Do nothing if there are no rows
        if self.rows is None:
            return

        self.column_names = self.create_column_names(has_header)

        columnstore = [[] for header in self.column_names]

        # Data is as a set of columns instead of rows
        for row in self.rows:
            for column_idx in range(0,len(self.column_names)):
                columnstore[column_idx].append(row[column_idx])

        # Data is stored in a dict. The key is the column name
        # Store into dict ja do relevant type conversions
        self.dataset = {}

        for col_idx, column in enumerate(columnstore):

            guessingrows = 5
            coltype = guesstype(column[0:guessingrows])

            # Convert_to returns the coltype that resulted, not what was requested
            data_and_coltype = convert_to(column, coltype, self.column_names[col_idx])

            self.dataset[self.column_names[col_idx]] = data_and_coltype["data"]
            self.column_types.append(data_and_coltype["coltype"])

    def get_column(self, column_name):
        return {
            "column_name": column_name,
            "data": self.dataset[column_name]
        }

    def get_column_names(self):
        return self.column_names

    def get_rowcount(self):
        return len(self.rows)

    def get_column_types(self):
        return self.column_types

    def get_numeric_column_names(self):
        colnames = self.column_names
        return [name for idx, name in enumerate(colnames) if self.column_types[idx] != 'str']

    def get_nonnumeric_column_names(self):
        numeric_cols = self.get_numeric_column_names()
        return [colname for colname in self.column_names if colname not in numeric_cols]

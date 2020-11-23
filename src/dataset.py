from misc.convert_to import convert_to
from misc.guess_datatype import guesstype


class Dataset:
    def __init__(self, rows):
        self.rows = rows
        self.dataset = None
        self.columnstore = {}
        self.column_names = None
        self.column_types = []

    def create(self, has_header=True):

        self.column_names = ['col'+str(idx)
                             for idx in range(0, len(self.rows[0]))]
        if has_header:
            self.column_names = self.rows.pop(0)

        columnstore = [[] for header in self.column_names]

        for row in self.rows:
            for column_idx in range(0,len(self.column_names)):
                columnstore[column_idx].append(row[column_idx])

        self.dataset = {}

        for column_idx, column in enumerate(columnstore):

            guessingrows = 5
            if guessingrows > len(column)-1:
                guessingrows = len(column)-1

            coltype = guesstype(column[0:guessingrows])
            self.column_types.append(coltype)

            self.dataset[self.column_names[column_idx]
                         ] = convert_to(column, coltype)

    def get_column(self, column_name):
        return self.dataset[column_name]

    def get_column_names(self):
        return self.column_names

    def get_column_types(self):
        return self.column_types

    def get_numeric_column_names(self):
        colnames = self.column_names
        return [name for idx, name in enumerate(colnames) if self.column_types[idx] != 'str']

    def get_nonnumeric_column_names(self):
        numeric_cols = self.get_numeric_column_names()
        return [colname for colname in self.column_names if colname not in numeric_cols]

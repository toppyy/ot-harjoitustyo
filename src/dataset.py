from misc.convert_to import convert_to
from misc.guess_datatype import guesstype


class Dataset:
    def __init__(self,reader):
        self.reader = reader
        self.dataset  = None
        self.columnstore = {}
        self.column_names = None
        self.column_types = []

    def create(self,has_header=True):


        if has_header:
            headers = self.reader.__next__()

            self.column_names = headers
            

        columnstore = [[] for header in headers]

        for row in self.reader:
            for column_idx,header in enumerate(headers):
                columnstore[column_idx].append(row[column_idx])


        self.dataset = {}

        for column_idx,column in enumerate(columnstore):

            guessingrows = 5
            if guessingrows > len(column)-1:
                guessingrows = len(column)-1

            coltype = guesstype(column[0:guessingrows])
            self.column_types.append(coltype)

            self.dataset[headers[column_idx]] = convert_to(column, coltype)

        
    def get_column(self,column_name):
        return self.dataset[column_name]

    def get_column_names(self):
        return self.column_names

    def get_numeric_column_names(self):
        return [colname for idx,colname in enumerate(self.column_names) if self.column_types[idx] != 'str' ]

    def get_nonnumeric_column_names(self):
        numeric_cols = self.get_numeric_column_names()
        return [colname for colname in self.column_names if colname not in numeric_cols]

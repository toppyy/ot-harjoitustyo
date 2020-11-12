import csv
import re


class FileAccess:

    def guesstype(self, datapart):

        obs = datapart[0]  # Guess from one obs

        if re.match('[^0-9.,]', obs) is not None:
            return 'str'

        if re.match('[^0-9]', obs) is not None:
            return 'float'

        if re.match('[0-9]+', obs) is not None:
            return 'int'

        return 'str'

    def convert_to(self, data, coltype):

        if coltype == 'int':
            return [int(obs) for obs in data]

        if coltype == 'float':
            return [float(obs) for obs in data]

        return data

    def read_csv(self, path, delimiter, quote, has_header):

        csvfile = open(path, 'r', encoding='ISO-8859-1')

        try:
            reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quote)

            if has_header:
                headers = reader.__next__()
            #else:
                # Read first line to get number of columns
            #    headers = 

            columnstore = [[] for header in headers]

            for row in reader:
                for column_idx,header in enumerate(headers):
                    columnstore[column_idx].append(row[column_idx])

        except FileExistsError:
            print('File does not exist')

        dataset = {}

        for column_idx,column in enumerate(columnstore): #range(0, len(columnstore)):

            guessingrows = 5
            if guessingrows > len(column)-1:
                guessingrows = len(column)-1

            coltype = self.guesstype(column[0:guessingrows])

            dataset[headers[column_idx]] = self.convert_to(column, coltype)

        return dataset

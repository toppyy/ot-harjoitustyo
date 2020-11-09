import csv
import re

class FileAccess:

    def guesstype(self,datapart):

        obs = datapart[0] # Guess from one obs

        if re.match('[^0-9.,]',obs) is not None:
            return 'str'

        if re.match('[^0-9]',obs)   is not None:
            return 'float'

        if re.match('[0-9]+',obs)   is not None:
            return 'int'

        return 'str'

    def convert_to(self,data,coltype):

        if coltype=='int':
            return [int(obs) for obs in data]

        if coltype=='float':
            return [float(obs) for obs in data]

        return data

    def read_csv(self,path,delimiter,quote,header):

        csvfile = open(path,'r',encoding='ISO-8859-1')
        try:
            reader = csv.reader(csvfile,delimiter=delimiter,quotechar=quote)

            if header:
                headers = reader.__next__()

            headercount = len(headers)

            columnstore = [[] for header in headers ]

            for row in reader:
                for column_idx in range(0,headercount):
                    columnstore[column_idx].append(row[column_idx])

        except Exception as error:
            print('Problem reading the file:',error)

        dataset = {}

        for column_idx in range(0,len(columnstore)):

            column = columnstore[column_idx]

            guessingrows = 5
            if guessingrows > len(column)-1:
                guessingrows = len(column)-1

            coltype = self.guesstype(column[0:guessingrows])

            dataset[headers[column_idx]] = self.convert_to(column,coltype)

        return dataset

import csv
import re


class FileAccess:


    def read_csv(self, path, delimiter, quote):

        csvfile = open(path, 'r', encoding='ISO-8859-1')

        try:
            reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quote)

            return reader

        except FileExistsError:
            print('File does not exist')


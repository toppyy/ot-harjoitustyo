import csv
from tkinter import messagebox

class FileAccess:

    def read_csv(self, path, delimiter, quote='"', row_limit=None):

        csvfile = open(path, 'r', encoding='ISO-8859-1')

        try:
            reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quote)

            rows = []
            row_count = 0
            for row in reader:
                row_count = row_count + 1
                rows.append(row)
                if row_limit is not None and row_count is row_limit:
                    break

            if len(rows) == 0:
                raise Exception('File is empty')

            return rows

        except Exception as err:
            error_msg = 'Error reading file: {}.\n\nNo data loaded.'.format(str(err))
            messagebox.showerror(message=error_msg)

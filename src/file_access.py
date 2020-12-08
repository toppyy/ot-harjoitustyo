import csv

class FileAccess:
    """Class that provides access to the file system
    """

    def read_csv(self, path, delimiter, quote='"', row_limit=None, gui=None):
        """Reads a csv-file into a list

        Args:
            path: Path of the file
            delimiter: Delimiter of the file
            quote: The character used for quoting in the file. Defaults to '"'.
            row_limit: A limit for rows to read. If None all are read. Defaults to None.
            gui: Reference to the gui calling the method. Defaults to None.

        Raises:
            Exception: Errors related to reading the file

        Returns:
            List: A list of rows in the dataset
        """

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
            if gui is not None:
                error_msg = 'Error reading file: {}.\n\nNo data loaded.'.format(str(err))
                gui.show_error(error_msg)

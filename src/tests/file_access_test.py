import unittest
from file_access import read_csv


class TestFileAccess(unittest.TestCase):

    def test_csv_read(self):

        path = './data/iris.csv'
        rows = read_csv(path, ";", '"')

        first_row = 'Sepal.Length;Sepal.Width;Petal.Length;Petal.Width;Species'

        self.assertEqual(first_row,';'.join(rows[0]))

    def test_csv_read_rowlimit(self):

        rows_to_read = 12

        path = './data/iris.csv'
        rows = read_csv(path, ";", '"', row_limit=12)

        self.assertEqual(rows_to_read, len(rows))

import unittest
from dataset import Dataset
from file_access import read_csv
from test_helpers.pseudo_gui import PseudoGUI

class TestDataset(unittest.TestCase):

    def setUp(self):
        path = './data/iris.csv'
        self.rows = read_csv(path, ";", '"')
        self.dataset = Dataset(  self.rows  )
        self.dataset.gui = PseudoGUI()

    def test_dataset_creation(self):

        dataset = self.dataset
        dataset.create(has_header=True)

        rowcount = dataset.get_rowcount()

        self.assertEqual(rowcount, 150)

    def test_dataset_creation_without_headers(self):

        dataset = self.dataset
        dataset.create(has_header=False)

        rowcount = dataset.get_rowcount()

        self.assertEqual(rowcount, 151)


    def test_column_sets(self):

        self.dataset.create(has_header=True)
        columns             = self.dataset.get_column_names()
        nonnumeric_columns  = self.dataset.get_nonnumeric_column_names()
        numeric_columns     = self.dataset.get_numeric_column_names()

        numeric_columns.extend(nonnumeric_columns)
        self.assertSetEqual(set(columns),set(numeric_columns))

    def test_nonnumeric_columns(self):

        self.dataset.create(has_header=True)
        nonnumeric_columns  = self.dataset.get_nonnumeric_column_names()
        self.assertEqual(['Species'], nonnumeric_columns)


    def test_convert_to_works(self):

        result_of_conversion = self.dataset.convert_to(['10.7','5','2.1'],'float','test_column')

        self.assertEqual([10.7,5.0,2.1],result_of_conversion['data'])
        self.assertEqual('float',result_of_conversion['coltype'])

    def test_convert_to_falls_to_str(self):

        result_of_conversion = self.dataset.convert_to(['10.7','5x','2.1'],'float','test_column')

        self.assertEqual(['10.7','5x','2.1'],result_of_conversion['data'])
        self.assertEqual('str',result_of_conversion['coltype'])

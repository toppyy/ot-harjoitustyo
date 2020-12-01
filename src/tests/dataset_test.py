import unittest
from dataset import Dataset
from file_access import FileAccess



class TestDataset(unittest.TestCase):

    def setUp(self):
        path = './data/tyovoimakunnittain.csv'
        self.rows = FileAccess().read_csv(path, ";", '"')
        self.dataset = Dataset(  self.rows  )

    def test_dataset_creation(self):
        
        dataset = self.dataset
        dataset.create(has_header=True)

        rowcount = dataset.get_rowcount()

        self.assertEqual(rowcount, 310)

    def test_dataset_creation_without_headers(self):
        
        dataset = self.dataset
        dataset.create(has_header=False)

        rowcount = dataset.get_rowcount()

        self.assertEqual(rowcount, 311)


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
        self.assertEqual(['alue'], nonnumeric_columns)
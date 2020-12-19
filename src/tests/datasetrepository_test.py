import unittest
from dataset_repository import DatasetRepository
from misc.db_connection import get_database_connection

connection = get_database_connection()
dataset_repo = DatasetRepository(connection)


class TestDatasetRepository(unittest.TestCase):

    def setUp(self):
        self.dataset_repo = dataset_repo
        self.dataset_repo.delete_all()

    def test_store_to_repository_works(self):


        filename = "/path/to/csv_file.csv"

        for i in range(0,6):
            id_insert = self.dataset_repo.store_dataset_parameters({ "filename": filename } )

        datasets = self.dataset_repo.get_all()

        self.assertEqual(6,len(datasets))

    def test_id_is_incremented(self):


        filename = "/path/to/csv_file.csv"
        id1 = self.dataset_repo.store_dataset_parameters({ "filename": filename } )
        id2 = self.dataset_repo.store_dataset_parameters({ "filename": filename } )

        self.assertGreater(id2,id1)


    def test_get_from_repository_works(self):

        filename = "/path/to/csv_file.csv"
        id_of_inserted_row = self.dataset_repo.store_dataset_parameters({ "filename": filename } )

        dataset_params = self.dataset_repo.get_dataset_parameters(id_of_inserted_row)
        self.assertEqual(filename,dataset_params['filename'])

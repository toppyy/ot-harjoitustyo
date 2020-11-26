import unittest
from file_access import FileAccess


class TestFileAccess(unittest.TestCase):

    def test_csv_read(self):

        path = './data/sepelvaltimo_korvausoikeus.csv'
        rows = FileAccess().read_csv(path, ";", '"')

        first_row = 'aluekoodi;maakunta;vaesto65_84;sepelvaltimotauti_korv_oikeus;sepelvaltimotauti_korv_oikeus_osuus'
        
        self.assertEqual(first_row,';'.join(rows[0]))

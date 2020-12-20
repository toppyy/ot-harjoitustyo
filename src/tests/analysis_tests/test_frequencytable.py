import unittest
from analyses.frequencytable import frequencytable
from test_helpers.create_testdata import get_testdata_as_dataset

class TestFrequencytable(unittest.TestCase):

    def setUp(self):
        self.testdata = get_testdata_as_dataset()
        self.testcolumn = self.testdata.get_column('col1')


    def test_frequencytable_count(self):

        freqtable = frequencytable(self.testcolumn)

        number_of_aletter_a = freqtable[1][1]

        self.assertEqual(10, number_of_aletter_a)

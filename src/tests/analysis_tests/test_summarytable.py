import unittest
from analyses.summarytable import summarytable
from test_helpers.create_testdata import get_testdata_as_dataset

class TestSummarytable(unittest.TestCase):

    def setUp(self):
        self.testdata = get_testdata_as_dataset()
        self.numbers = self.testdata.get_column('col0')
        self.group_by = self.testdata.get_column('col1')


    def test_summarytable_works_as_expected(self):

        result = summarytable(self.group_by,self.numbers)

        stats = result[0]

        self.assertEqual('A',stats[0])                     # Group value
        self.assertEqual(10, stats[1])                     # Count
        self.assertAlmostEqual(61.58, stats[2], places=2)  # Mean
        self.assertAlmostEqual(59.2,  stats[3], places=1)  # Median

import unittest
from analyses.summary import summary
from test_helpers.create_testdata import get_testdata_as_dataset

class TestSummary(unittest.TestCase):

    def setUp(self):
        self.testdata = get_testdata_as_dataset()
        self.testcolumn = self.testdata.get_column('col0')


    def test_summary_works_as_expected(self):

        summaryresult = summary(self.testcolumn)

        median = summaryresult[0]
        mean   = summaryresult[1]
        stdev  = summaryresult[2]

        decimals = 2

        self.assertAlmostEqual(54.67, mean, places=decimals)
        self.assertAlmostEqual(53.0 , median, places=decimals)
        self.assertAlmostEqual(16.87, stdev, places=decimals)

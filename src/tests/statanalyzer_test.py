import unittest
from stat_analyzer import StatAnalyzer
from dataset import Dataset
from test_helpers.pseudo_gui import PseudoGUI
from analyses_config import get_analyses_config

# Helper to create data for testing
def letter(i):

    if i % 2 == 0:
        return 'A'
    return 'B'

class TestStatAnalyzer(unittest.TestCase):

    def setUp(self):
        testcolumn = [40.8, 21.7, 50, 67, 42, 35.5, 90.7, 62.1, 74.7,
              39.5, 56.7, 47.2, 61.7, 52.2, 68.9, 53.8, 81.7, 37.1, 48.6, 61.5]

        testdata = [[str(val),letter(i)] for i,val in enumerate(testcolumn)]
        testdataset = Dataset(testdata)
        testdataset.create(has_header=False)

        self.stat_analyzer = StatAnalyzer(testdataset)
        self.stat_analyzer.set_gui(PseudoGUI())

        self.analyses = get_analyses_config()

    def test_summary(self):

        summaryresult = self.stat_analyzer.analyse(self.analyses['summary'],["col0"])

        median = summaryresult[0]
        mean   = summaryresult[1]
        stdev  = summaryresult[2]

        decimals = 2

        self.assertAlmostEqual(54.67, mean, places=decimals)
        self.assertAlmostEqual(53.0 , median, places=decimals)
        self.assertAlmostEqual(16.87, stdev, places=decimals)

    def test_frequencytable_count(self):

        freqtable = self.stat_analyzer.analyse(self.analyses['freqtable'],["col1"])

        number_of_aletter_a = freqtable[1][1]

        self.assertEqual(10, number_of_aletter_a)


    def test_summarytable(self):

        summarytable = self.stat_analyzer.analyse(self.analyses['summarytable'],["col1","col0"])

        stats = summarytable[0]

        self.assertEqual('A',stats[0])                     # Group value
        self.assertEqual(10, stats[1])                     # Count
        self.assertAlmostEqual(61.58, stats[2], places=2)  # Mean
        self.assertAlmostEqual(59.2,  stats[3], places=1)  # Median

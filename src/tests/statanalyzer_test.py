import unittest
from stat_analyzer import StatAnalyzer
from dataset import Dataset


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

        


    def test_summary(self):

        summaryresult = self.stat_analyzer.summary("col0")

        mean   = list(filter(lambda r: r['id'] == 'mean', summaryresult))[0]
        median = list(filter(lambda r: r['id'] == 'median', summaryresult))[0]
        stdev  = list(filter(lambda r: r['id'] == 'stddev', summaryresult))[0]

        self.assertEqual(mean["value"], 54.67)
        self.assertEqual(median["value"], 53.8)
        self.assertAlmostEqual(stdev["value"],16.87019,places=5)

    def test_frequency_table(self):

        freqtable = self.stat_analyzer.frequencytable("col1")

        numberOfAs = freqtable[0]

        # TODO: better way to test this
        self.assertEqual(numberOfAs['value'][0:5],'A: 10')

import unittest
from stat_analyzer import StatAnalyzer
from dataset       import Dataset


testcolumn = [40.8, 21.7, 50, 67, 42, 35.5, 90.7, 62.1, 74.7, 39.5, 56.7, 47.2, 61.7, 52.2, 68.9, 53.8, 81.7, 37.1, 48.6, 61.5]
testdata   = [[str(x)] for x in testcolumn]

testdataset = Dataset(testdata)

testdataset.create(has_header=False)




class TestStatAnalyzer(unittest.TestCase):

    def setUp(self):
        self.stat_analyzer = StatAnalyzer(testdataset)


    def test_summary(self):

        summaryresult = self.stat_analyzer.summary("col0")

        mean    = list( filter(lambda r: r['text']=='Mean: ', summaryresult) )[0]
        median  = list( filter(lambda r: r['text']=='Median: ', summaryresult) )[0]


        self.assertEqual(mean["value"], 54.67)
        self.assertEqual(median["value"], 53.8)

    
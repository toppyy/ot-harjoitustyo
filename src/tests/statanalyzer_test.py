import unittest
from stat_analyzer import StatAnalyzer

testdata = {
    "column": [40.8, 21.7, 50, 67, 42, 35.5, 90.7, 62.1, 74.7, 39.5, 56.7, 47.2, 61.7, 52.2, 68.9, 53.8, 81.7, 37.1, 48.6, 61.5]
}


class TestStatAnalyzer(unittest.TestCase):

    def setUp(self):
        self.stat_analyzer = StatAnalyzer(testdata)

    def test_mean(self):
        self.assertEqual(self.stat_analyzer.mean("column"), 54.67)

    def test_max(self):
        self.assertEqual(self.stat_analyzer.max("column"), 90.7)

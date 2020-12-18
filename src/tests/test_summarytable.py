import unittest

from analyses.summarytable import summarytable
from test_helpers.pseudo_gui import PseudoGUI


class TestSummarytable(unittest.TestCase):

    def setUp(self):
        self.groups = {
            "data": ['A','B','A','C','B','A','A'],
            "column_name": "letters"
        }
        self.numbers = {
            "data": [34,12,55,2,9,43.2,25.6],
            "column_name": "numbers"
        }


    def test_summarytable_works(self):

        table = summarytable(self.groups, self.numbers)
        stats = table[0]

        self.assertEqual('A',stats[0])                     # Group value
        self.assertEqual(4, stats[1])                      # Count
        self.assertAlmostEqual(39.4,  stats[2], places=1)  # Mean
        self.assertAlmostEqual(38.6,  stats[3], places=1)  # Median


    def test_summarytable_dimensions(self):

        table = summarytable(self.groups, self.numbers)

        self.assertEqual(3,len(table))
        self.assertEqual(4,len(table[0]))

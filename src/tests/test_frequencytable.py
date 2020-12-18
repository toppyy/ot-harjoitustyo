import unittest

from analyses.frequencytable import frequencytable
from test_helpers.pseudo_gui import PseudoGUI


class TestFrequencytable(unittest.TestCase):

    def setUp(self):
        self.column = {
            "data": ['A','B','A','C','B','A','A'],
            "column_name": "letters"
        }

    def test_freqtable_works(self):

        table = frequencytable(self.column)
        self.assertEqual(4,table[0][1])


    def test_frequencytable_dimensions(self):

        table = frequencytable(self.column)

        self.assertEqual(3,len(table))
        self.assertEqual(2,len(table[0]))

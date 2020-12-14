import unittest

from analyses.frequencytable import frequencytable
from test_helpers.pseudo_gui import PseudoGUI


class TestFrequencytable(unittest.TestCase):

    def setUp(self):
        self.gui = PseudoGUI()

    def test_freqtable_works(self):

        column = {
            "data": ['A','B','A','C','B','A','A'],
            "column_name": "letters"
        }

        result = frequencytable(column)

        header = result[0]
        table  = result[1]

        self.assertEqual(4,len(table))
        self.assertEqual(4,table[1][1])
        self.assertEqual('letters',header)

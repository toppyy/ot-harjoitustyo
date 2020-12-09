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

        result = frequencytable(column,self.gui)
        table  = result[1].get_output(master_to_be=None,row_idx=0)
        header = result[0]
        # size is:
        #  2 cells for headers
        #  2 * 3 (distinct values in data)
        #  8

        self.assertEqual(8,len(table))
        self.assertEqual('4',table[3].get())
        self.assertEqual('letters',header.get_text())

    def test_large_freqtable_raises_questions(self):

        column = {
            "data": range(0,201),
            "column_name": "too much letters"
        }

        frequencytable(column,self.gui)
        args = self.gui.get_method_call_args()

        self.assertIn('Are you sure',args)

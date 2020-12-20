import unittest
from analyses.barplot import barplot
from test_helpers.pseudo_plt import PseudoPlt

class TestBarplot(unittest.TestCase):

    def setUp(self):
        self.plt = PseudoPlt()

        self.to_plot =  {
            "data": ['A','B','A','C','B','A','A'],
            "column_name": "test"
        }


    def test_bar_is_called(self):

        barplot(self.to_plot,self.plt)

        arguments_for_bar_method = self.plt.get_method_call_args()

        self.assertIsNotNone(arguments_for_bar_method)

    def test_bar_is_called_with_correct_args(self):

        barplot(self.to_plot,self.plt)

        arguments_for_bar_method = self.plt.get_method_call_args()

        self.assertEqual(['A','B','C'],arguments_for_bar_method[0])
        self.assertEqual([4,2,1],arguments_for_bar_method[1])

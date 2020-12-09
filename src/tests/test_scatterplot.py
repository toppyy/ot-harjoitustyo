import unittest
from analyses.scatterplot import scatterplot
from test_helpers.pseudo_plt import PseudoPlt

class TestBarplot(unittest.TestCase):

    def setUp(self):
        self.plt = PseudoPlt()

        self.to_plot_A =  {
            "data": [1,2,3,4],
            "column_name": "test"
        }
        self.to_plot_B =  {
            "data": [987,872,442,765],
            "column_name": "test"
        }



    def test_bar_is_called(self):

        scatterplot(self.to_plot_A,self.to_plot_B,self.plt)

        arguments_for_scatter_method = self.plt.get_method_call_args()

        self.assertIsNotNone(arguments_for_scatter_method)

    def test_bar_is_called_with_correct_args(self):

        scatterplot(self.to_plot_A,self.to_plot_B,self.plt)

        arguments_for_scatter_method = self.plt.get_method_call_args()

        self.assertEqual([1,2,3,4],arguments_for_scatter_method[0])
        self.assertEqual([987,872,442,765],arguments_for_scatter_method[1])

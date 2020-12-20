import unittest

from analyses.linear_regression import linear_regression


class TestLinearRegression(unittest.TestCase):

    def setUp(self):
        self.column1 = {
            "data": [34,12,55,2,9,43.2,25.6]
        }
        self.column2 = {
            "data": [43,22.2,98,65,2,39,20]
        }


    def test_linear_regression_output_is_correct(self):

        slope, intercept, r_value, p_value, std_err  = linear_regression(self.column1,self.column2)



        self.assertAlmostEqual(slope,0.3243,places=3)
        self.assertAlmostEqual(intercept,12.43,places=2)
        self.assertAlmostEqual(r_value,0.2858,places=4)
        self.assertAlmostEqual(p_value,0.2163,places=4)
        self.assertAlmostEqual(std_err,0.2293,places=3)

import unittest

from analyses.varianceanalysis import varianceanalysis


class TestVarianceanalysis(unittest.TestCase):

    def setUp(self):
        groups = {
            "data": ['A','B','A','C','B','A','A'],
            "column_name": "letters"
        }
        numbers = {
            "data": [34,12,55,2,9,43.2,25.6],
            "column_name": "numbers"
        }

        self.result = varianceanalysis(groups,numbers)


    def test_f_statistic_is_correct(self):

        f_statistic = self.result[4]

        self.assertAlmostEqual(7.387,f_statistic, places=3)

    def test_p_value_is_correct(self):

        p_value = self.result[5]

        self.assertAlmostEqual(0.0454,p_value, places=3)

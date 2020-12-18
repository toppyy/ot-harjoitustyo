import unittest

from analyses.ttest import ttest


class TestTtest(unittest.TestCase):

    def setUp(self):

        self.numbers = {
            "data": [
                16.3695, 12.6063, 9.9329, 9.3255, 2.868, 9.3223, 9.7281, 18.4413, 
                8.2986, 13.1218, 9.6179, 14.0348, 10.6131, 13.6631, 6.1472, 4.8914, 
                10.2277, 6.2954, 9.1971, 3.9139
            ],
            "column_name": "numbers"
        }


    def test_t_statistic_is_correct(self):

        result = ttest(self.numbers, 10.5)

        t_statistic = result[2]

        self.assertAlmostEqual(-0.6346,t_statistic, places=3)

    def test_p_value_is_correct_when_larger(self):

        result = ttest(self.numbers, 10.5)
        p_value = result[3]

        self.assertAlmostEqual(0.5332,p_value, places=3)

    def test_p_value_is_correct_when_smaller(self):

        result = ttest(self.numbers, 9.5)
        p_value = result[3]

        self.assertAlmostEqual(0.6365,p_value, places=3)

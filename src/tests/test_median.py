import unittest
from math_helper.median import median


class TestMedian(unittest.TestCase):

    def setUp(self):
        pass

    def test_even_set(self):

        numbers = [40.8, 21.7, 50, 67, 42, 35.5, 90.7, 62.1, 74.7,
              39.5, 56.7, 47.2, 61.7, 52.2, 68.9, 53.8, 81.7, 37.1, 48.6, 61.5]

        self.assertEqual( 53 , median(numbers) )


    def test_uneven_set(self):

        problem2 = [40.8, 21.7, 50, 67, 42, 35.5, 90.7, 62.1, 74.7]

        self.assertEqual( 50 , median(problem2) )

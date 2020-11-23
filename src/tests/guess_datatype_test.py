import unittest
from misc.guess_datatype import guesstype


class TestGuesstype(unittest.TestCase):

    def setUp(self):
        pass


    def test_guesstype(self):
        self.assertEqual( guesstype(['10.7']) , 'float' )
        self.assertEqual( guesstype(['107a']) , 'str' )
        self.assertEqual( guesstype(['1099128']) , 'int' )
import unittest
from misc.convert_to import convert_to


class TestConvertTo(unittest.TestCase):

    def setUp(self):
        pass

    def test_convert_to_works(self):

        conversion1 = convert_to(['10.7','1'],'float')
        self.assertEqual(conversion1, [10.7,1])

        conversion2 = convert_to(['10.7',1],'int')
        self.assertEqual(conversion2, [10,1])

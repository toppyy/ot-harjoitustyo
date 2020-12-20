import unittest
from stat_analyzer import StatAnalyzer
from dataset import Dataset
from analyses_config import get_analyses_config
from test_helpers.create_testdata import get_testdata_as_dataset

class ArgumentCollector:

    def __init__(self,arguments):
        self.arguments = arguments


    def get_args(self):
        return self.arguments

def empty_function(*args):
    return args

class TestStatAnalyzer(unittest.TestCase):

    def setUp(self):
        self.testdataset = get_testdata_as_dataset()

        self.stat_analyzer = StatAnalyzer(self.testdataset)

        self.analyses = get_analyses_config()

        # Add pseudo analysis
        self.pseudo_analysis = {
            'displayname': 'A name',
            'setup': empty_function,
            'analyse': empty_function
        }


    def test_analyse_is_called_with_correct_arguments(self):

        result = self.stat_analyzer.analyse(self.pseudo_analysis,['col1'])


        print(result)

        self.assertEqual(self.testdataset.get_column('col1'),result[0])

    def test_analyse_is_called_multiple_correct_arguments(self):

        additional_parameter = 123.6

        result = self.stat_analyzer.analyse(self.pseudo_analysis,['col1'],additional_parameter)

        self.assertEqual(
            (self.testdataset.get_column('col1'),additional_parameter)
            ,
            result
        )

    def test_analyzer_knows_it_does_not_have_data(self):

        analyzer = StatAnalyzer()

        self.assertFalse(analyzer.has_dataset())

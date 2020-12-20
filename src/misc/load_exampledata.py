from file_access import read_csv
from dataset import Dataset


def load_exampledata():
    """Reads the example data

    Returns:
        Dataset
    """
    path = './data/iris.csv'
    data = Dataset(read_csv(path,";"))
    data.create()
    return data

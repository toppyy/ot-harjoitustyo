from file_access import FileAccess
from dataset import Dataset


def load_exampledata(gui=None):
    path = './data/iris.csv'
    data = Dataset(FileAccess().read_csv(path,";"))
    data.create()
    return data

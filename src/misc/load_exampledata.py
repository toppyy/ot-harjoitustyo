from file_access import FileAccess
from dataset import Dataset


def load_exampledata(gui=None):
    path = './data/sepelvaltimo_korvausoikeus.csv'
    data = Dataset(FileAccess().read_csv(path,";"))
    data.create(gui=gui)

    return data

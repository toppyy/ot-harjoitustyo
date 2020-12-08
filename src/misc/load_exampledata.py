from file_access import FileAccess
from dataset import Dataset


def load_exampledata(gui=None):
    path = './data/sepelvaltimo_korvausoikeus.csv'
    data = Dataset(FileAccess().read_csv(path,";",gui=gui))
    data.create(gui=gui)

    return data

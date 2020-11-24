from file_access import FileAccess
from dataset import Dataset


def load_exampledata():


    path = './data/sepelvaltimo_korvausoikeus.csv'
    data = Dataset(FileAccess().read_csv(path, ";", '"'))
    data.create()

    return data

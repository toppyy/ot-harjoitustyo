from file_access import FileAccess
from dataset import Dataset


def load_exampledata():

    data = Dataset(FileAccess().read_csv(
        './data/sepelvaltimo_korvausoikeus.csv', ";", '"'))
    data.create()

    return data

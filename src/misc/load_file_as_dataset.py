from file_access import FileAccess
from dataset import Dataset


def load_file_as_dataset(path):

    data = Dataset(FileAccess().read_csv(path, ";", '"'))
    data.create(has_header=True)

    return data


def load_exampledata():
    return load_file_as_dataset('./data/sepelvaltimo_korvausoikeus.csv')

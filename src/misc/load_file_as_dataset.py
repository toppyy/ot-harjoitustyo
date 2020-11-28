from file_access import FileAccess
from dataset import Dataset


def load_file_as_dataset(path, delimiter=";", quote='"', has_header=True, row_limit=None):

    data = Dataset(FileAccess().read_csv(path, delimiter, quote, row_limit))
    data.create(has_header=has_header)

    return data


def load_exampledata():
    return load_file_as_dataset('./data/sepelvaltimo_korvausoikeus.csv')

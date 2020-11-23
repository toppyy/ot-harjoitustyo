from file_access import FileAccess
from dataset import Dataset

def load_exampledata():

    data = Dataset( FileAccess().read_csv('./data/tyovoimakunnittain.csv', ";", '"') )
    data.create()

    return data
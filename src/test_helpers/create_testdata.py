from dataset import Dataset

# Helper to create data for testing
def letter(i):

    if i % 2 == 0:
        return 'A'
    return 'B'


def get_testnumbers():
    return [40.8, 21.7, 50, 67, 42, 35.5, 90.7, 62.1, 74.7,
            39.5, 56.7, 47.2, 61.7, 52.2, 68.9, 53.8, 81.7, 37.1, 48.6, 61.5]



def get_testdata():
    testnumbers = get_testnumbers()
    testdata = [[str(val),letter(i)] for i,val in enumerate(testnumbers)]

    return testdata


def get_testdata_as_dataset():

    testdataset = Dataset(get_testdata())
    testdataset.create(has_header=False)

    return testdataset
        
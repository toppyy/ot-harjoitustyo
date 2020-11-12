import re


class StatAnalyzer:

    def __init__(self, dataset=None):
        self.dataset = dataset

    def set_dataset(self, dataset):
        self.dataset = dataset

    def call(self, functioncall):

        function = functioncall[0]
        column = functioncall[1]

        # Functions that dont require a column
        if function == 'head':
            return self.head(column)

        if function == 'help':
            return self.help()

        if not column in self.dataset:
            print('Column not in dataset.')
            return ''

        if function == "mean":
            return self.mean(column)

        if function == "median":
            return self.median(column)

        if function == "max":
            return self.max(column)

        if function == "min":
            return self.min(column)

    def head(self, obs=''):

        if obs is not None and re.match('[^0-9]', obs) is None:
            obs = int(obs)
        else:
            obs = 5

        headerset = self.dataset.copy()

        for key in headerset:

            if len(headerset[key]) < obs:
                obs = len(headerset[key])-1

            headerset[key] = headerset[key][0:obs]

        return headerset

    def mean(self, column):
        data = self.dataset[column]
        return sum(data)/len(data)

    def median(self, column):

        data = self.dataset[column]
        data = sorted(data)

        midpoint = len(data) // 2

        return data[midpoint]

    def max(self, column):
        return max(self.dataset[column])

    def min(self, column):
        return min(self.dataset[column])

    def help(self):
        helpstr = "List of available commands:"

        helpstr = helpstr + \
            '\n -'.join(['', 'mean', 'median', 'min', 'max', 'head', 'help'])

        return helpstr

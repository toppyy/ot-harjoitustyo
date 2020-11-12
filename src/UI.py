import re
from file_access import FileAccess


class UI:

    def __init__(self, StatAnalyzer):
        self.stat_analyzer = StatAnalyzer
        self.file_access_object = FileAccess()

    def start(self):

        while True:

            commandinput = input(
                "Enter function and column (eg. mean(tyovoima)): ")

            if commandinput == '':
                break

            # Finds function call and parameter
            pattern = r'([a-z]+)\(([^\)]+)?\)'

            function_call = re.match(pattern, commandinput, re.IGNORECASE)

            if function_call is None:
                print("Invalid command")
                continue

            function = function_call.groups()

            if function[0] == "readCSV":
                data = self.read_csv(function[1])
                self.stat_analyzer.set_dataset(data)

            else:
                print(self.stat_analyzer.call(function))

    def read_csv(self, path, delimiter=";", quote='"', header=True):

        return self.file_access_object.read_csv(path, delimiter, quote, header)

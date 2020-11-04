import re
from FileAccess import FileAccess
class UI:

    def __init__(self,StatAnalyzer):
        self.StatAnalyzer = StatAnalyzer
        self.FAO          = FileAccess()


    def start(self):

        while True:

            commandinput = input("Enter function and column (eg. mean(tyovoima)): ")
            
            if commandinput == '':
                break
            
            # Finds function call and parameter
            pattern = '([a-z]+)\(([^\)]+)?\)'

            functionMatch = re.match(pattern,commandinput, re.IGNORECASE)

            if functionMatch == None:
                print("Invalid command")
                continue

            function = functionMatch.groups()

            if function[0] == "readCSV":
                data = self.readCSV(function[1])
                self.StatAnalyzer.setDataset( data )

            else:
                print( self.StatAnalyzer.call(function) )



    def readCSV(self,path,delimiter=";",quote='"',header=True):
        return self.FAO.readCSV(path,delimiter,quote,header)

            

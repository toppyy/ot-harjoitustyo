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
            
            pattern = '([a-z]+)\(([^\)]+)\)'

            function = re.match(pattern,commandinput, re.IGNORECASE).groups()


            if function[0] == "r":
                self.StatAnalyzer.setDataset( self.readCSV(function[1]) )

            else:
                print( self.StatAnalyzer.call(function) )



    def readCSV(self,path,delimiter=";",quote='"',header=True):
        self.FAO.readCSV(path,delimiter,quote,header)

            

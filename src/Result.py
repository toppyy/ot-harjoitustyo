

class Result:

    def __init__(self,regexResult):
        self.regexResult = regexResult

    def getMatches(self):
        
        return self.regexResult.group()


    def printResults(self):

        if self.regexResult == None:
            print('There was no match.')

        groups = self.regexResult.group()
        
        print("Matching group(s): {}".format(groups))

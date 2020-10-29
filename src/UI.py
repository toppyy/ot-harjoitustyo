

class UI:

    def __init__(self,regtester):
        self.regtester = regtester


    def start(self):

        while True:

            regex = input("Enter regular expression: ")
            
            if regex=="":
                break

            teststr = input("Enter string to test against: ")

            result = self.regtester.test(regex,teststr)
            
            result.printResults()


            

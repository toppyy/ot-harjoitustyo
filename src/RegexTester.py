import re
from Result import Result

class RegexTester:


    def test(self,regex,teststr):

        return Result(re.search(regex,teststr))
    
    

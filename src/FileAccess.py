import csv
import re

class FileAccess:

    def guesstype(self,datapart):

        obs = datapart[0] # Guess from one obs

        if re.match('[^0-9.,]',obs) != None:
            return 'str'

        if re.match('[^0-9]',obs)   != None:
            return 'float'

        if re.match('[0-9]+',obs)   != None:
            return 'int'

        return 'str'

    def convertTo(self,data,coltype):

        if coltype=='int':
            return [int(obs) for obs in data]
            
        if coltype=='float':
            return [float(obs) for obs in data]

        return data

    def readCSV(self,path,delimiter,quote,header):

        csvfile = open(path,'r',encoding='ISO-8859-1')
        try:
            reader = csv.reader(csvfile,delimiter=delimiter,quotechar=quote)
            
            if header:
                headers = reader.__next__()

            headercount = len(headers)

            columnstore = [[] for header in headers ]

            for row in reader:
                for c in range(0,headercount):
                    columnstore[c].append(row[c])  

        except Exception as e:
            print('Problem reading the file:',e)
            
        dataset = {}

        for c in range(0,len(columnstore)):

            column = columnstore[c]

            guessingrows = 5
            if guessingrows > len(column)-1:
                guessingrows = len(column)-1

            coltype = self.guesstype(column[0:guessingrows]) 
        
            dataset[headers[c]] = self.convertTo(column,coltype)
        
        return dataset

            
 

        
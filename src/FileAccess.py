import csv


class FileAccess:

    def readCSV(self,path,delimiter,quote,header):

        csvfile = open('./data/tyovoimakunnittain.csv','r',encoding='ISO-8859-1')
        try:
            reader = csv.reader(csvfile,delimiter=delimiter,quotechar=quote)
            
            if header:
                headers = reader.__next__()

            headercount = len(headers)

            columnstore = [[] for header in headers ]
            
            for row in reader:
                for c in range(0,headercount):
                    columnstore[c].append(row[c])                

            dataset = {}
            for c in range(0,headercount):
                dataset[headers[c]] = columnstore[c] 

            return dataset
            
        except Exception as e:
            print('Problem reading the file:',e)
            return


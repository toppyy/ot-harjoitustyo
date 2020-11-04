

class StatAnalyzer:


    #def __init__(self,dataset):
    #   self.dataset = dataset

    def setDataset(self,dataset):
        self.dataset = dataset
        print("Dataset set.")
        return

    def call(self,functioncall):

        function = functioncall[0]
        column   = functioncall[1]

        if function == "mean":
            return self.mean(column)

        if function == "median":
            return self.median(column)

    def headers(self):
        print(self.dataset)


    def mean(self,column):
        d = self.dataset[column]
        return sum(d)/len(d) 


    def median(self,column):

        d = self.dataset[column]
        d = sorted(d)

        midpoint = len(d) // 2
        
        return d[midpoint]

    def max(self,column):
        return( max( self.dataset[column] ) )

    def min(self,column):
        return( min( self.dataset[column] ) )


    
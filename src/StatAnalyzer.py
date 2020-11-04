

class StatAnalyzer:


    def __init__(self,dataset=None):
        self.dataset = dataset
   
    def setDataset(self,dataset):
        self.dataset = dataset
        
    def call(self,functioncall):

        function = functioncall[0]
        column   = functioncall[1]

        if not column in self.dataset:
            print('Column not in dataset.')
            return ''

        if function == "mean":
            return self.mean(column)

        if function == "median":
            return self.median(column)

        if function == "max":
            return self.median(column)

        if function == "max":
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


    
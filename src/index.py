from StatAnalyzer   import StatAnalyzer
from UI             import UI
from FileAccess     import FileAccess


datareader = FileAccess()



TSS = UI( StatAnalyzer( datareader.read_csv('./data/tyovoimakunnittain.csv',";",'"',True) ))


TSS.start()


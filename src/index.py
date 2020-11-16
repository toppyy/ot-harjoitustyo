
from stat_analyzer import StatAnalyzer
from user_interface import UI
from file_access import FileAccess


datareader = FileAccess()


TSS = UI(StatAnalyzer(datareader.read_csv('./data/tyovoimakunnittain.csv', ";", '"', True)))


TSS.start()


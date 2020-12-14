from gui.output_elements.table import Table
from gui.output_elements.header import Header

def frequencytable(column):

    freqs = {}

    data = column["data"]

    for item in data:
        freqs[item] = freqs.get(item, 0) + 1

    freq_list = [['Value','Count']]
    for key, value in freqs.items():
        freq_list.append([key,value])


    results = [
            Header(column["column_name"]),
            Table(freq_list)
    ]

    return results

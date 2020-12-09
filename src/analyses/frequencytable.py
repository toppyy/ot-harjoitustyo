from gui.output_elements.table import Table
from gui.output_elements.header import Header

def frequencytable(column,gui=None):

    freqs = {}

    data = column["data"]

    for item in data:
        freqs[item] = freqs.get(item, 0) + 1

    freq_list = [['Value','Count']]
    for key, value in freqs.items():
        freq_list.append([key,value])

    if len(freq_list)>100:

        msg = "The table has {} elements.".format(len(freq_list))
        msg = msg+"Are you sure you wish to render it?"

        answer = gui.ask_are_you_sure(msg)
        if answer is False:
            return None

    results = [
            Header(column["column_name"]),
            Table(freq_list)
    ]

    return results

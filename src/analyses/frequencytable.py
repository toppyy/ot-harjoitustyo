from gui.output_elements.table import Table

def frequencytable(data):

    freqs = {}

    for item in data:
        freqs[item] = freqs.get(item, 0) + 1

    freq_list = [['Value','Count']]
    for key, value in freqs.items():
        freq_list.append([key,value])

    results = [
            Table(freq_list)
    ]

    return results

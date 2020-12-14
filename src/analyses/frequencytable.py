
def frequencytable(column):

    freqs = {}

    data = column["data"]

    for item in data:
        freqs[item] = freqs.get(item, 0) + 1

    freq_list = [['Value','Count']]
    for key, value in freqs.items():
        freq_list.append([key,value])


    results = [
            column["column_name"],
            freq_list
    ]

    return results

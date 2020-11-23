def frequencytable(data):

    freqs = {}

    for item in data:
        freqs[item] = freqs.get(item, 0) + 1

    freq_list = []
    for key, value in freqs.items():
        temp = '{}: {}'.format(key, value)
        freq_list.append(temp)

    results = [
        {
            "display_as": "label",
            "text":   "Frequencies:\n",
            "value":  '\n'.join(freq_list)
        }
    ]

    return results

from gui.output_elements.text import Text

def frequencytable(data):

    freqs = {}

    for item in data:
        freqs[item] = freqs.get(item, 0) + 1

    freq_list = []
    for key, value in freqs.items():
        temp = '{}: {}'.format(key, value)
        freq_list.append(temp)

    results = [
            Text( "Frequencies:\n" +  '\n'.join(freq_list) )
    ]

    return results

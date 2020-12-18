
def frequencytable(column):
    """Counts the frequencies of distinct values of an column

    Args:
        column: a column to analyse

    Returns:
        A list of tuples (value,count)
    """

    freqs = {}

    data = column["data"]

    for item in data:
        freqs[item] = freqs.get(item, 0) + 1

    freq_list = []
    for key, value in freqs.items():
        freq_list.append((key,value))

    return freq_list

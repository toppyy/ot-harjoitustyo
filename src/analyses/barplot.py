import matplotlib.pyplot as plt


def barplot(column):
    """Displays a barplot of a column

    Args:
        column: a dict that has the data for column

    Returns:
        None: Nothing is returned as plot is displayed here
    """

    data = column['data']
    freqs = {}

    for item in data:
        freqs[item] = freqs.get(item, 0) + 1

    key_list   = []
    freq_list  = []
    for key, value in freqs.items():
        key_list.append(key)
        freq_list.append(value)

    plt.bar(key_list,freq_list)
    plt.show()

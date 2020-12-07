import matplotlib.pyplot as plt


def scatterplot(column_a,column_b):

    data_a = column_a['data']
    data_b = column_b['data']

    plt.scatter(data_a, data_b, alpha=0.5)
    plt.show()

    return None

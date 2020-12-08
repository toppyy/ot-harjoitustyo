import matplotlib.pyplot as plt


def scatterplot(column_a,column_b):
    """Displays a scatterplot of columns a and b

    Args:
        column_a: a dict that has the data for column_a
        column_b: a dict that has the data for column_b

    Returns:
        None: Nothing is returned as plot is displayed here
    """

    data_a = column_a['data']
    data_b = column_b['data']

    plt.scatter(data_a, data_b, alpha=0.5)
    plt.show()

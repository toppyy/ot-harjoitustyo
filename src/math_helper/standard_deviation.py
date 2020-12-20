from math import sqrt
from math_helper.variance import variance


def standard_deviation(data):
    """Calculates standard deviation

    Args:
        data: A list of numbers to calculate standard deviation for

    Returns:
        Standard deviation of the data
    """
    return sqrt(variance(data))

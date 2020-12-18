from math_helper.mean import mean
from math_helper.median import median
from math_helper.standard_deviation import standard_deviation

def summary(column):
    """Calculates summary statistics for a column

    Args:
        column to analyse

    Returns:
        A list of summary statistics
    """

    data = column["data"]

    return [
        median(data),
        mean(data),
        standard_deviation(data)
    ]

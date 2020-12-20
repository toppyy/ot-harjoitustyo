from math_helper.mean import mean


def variance(data):
    """Calculates sample variance

    Args:
        data: A list of numbers to calculate sample variance for

    Returns:
        Sample variance of the data
    """

    avg = mean(data)

    diff = [(x-avg)**2 for x in data]

    return sum(diff) / (len(data)-1)

from math_helper.mean import mean


def variance(data):

    avg = mean(data)

    diff = [(x-avg)**2 for x in data]

    return sum(diff) / (len(data)-1) # Note: Sample variance

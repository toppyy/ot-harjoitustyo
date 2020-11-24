from math_helper.mean import mean
from math_helper.median import median
from math_helper.standard_deviation import standard_deviation

def summary(data):

    results = [
        {
            "display_as": "label",
            "id": "median",
            "text":   "Median: ",
            "value":  median(data)
        },
        {
            "display_as": "label",
            "id": "mean",
            "text":   "Mean: ",
            "value":  mean(data)
        },
        {
            "display_as": "label",
            "id": "stddev",
            "text":   "Std.dev: ",
            "value":  standard_deviation(data)
        }
    ]

    return results

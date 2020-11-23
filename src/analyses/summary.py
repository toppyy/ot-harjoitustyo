from math_helper.mean import mean
from math_helper.median import median


def summary(data):

    results = [
        {
            "display_as": "label",
            "text":   "Median: ",
            "value":  median(data)
        },
        {
            "display_as": "label",
            "text":   "Mean: ",
            "value":  mean(data)
        }
    ]

    return results

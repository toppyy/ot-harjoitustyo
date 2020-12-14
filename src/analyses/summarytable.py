from math_helper.mean import mean
from math_helper.median import median


def summarytable(column_to_summarise_by,column_to_summarise):

    observations = {}

    data_by         = column_to_summarise_by["data"]
    data_summarise  = column_to_summarise["data"]

    # Collect data per value of column to summarise by
    for idx,item in enumerate(data_by):
        arr = observations.get(item, [])
        arr.append( data_summarise[idx] )
        observations[item] = arr

    summarystats = {}
    # Create stats per value of column to summarise by
    for key in observations:
        summarystats[key] = [
            len(observations[key]),
            mean(observations[key]),
            median(observations[key])
        ]

    # Store as list
    stats_as_list = [['Value','Count','Mean','Median']]

    for key, value in summarystats.items():
        arr = [key]
        arr.extend(value)
        stats_as_list.append(arr)


    results = stats_as_list

    return results

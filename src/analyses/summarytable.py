from math_helper.mean import mean
from math_helper.median import median


def summarytable(column_to_summarise_by,column_to_summarise):
    """Creates summary statistics for groups (distinct values in data)

    Args:
        column_to_summarise_by: column to group data by
        column_to_summarise: column to calculate summary statistics from

    Returns:
        A nested list.
        Each list contains summary statistics for each unique value of column_to_summarise_by
    """

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
    stats_as_list = []

    for key, value in summarystats.items():
        arr = [key]
        arr.extend(value)
        stats_as_list.append(arr)


    results = stats_as_list

    return results

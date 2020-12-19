from math import sqrt
from scipy.stats import t
from math_helper.mean import mean
from math_helper.variance import variance


def ttest(column,population_mean):
    """Calculates a two-way t-test

    Args:
        column: column to test
        population_mean: the mean to test agains

    Returns:
        A list of test statistics
    """


    data = column['data']

    data_mean       = mean(data)
    data_var        = variance(data)
    observations    = len(data)
    standard_err    = sqrt(data_var/observations)
    degrees_of_freedom = observations - 1

    t_statistic = ( data_mean - population_mean ) / standard_err
    p_stat     = t.cdf(t_statistic,degrees_of_freedom)

    p_value = ( 1 - p_stat ) * 2

    if data_mean < population_mean:
        p_value = p_stat * 2

    return [
        data_mean,
        population_mean,
        t_statistic,
        p_value,
        degrees_of_freedom
    ]

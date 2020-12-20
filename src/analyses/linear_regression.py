from scipy import stats
import numpy as np


def linear_regression(depended,regressor):
    """Does linear regression

    Args:
        depended: Colum whose variation is of interest
        regressor: Column to regress on

    Returns:
        List of statistics
    """

    depended_array  = np.array(depended['data'])
    regressor_array = np.array(regressor['data'])

    slope, intercept, r_value, p_value, std_err = stats.linregress(regressor_array,depended_array)

    return (
        slope,
        intercept,
        r_value**2, # R-squared
        p_value,
        std_err
    )

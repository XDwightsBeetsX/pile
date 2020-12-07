"""
Statistical Operations on data
"""


def chi_squared(observed, expected):
    """
    Returns X^2 value given 1d observed and expected arrays
    
    NOTE: expected array should not have any 0
    """
    lo = len(observed)
    le = len(expected)
    if lo == 0 or le == 0:
        raise Exception("[ERROR]: in chi_squared, observed and expected arrays must have length > 0")
    if lo != le:
        raise Exception("[ERROR]: in chi_squared, observed and expected arrays must be of same length")
    if 0 in expected:
        raise Exception("[ERROR]: in chi_squared, expected array cannot contain 0")

    x_2 = 0.0
    for i in range(lo):
        x_2 += ((observed[i] - expected[i])**2) / expected[i]
    
    return x_2


def squared_residual_sum(x, y_actual, y_regression):
    """
    Sum of squares of residual deviation of y_actual from y_regression

    Returns: float sum
    """
    pass


def squared_deviation_sum(x, y):
    """
    Sum of squares of deviation of y from mean (y)

    Returns: float sum
    """
    pass

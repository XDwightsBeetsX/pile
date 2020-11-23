"""
Statistical Operations on data
"""


def chi_squared(observed, expected):
    """
    Returns X^2 value given 1d observed and expected arrays
    
    NOTE: expected array should not have any 0
    """
    if len(observed) == 0 or len(expected) == 0:
        raise Exception("[ERROR]: in chi_squared, observed and expected arrays must have length > 0")
    if len(observed) != len(expected):
        raise Exception("[ERROR]: in chi_squared, observed and expected arrays must be of same length")
    if 0 in expected:
        raise Exception("[ERROR]: in chi_squared, expected array cannot contain 0")

    x_2 = 0.0
    for i in range(len(observed)):
        x_2 += ((observed[i] - expected[i])**2) / expected[i]
    
    return x_2


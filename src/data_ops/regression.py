"""
File to interpolate data
"""
import numpy as np


def linear_regression(x, y):
    """
    Basic linear regression in form: y = Ax + B

    To do more complex regression:
        ex: y=ln(x)
        1. take x' = ln(x)
        2. use take e^linear_regression(x', y)

    Returns regressed r_vals of linear regression
    (will have same length as input)
    """
    lx = len(x)
    ly = len(y)
    if lx == 0 or ly == 0:
        raise Exception("[ERROR]: in linear_regression, x and y arrays must have length > 0")
    if lx != ly:
        raise Exception("[ERROR]: in linear_regression, x and y arrays must be of same length")

    sum_x = 0.0
    sum_x2 = 0.0
    sum_y = 0.0
    sum_xy = 0.0
    for i in range(lx):
        xi = x[i]
        yi = y[i]
        sum_x += xi
        sum_y += yi
        sum_x2 += xi**2
        sum_xy += xi*yi
    
    a = (lx * sum_xy - sum_x * sum_y) / (lx * sum_x2 - sum_x**2)
    b = (sum_x2 * sum_y - sum_x * sum_xy) / (lx * sum_x2 - sum_x**2)

    r_vals = np.zeros(lx)
    for i in range(lx):
        r_vals[i] = a * x[i] + b
    
    return r_vals

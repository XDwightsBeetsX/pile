"""
Tests For Data Operations lib
"""
from src.data_ops import regression as reg
from src.data_gen import basic_data as basic


def test_linear_regression(displayCheck=True):
    """
    Testing if the baic.linear_regression() reduced the sum of residuals.
    """
    correct = True

    x, y = basic.linear_noise(100)
    r = reg.linear_regression(x, y)
    l = len(r)

    # need a tolerance for the accuracy of the regression
    # to check if regression has minimized
    tol = max(r) / 100  # order of magnitude 100

    resid_sum = 0
    for i in range(l):
        resid_sum += y[i] - r[i]
    
    if resid_sum > tol:
        correct = False
    
    print(resid_sum)

    if displayCheck:
        from matplotlib import pyplot as plt
        plt.scatter(x, y)
        plt.plot(x, r, 'r+')
        plt.show()

    assert correct

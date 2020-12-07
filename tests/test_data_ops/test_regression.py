"""
Tests For Data Operations lib
"""
from src.data_ops import regression as reg
from src.data_gen import basic_data as basic


# TODO FIXME
def test_linear_regression():
    correct = True

    from matplotlib import pyplot as plt
    x, y = basic.linear_noise(100)
    r = reg.linear_regression(x, y)
    plt.scatter(x, y)
    plt.plot(x, r)
    plt.show()

    assert correct

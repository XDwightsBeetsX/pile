"""
John Gutierrez
Tests For Data Manipulation lib
"""

from matplotlib import pyplot as plt

from data_manipulation import make_data as md


def test_linear_basic():
    x, y = md.linear(100)
    correct = True
    if(len(x) != len(y)):
        correct = False
    
    slope = (y[-1] - y[0]) / (x[-1] - x[0])
    if(slope != 1.0):
        correct = False

    assert correct

test_linear_basic()

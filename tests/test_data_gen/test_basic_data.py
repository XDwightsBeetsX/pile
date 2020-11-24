"""
Tests For Data Manipulation lib
"""

import numpy as np
from src.data_gen import basic_data as basic


def test_linear_basic():
    correct = True

    x, y = basic.linear(100)
    if(len(x) != len(y)):
        correct = False
    
    slope = (y[-1] - y[0]) / (x[-1] - x[0])
    if(slope != 1.0):
        correct = False

    assert correct

def test_sin_basic():
    correct = True

    x, y = basic.sin(np.pi/2)
    if(len(x) != len(y)):
        correct = False
    
    if(y[0] != 0.0):
        correct = False
    if(y[-1] != 1.0):
        correct = False

    assert correct

def test_cos_basic():
    correct = True

    x, y = basic.cos(np.pi)
    if(len(x) != len(y)):
        correct = False
    
    if(y[0] != 1.0):
        correct = False
    if(y[-1] != -1.0):
        correct = False

    assert correct


def test_normal_dist():
    correct = True

    # TODO X^2 test to compare distributions
    # TODO implement make.chi_squared

    assert correct

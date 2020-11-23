"""
Tests For Data Manipulation lib
"""

import numpy as np
from matplotlib import pyplot as plt
from src.data_gen import make_data as make


def test_linear_basic():
    correct = True

    x, y = make.linear(100)
    if(len(x) != len(y)):
        correct = False
    
    slope = (y[-1] - y[0]) / (x[-1] - x[0])
    if(slope != 1.0):
        correct = False

    assert correct

def test_sin_basic():
    correct = True

    x, y = make.sin(np.pi/2)
    if(len(x) != len(y)):
        correct = False
    
    if(y[0] != 0.0):
        correct = False
    if(y[-1] != 1.0):
        correct = False

    assert correct

def test_cos_basic():
    correct = True

    x, y = make.cos(np.pi)
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

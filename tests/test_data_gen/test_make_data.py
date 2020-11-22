"""
John Gutierrez
Tests For Data Manipulation lib
"""

import numpy as np
from matplotlib import pyplot as plt
import src.data_gen.make_data as make


def test_linear_basic():
    x, y = make.linear(100)
    correct = True
    if(len(x) != len(y)):
        correct = False
    
    slope = (y[-1] - y[0]) / (x[-1] - x[0])
    if(slope != 1.0):
        correct = False

    assert correct

def test_sin_basic():
    x, y = make.sin(np.pi/2)
    correct = True
    if(len(x) != len(y)):
        correct = False
    
    if(y[0] != 0.0):
        correct = False
    if(y[-1] != 1.0):
        correct = False

    assert correct

def test_cos_basic():
    x, y = make.cos(np.pi)
    correct = True
    if(len(x) != len(y)):
        correct = False
    
    if(y[0] != 1.0):
        correct = False
    if(y[-1] != -1.0):
        correct = False

    assert correct

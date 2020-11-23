"""
John Gutierrez
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


def test_split_int():
    correct = True

    basic = 1234
    basic_nums = make.split_int(basic)
    for i in range(4):
        if(basic_nums[i] != i + 1):
            correct = False
    
    assert correct


def test_chi_squared():
    correct = True

    # exact same dist should produce X^2 == 0.0
    exp_same = [i for i in range(1, 11)]
    obs_same = exp_same
    if(make.chi_squared(obs_same, exp_same) != 0.0):
        correct = False
    
    # diff obs and exp should produce positive X^2 > 0.0
    exp_diff = [i for i in range(1, 11)]
    obs_diff = [i for i in range(0, 10)]
    if(make.chi_squared(obs_diff, exp_diff) <= 0.0):
        correct = False
    
    # cannot expect 0.0
    try:
        exp_same = [i for i in range(0, 10)]
        obs_same = [i for i in range(1, 11)]
        _x2 = make.chi_squared(obs_same, exp_same)
        correct = False 
    except Exception as _e:
        # should throw bc expect 0.0
        pass
    
    exp_len = 100
    exp_bigTest = np.zeros(exp_len)
    obs_bigTest = np.zeros(exp_len)
    for i in range(1, exp_len + 1):
        exp_bigTest[i-1] = i
        obs_bigTest[i-1] = i + (-1)**((i + 1) % 2)
    
    x_2_big_test = make.chi_squared(obs_bigTest, exp_bigTest)

    if(x_2_big_test != 5.187377517639621):
        correct = False

    assert correct

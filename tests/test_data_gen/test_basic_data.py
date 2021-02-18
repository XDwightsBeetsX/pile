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


def test_linear_noise():
    correct = True

    x, y = basic.linear_noise(100)
    ly = len(y)
    lx = len(x)
    if(lx != ly):
        correct = False

    earlyY = sum(y[0:ly//4])
    lateY = sum(y[(3*ly//4):-1])
    pass


def test_sin():
    correct = True

    x, y = basic.sin(np.pi/2)
    if(len(x) != len(y)):
        correct = False
    
    if(y[0] != 0.0):
        correct = False
    if(y[-1] != 1.0):
        correct = False

    assert correct


def test_cos():
    correct = True

    x, y = basic.cos(np.pi)
    if (len(x) != len(y)):
        correct = False
    
    if (y[0] != 1.0):
        correct = False
    if (y[-1] != -1.0):
        correct = False

    assert correct


def test_normal_dist():
    correct = True

    b = basic.normal_dist(count=100)
    l = len(b)

    # test if 68% of data is in the one std dev range
    # within 2% deviation is acceptable
    dev = .02
    oneStdDevCtExpLower = (.68 - dev) * l
    oneStdDevCtExpUpper = (.68 + dev) * l
    oneStdDevCt = len(b[16 : (16 + 2*34)])
    if (oneStdDevCt > oneStdDevCtExpUpper or oneStdDevCt < oneStdDevCtExpLower):
        correct = False
    
    # Ensure no tails
    # within sqrt(len(b)) deviation is acceptable
    max = abs(b[-1])
    min = abs(b[0])

    spanTol = len(b)**(1/2)
    if (max - min > spanTol):
        correct = False

    assert correct

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

    s = 1.0
    yInt = 3.2
    x, y = basic.linear_noise(100, slope=s, y_int=yInt)
    
    ly = len(y)
    lx = len(x)
    if (lx != ly):
        print(ly, lx)
        correct = False

    fourth = ly//4
    earlyY = sum(y[0:fourth]) / fourth
    lateY = sum(y[(3*fourth):-1]) / fourth

    # Check if the slope bw the first fourth and last fourth is about 1.0
    # within 10% deviation is acceptable
    s_act = (lateY - earlyY) / (x[(7*fourth//2)] - x[fourth//2])
    if (abs(s - s_act) > .1):
        print(f"expected: {s}\nbut got:  {s_act}")
        correct = False
        
    assert correct


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


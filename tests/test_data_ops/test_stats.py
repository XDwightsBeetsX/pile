"""
Tests for data_gen/stats
"""
import numpy as np
from src.data_ops import stats


def test_chi_squared():
    correct = True

    # exact same dist should produce X^2 == 0.0
    exp_same = [i for i in range(1, 11)]
    obs_same = exp_same
    if(stats.chi_squared(obs_same, exp_same) != 0.0):
        correct = False
    
    # diff obs and exp should produce positive X^2 > 0.0
    exp_diff = [i for i in range(1, 11)]
    obs_diff = [i for i in range(0, 10)]
    if(stats.chi_squared(obs_diff, exp_diff) <= 0.0):
        correct = False
    
    # cannot expect 0.0
    try:
        exp_same = [i for i in range(0, 10)]
        obs_same = [i for i in range(1, 11)]
        _x2 = stats.chi_squared(obs_same, exp_same)
        correct = _x2 == None
    except Exception as _e:
        pass
    
    exp_len = 100
    exp_bigTest = np.zeros(exp_len)
    obs_bigTest = np.zeros(exp_len)
    for i in range(1, exp_len + 1):
        exp_bigTest[i-1] = i
        obs_bigTest[i-1] = i + (-1)**((i + 1) % 2)
    
    x_2_big_test = stats.chi_squared(obs_bigTest, exp_bigTest)

    calculated_x_2 = 5.187377517639621
    if(x_2_big_test != calculated_x_2):
        correct = False
    
    assert correct

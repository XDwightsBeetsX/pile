"""
Tests for utils
"""
from src.utils import utils


def test_split_int():
    correct = True

    basic = 1234
    basic_nums = utils.split_int(basic)
    for i in range(4):
        if(basic_nums[i] != i + 1):
            correct = False
    
    assert correct

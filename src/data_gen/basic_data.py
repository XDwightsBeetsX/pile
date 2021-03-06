"""
File to create artificial data
"""
import numpy as np


def linear(length, slope=1.0, y_int=0):
    """
    perfect linear trend from [0, length] with slope & y_int
    NOTE: returned arrays will not have len() == length
    """
    x_vals = np.linspace(0, length, num=int(length)*10)
    l = len(x_vals)
    y_vals = np.zeros(l)
    for i in range(l):
        y_vals[i] = slope * x_vals[i] + y_int
    
    return x_vals, y_vals



def linear_noise(length, max_noise=10.0, noise_lvl=1.0, slope=1.0, y_int=0):
    """
    Imperfect linear trend from [0, length] with slope & y_int
    
    max_noise is the noise tolerance desired. Results are based
    off a normal distribution with std_dev=noise_lvl
    
    noise_lvl should be [0, 1] with 0 being equivalent to perfect
    and 1 being maximum noise.
    
    NOTE: returned arrays will not have len() == length
    """
    if (noise_lvl < 0 or noise_lvl > 1.0):
        raise Exception("[ERROR]: In linear_noise, noise must be [0, 1.]")
    if noise_lvl == 0.0:
        return linear(length, slope=slope, y_int=y_int)
    
    l = int(length)*10
    x_vals = np.linspace(0.0, length, num=l)
    y_vals = np.zeros(l)
    
    rand_range = 100
    norm = normal_dist(center=0, std_dev=noise_lvl, count=rand_range)
    m = max(max(norm), abs(min(norm)))
    
    for i in range(l):
        y_norm = slope * x_vals[i] + y_int
        rand_i = np.random.randint(0, rand_range)
        y_noise = (norm[rand_i] / m) * max_noise
        y_vals[i] = y_norm + y_noise
    
    return x_vals, y_vals


def sin(duration=2*np.pi, amp=1.0, phase=0):
    """
    Returns x_vals, and y_vals arrays based on parameters given

    NOTE: returned arrays will not have len() == length
    """
    x_vals = np.linspace(0.0, duration, num=int(duration)*10)
    l = len(x_vals)
    y_vals = np.zeros(l)
    for i in range(l):
        y_vals[i] = amp * np.sin(x_vals[i] + phase)
    
    return x_vals, y_vals


def cos(duration, amp=1.0, phase=0):
    """
    Returns x_vals, and y_vals arrays based on parameters given

    NOTE: returned arrays will not have len() == length
    """
    divisions = 10 * duration
    x_vals = np.linspace(0.0, duration, num=int(divisions)*10)
    l = len(x_vals)
    y_vals = np.zeros(l)
    for i in range(l):
        y_vals[i] = amp * np.cos(x_vals[i] + phase)
    
    return x_vals, y_vals


def normal_dist(center=0.0, std_dev=1.0, count=100):
    return np.random.normal(center, std_dev, count)

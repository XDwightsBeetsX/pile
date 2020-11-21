"""
John Gutierrez
File to create artificial data
"""
import numpy as np


def linear(length, slope=1.0, y_int=0):
    x_vals = np.linspace(0, length, num=int(length)*10)
    l = len(x_vals)
    y_vals = np.zeros(l)
    for i in range(l):
        y_vals[i] = slope * x_vals[i] + y_int
    
    return x_vals, y_vals

def sin(duration=2*np.pi, amp=1.0, phase=0):
    x_vals = np.linspace(0.0, duration, num=int(duration)*10)
    l = len(x_vals)
    y_vals = np.zeros(l)
    for i in range(l):
        y_vals[i] = amp * np.sin(x_vals[i] + phase)
    
    return x_vals, y_vals

def cos(duration, amp=1.0, phase=0):
    divisions = 10 * duration
    x_vals = np.linspace(0, duration, num=int(divisions)*10)
    l = len(x_vals)
    y_vals = np.zeros(l)
    for i in range(l):
        y_vals[i] = amp * np.cos(x_vals[i] + phase)
    
    return x_vals, y_vals

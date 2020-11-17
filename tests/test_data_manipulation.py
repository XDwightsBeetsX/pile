"""
John Gutierrez
Tests For Data Manipulation lib
"""

from matplotlib import pyplot as plt

import data_manipulation.make_data as md

x, y = md.linear(100)
plt.plot(x, y)
plt.show()

x, y = md.sin(100)
plt.plot(x, y)
plt.show()

x, y = md.cos(100)
plt.plot(x, y)
plt.show()

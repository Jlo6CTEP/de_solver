"""euler start"""

import math

import numpy
from numba import jit


@jit(nopython=True)
def calculate(x, y, end, n_of_iter, x_axis, y_axis):
    step = (end - x) / n_of_iter

    x_0 = x
    i = 1
    x_axis[0] = x_0
    y_axis[0] = y
    while i < n_of_iter:
        z = y_axis[i - 1]
        x_axis[i] = x_0
        y_axis[i] = z + step * "$$"
        i = i + 1
        x_0 = x_0 + step
    return


"""euler end"""

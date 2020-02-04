import math

import numpy
from numba import jit


@jit(nopython=True)
def calculate(x, y, end, n_of_iter, x_axis, y_axis):
    step = (end - x) / n_of_iter

    i = 1
    x_axis[0] = x
    y_axis[0] = y
    while i < n_of_iter:
        x = x + step
        y_axis[i] = ((3*x**2 - 3*x + 2002)*math.e**(x) - 2001.0)*math.e**(-x)
        x_axis[i] = x
        i = i + 1
    return


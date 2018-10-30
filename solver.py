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
        y_axis[i] = math.e**(-2*x) +2*x - 1
        x_axis[i] = x
        i = i + 1
    return


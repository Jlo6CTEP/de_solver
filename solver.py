
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
        x_axis[i] = x
        x = x_axis[i - 1]
        y = y_axis[i - 1]
        k1 = -y + 3*x**2 + 3*x + 19

        x = x_axis[i - 1] + step / 2.0
        y = y_axis[i - 1] + step / 2.0 * k1
        k2 = -y + 3*x**2 + 3*x + 19

        x = x_axis[i - 1] + step / 2.0
        y = y_axis[i - 1] + step / 2.0 * k2
        k3 = -y + 3*x**2 + 3*x + 19

        x = x_axis[i - 1] + step
        y = y_axis[i - 1] + step * k3
        k4 = -y + 3*x**2 + 3*x + 19

        y_axis[i] = y_axis[i - 1] + step / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)

        x = x_axis[i]

        i = i + 1
        x = x + step
    return


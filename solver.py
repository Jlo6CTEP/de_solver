

import math

from numba import jit


@jit(nopython=True)
def calculate(x, y, end, n_of_iter, solution):
    step = (end - x) / n_of_iter
    x_0 = x
    i = 1
    solution[0] = y
    while i < n_of_iter:
        z = solution[i - 1]
        solution[i] = z + step * x_0 + z
        i = i + 1
        x_0 = x_0 + step
    return solution


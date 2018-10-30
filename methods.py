# this file holds python implementations for euler, improved, runge-kutta methods and for calculating analytical
# solution. Main idea is that backend takes code from here, replace $$ to differential equation and $ to analytical
# solution, then paste id into solver.py file, reload module, and calculate everything with speed of hard-coded solution
# BTW it is hardcoding.. But smart

"""e start"""

import math

import numpy
from numba import jit


@jit(nopython=True)
def calculate(x, y, end, n_of_iter, x_axis, y_axis, e_x_axis, e_y_axis):
    step = (end - x) / n_of_iter

    i = 1
    e_y_axis[0] = 0
    e_x_axis[0] = x
    x_axis[0] = x
    y_axis[0] = y
    while i < n_of_iter:
        y = y_axis[i - 1]
        x_axis[i] = x
        e_x_axis[i] = x
        y_axis[i] = y + step * ("$$")
        e_y_axis[i] = abs(y_axis[i - 1]) - abs("$")
        i = i + 1
        x = x + step
    return


"""e end"""

"""ie start"""

import math

import numpy
from numba import jit


@jit(nopython=True)
def calculate(x, y, end, n_of_iter, x_axis, y_axis, e_x_axis, e_y_axis):
    step = (end - x) / n_of_iter

    i = 1
    e_y_axis[0] = 0
    e_x_axis[0] = x
    x_axis[0] = x
    y_axis[0] = y
    while i < n_of_iter:
        x_axis[i] = x
        e_x_axis[i] = x
        x = x_axis[i - 1]
        y = y_axis[i - 1]
        m1 = "$$"

        x = x_axis[i]
        y = y_axis[i - 1] + step * m1

        m2 = "$$"

        y_axis[i] = y_axis[i - 1] + step * (m1 + m2) / 2.0

        x = x_axis[i]

        e_y_axis[i] = abs(y_axis[i - 1]) - abs("$")
        i = i + 1
        x = x + step
    return


"""ie end"""

"""rk start"""

import math

import numpy
from numba import jit


@jit(nopython=True)
def calculate(x, y, end, n_of_iter, x_axis, y_axis, e_x_axis, e_y_axis):
    step = (end - x) / n_of_iter

    i = 1
    e_y_axis[0] = 0
    e_x_axis[0] = x
    x_axis[0] = x
    y_axis[0] = y
    while i < n_of_iter:
        x_axis[i] = x
        e_x_axis[i] = x
        x = x_axis[i - 1]
        y = y_axis[i - 1]
        k1 = "$$"

        x = x_axis[i - 1] + step / 2.0
        y = y_axis[i - 1] + step / 2.0 * k1
        k2 = "$$"

        x = x_axis[i - 1] + step / 2.0
        y = y_axis[i - 1] + step / 2.0 * k2
        k3 = "$$"

        x = x_axis[i - 1] + step
        y = y_axis[i - 1] + step * k3
        k4 = "$$"

        y_axis[i] = y_axis[i - 1] + step / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)

        x = x_axis[i]

        e_y_axis[i] = abs(y_axis[i - 1]) - abs("$")

        i = i + 1
        x = x + step
    return


"""rk end"""

"""a start"""

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
        y_axis[i] = "$"
        x_axis[i] = x
        i = i + 1
    return


"""a end"""

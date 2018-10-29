import re

import numba
import numpy as np
from PyQt5 import QtWidgets
import time

import importlib
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigCanvas
from matplotlib.figure import Figure
import methods
import math_constants
import constants as c

legend_patches = {'e': 'euler', 'e_e': 'euler error', 'ie': 'improved euler',
                  'e_ie': 'improved euler error', 'rk': 'runge-kutta', 'e_rk': 'runge-kutta error', 'a': 'analytical'}


def modify_code(mode, funct="", solution=""):
    mode = (mode + ' start', mode + ' end')
    code = open('methods.py', 'r+').read()  # open back-up code file
    # modify code from back-up file, putting function into right place
    code = code[code.index(mode[0]) + 12:code.index(mode[1]) - 4].replace("\"$$\"", funct).replace("\"$\"", solution)
    open('solver.py', 'w+').write(code)  # write modified code to file
    solver = importlib.import_module("solver")
    solver = importlib.reload(solver)
    return solver


class Expression:
    def __init__(self, exp):
        self.raw = exp
        self.cooked = exp
        for x in math_constants.math_const.items():
            self.cooked = self.cooked.replace(x[0], x[1])

    def numerical_solution(self, x_0, y_0, x_n, n_iter, solution, mode,
                           euler_x, euler_y, i_euler_x, i_euler_y, runge_kutta_x, runge_kutta_y,
                           e_euler_x, e_euler_y, e_i_euler_x, e_i_euler_y, e_runge_kutta_x, e_runge_kutta_y):

        if self.check_validity():
            for x in mode:
                if x is 'e' or x is 'e_e':
                    modify_code('e', self.cooked, solution).calculate(x_0, y_0, x_n, n_iter, euler_x, euler_y,
                                                                      e_euler_x, e_euler_y)
                elif x is 'ie' or x is 'e_ie':
                    modify_code('ie', self.cooked, solution).calculate(x_0, y_0, x_n, n_iter, i_euler_x, i_euler_y,
                                                                       e_i_euler_x, e_i_euler_y)
                elif x is 'rk' or x is 'e_rk':
                    modify_code('rk', self.cooked, solution).calculate(x_0, y_0, x_n, n_iter, runge_kutta_x,
                                                                       runge_kutta_y, e_runge_kutta_x, e_runge_kutta_y)
        else:
            raise ValueError(c.PRE_CHECK_ERROR_DE)

    def analytical_solution(self, x_0, y_0, x_n, n_iter, analytical_x, analytical_y):
        if self.check_validity():
            solver = modify_code('a', solution=self.cooked)
            solver.calculate(x_0, y_0, x_n, n_iter, analytical_x, analytical_y)
        else:
            raise ValueError(c.PRE_CHECK_ERROR_AN)

    def check_validity(self):
        a = math_constants.math_const.keys()
        expr = self.raw
        for x in a:
            expr = expr.replace(x, "")
        try:
            expr = expr.replace(" ", "")
            expr = expr.replace(expr[0], "")
            expr = expr.replace(expr[0], "")
        except IndexError:
            pass
        return len(expr) == 0


class Canvas(FigCanvas):
    # plotted_graphs = {}

    def __init__(self, parent=None, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigCanvas.__init__(self, fig)
        self.setParent(parent)

    def plot(self, x_axis, y_axis, mode):
        self.axes.plot(x_axis, y_axis, label = legend_patches.get(mode))

    def pop(self, mode):
        self.plotted_graphs.pop(mode)[1].remove()

    def plot_graph(self, de, solution, graphs, x_n, n_iter, x_0, y_0):

        euler_x = np.empty([n_iter])
        euler_y = np.empty([n_iter])
        i_euler_x = np.empty([n_iter])
        i_euler_y = np.empty([n_iter])
        runge_kutta_x = np.empty([n_iter])
        runge_kutta_y = np.empty([n_iter])

        e_euler_x = np.empty([n_iter])
        e_euler_y = np.empty([n_iter])
        e_i_euler_x = np.empty([n_iter])
        e_i_euler_y = np.empty([n_iter])
        e_runge_kutta_x = np.empty([n_iter])
        e_runge_kutta_y = np.empty([n_iter])
        analytical_x = np.empty([n_iter])
        analytical_y = np.empty([n_iter])

        numerical = Expression(de)
        analytical = Expression(solution)

        try:
            numerical.numerical_solution(x_0, y_0, x_n, n_iter, analytical.cooked, graphs,
                                         euler_x, euler_y, i_euler_x, i_euler_y, runge_kutta_x, runge_kutta_y,
                                         e_euler_x, e_euler_y, e_i_euler_x, e_i_euler_y, e_runge_kutta_x,
                                         e_runge_kutta_y)
        except numba.errors.NumbaError:
            return c.CALCULATION_ERROR_DE
        try:
            analytical.analytical_solution(x_0, y_0, x_n, n_iter, analytical_x, analytical_y)
        except numba.errors.NumbaError:
            return c.CALCULATION_ERROR_DE

        self.axes.clear()

        for x in graphs:
            if x is 'e':
                self.plot(euler_x, euler_y, 'e')
            elif x is 'e_e':
                self.plot(e_euler_x, e_euler_y, 'e_e')
            elif x is 'ie':
                self.plot(i_euler_x, i_euler_y, 'ie')
            elif x is 'e_ie':
                self.plot(e_i_euler_x, e_i_euler_y, 'e_ie')
            elif x is 'rk':
                self.plot(runge_kutta_x, runge_kutta_y, 'rk')
            elif x is 'e_rk':
                self.plot(e_runge_kutta_x, e_runge_kutta_y, 'e_rk')
            elif x is 'a':
                self.plot(analytical_x,analytical_y, 'a')
            else:
                self.draw()
        self.axes.legend(title="Legend")
        self.draw()


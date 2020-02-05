import importlib

import numpy as np
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigCanvas
from matplotlib.figure import Figure
from sympy import Equality, Function, symbols, dsolve, lambdify
from sympy.parsing.sympy_parser import (parse_expr,
                                        standard_transformations,
                                        implicit_multiplication)

import constant_math
import constant_string as c

legend_patches = {'e': 'euler', 'ie': 'improved euler',
                  'rk': 'runge-kutta', 'a': 'analytical'}


def modify_code(mode, funct=""):
    mode = (mode + ' start', mode + ' end')
    code = open('methods.py', 'r+').read()  # open back-up code file
    # modify code from back-up file, putting function into right place
    code = code[code.index(mode[0]) + 12:code.index(mode[1]) - 4].replace("\"$$\"", funct)
    open('solver.py', 'w+').write(code)  # write modified code to file
    solver = importlib.import_module("solver")
    solver = importlib.reload(solver)
    return solver


class Expression:
    def __init__(self, exp):
        self.raw = exp
        self.cooked = exp
        for x in constant_math.math_const.items():
            self.cooked = self.cooked.replace(x[0], x[1])

    def numerical_solution(self, x_0, y_0, x_n, n_iter, mode, x_axis,
                            euler_y, i_euler_y, runge_kutta_y):

        if self.check_validity():
            for x in mode:
                if x is 'e':
                    modify_code('e', self.cooked).calculate(
                        x_0, y_0, x_n, n_iter, x_axis, euler_y)
                elif x is 'ie':
                    modify_code('ie', self.cooked).calculate(
                        x_0, y_0, x_n, n_iter, x_axis, i_euler_y)
                elif x is 'rk':
                    modify_code('rk', self.cooked).calculate(
                        x_0, y_0, x_n, n_iter, x_axis, runge_kutta_y)

        else:
            raise ValueError(c.PRE_CHECK_ERROR_DE)


    def check_validity(self):
        a = constant_math.math_const.keys()
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
        self.axes.plot(x_axis, y_axis, label=legend_patches.get(mode))

    def plot_graph(self, de, graphs, x_n, n_iter, x_0, y_0):

        x_axis = np.linspace(x_0, x_n, n_iter)
        euler_y = np.empty([n_iter])
        i_euler_y = np.empty([n_iter])
        runge_kutta_y = np.empty([n_iter])

        numerical = Expression(de)

        transformations = standard_transformations + (implicit_multiplication,)
        expr = parse_expr(de, transformations=transformations)

        y = Function("f")
        from sympy.abc import x
        expr = expr.replace(symbols('x'), x)
        expr = expr.replace(symbols('y'), y(x))

        eq = Equality(y(x).diff(x), expr)

        solved = dsolve(eq, ics={y(x_0): y_0})

        exact = lambdify(x, solved.rhs, "numpy")

        try:
            numerical.numerical_solution(x_0, y_0, x_n, n_iter, graphs, x_axis,
                                          euler_y, i_euler_y, runge_kutta_y)
        except:
            return c.CALCULATION_ERROR_DE

        self.axes.clear()

        for x in graphs:
            if x is 'e':
                self.plot(x_axis, euler_y, 'e')
            elif x is 'ie':
                self.plot(x_axis, i_euler_y, 'ie')
            elif x is 'rk':
                self.plot(x_axis, runge_kutta_y, 'rk')
            elif x is 'a':
                self.plot(x_axis, exact(x_axis), 'a')
            else:
                self.draw()
        self.axes.legend(title="Legend")
        self.draw()

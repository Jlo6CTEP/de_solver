from operator import add, sub, mul, truediv, pow

import math

from math_token import MathToken


operators = [MathToken('+', add, 2, True, 0, False, 'op'),
             MathToken('-', sub, 2, True, 0, False, 'op'),
             MathToken('*', mul, 2, True, 1, False, 'op'),
             MathToken('/', truediv, 2, True, 1, False, 'op'),
             MathToken('^', pow, 2, True, 2, True, 'op'),
             MathToken('!', math.factorial, 1, True, None, None, 'funct'),
             MathToken('sin', math.sin, 1, False, None, None, 'funct'),
             MathToken('cos', math.cos, 1, False, None, None, 'funct'),
             MathToken('tg', math.tan, 1, False, None, None, 'funct'),
             MathToken('ctg', lambda x: 1 / math.tan(x), 1, False, None, None, 'funct'),
             MathToken('arcsin', math.asin, 1, False, None, None, 'funct'),
             MathToken('arccos', math.acos, 1, False, None, None, 'funct'),
             MathToken('arctg', math.atan, 1, False, None, None, 'funct'),
             MathToken('arcctg', lambda x: math.atan(1 / x), 1, False, None, None, 'funct'),
             MathToken('log', math.log, 1, False, None, None, 'funct'),
             MathToken('sqrt', math.sqrt, 1, False, None, None, 'funct'),
             MathToken('e', None, None, False, None, None, 'const'),
             MathToken('pi', None, None, False, None, None, 'const'),
             MathToken('(', None, None, True, None, None, 'brk'),
             MathToken(')', None, None, True, None, None, 'brk')]

operators_dict = dict(zip([x.alias for x in operators], operators))

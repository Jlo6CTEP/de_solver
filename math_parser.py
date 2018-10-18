import numpy

from math_token import MathToken
from operators import operators, operators_dict

symbolical_op = [x.alias for x in operators if x.is_symbolical]
literals = [x.alias for x in operators if not x.is_symbolical]


class Expression:
    exp = None

    def __init__(self, exp):
        self.exp = exp

    def parse_function(self):
        parsed_func = []
        letters = ""
        digits = ""
        x = 0
        self.exp = self.exp.replace(" ", "")

        while x < len(self.exp):
            if self.exp[x] in symbolical_op:
                parsed_func.append(operators_dict.get(self.exp[x]))
                x += 1
            elif self.exp[x].isalpha():
                while x < len(self.exp) and self.exp[x].isalpha():
                    letters += self.exp[x]
                    x += 1
                if letters in literals:
                    parsed_func.append(operators_dict.get(letters))
                    letters = ""
                else:
                    parsed_func.append(MathToken(letters, None, None, False, None, None, 'var'))
                    letters = ""
            elif self.exp[x].isdigit():
                while x < len(self.exp) and (self.exp[x].isdigit() or self.exp[x] == "."):
                    digits += self.exp[x]
                    x += 1
                parsed_func.append(MathToken(str(float(digits)), None, None, True, None, None, 'const'))
                digits = ""
            else:
                raise ValueError

        return parsed_func

    def shunting_yard(self):
        parsed_func = self.parse_function()

        stack = []
        out = []

        for token in parsed_func:
            if token.op_type == 'const':
                if token.value == 'e':
                    out.append((numpy.e, True))
                elif token.value == 'pi':
                    out.append((numpy.pi, True))
                else:
                    out.append((float(token.value), True))
            elif token.type == 'funct':
                stack.insert(0, token.encoding)
            elif token.type == 'op':
                while len(stack) != 0 and stack[0].value != '(' and ((stack[0].type == 'funct' or stack[0] > token or
                                                                      stack[0] == token and not token.r_assoc)):
                    out.append((stack.pop(0).encoding, False))
                stack.insert(0, token)
            elif token.value == '(':
                stack.insert(0, token)
            elif token.value == ')':
                while len(stack) != 0 and stack[0].value != '(':
                    if stack[0].value == 'const':
                        out.append((stack[0].value, True))
                    else:
                        out.append((stack[0].encoding, False))
                    stack.pop(0)
                stack.pop(0)

        for token in stack:
            if token.type == 'brk':
                raise ValueError
            out.append((token.encoding, False))
        out = numpy.array(out)

        return out

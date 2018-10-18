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
                if token.alias == 'e':
                    out.append((numpy.e, None))
                elif token.alias == 'pi':
                    out.append((numpy.pi, None))
                else:
                    out.append((float(token.alias), None))
            elif token.op_type == 'var':
                out.append((token.alias, None))
            elif token.op_type == 'funct':
                stack.insert(0, token)
            elif token.op_type == 'op':
                while len(stack) != 0 and stack[0].alias != '(' and ((stack[0].op_type == 'funct' or stack[0] > token or
                                                                      stack[0] == token and not token.is_right_assoc)):
                    out.append((stack[0].function, stack.pop(0).arity))
                stack.insert(0, token)
            elif token.alias == '(':
                stack.insert(0, token)
            elif token.alias == ')':
                while len(stack) != 0 and stack[0].alias != '(':
                    if stack[0].alias == 'const':
                        out.append((stack[0].alias, None))
                    else:
                        out.append((stack[0].function, stack[0].arity))
                    stack.pop(0)
                stack.pop(0)

        for token in stack:
            if token.op_type == 'brk':
                raise ValueError
            out.append((token.function, token.arity))
        out = numpy.array(out)

        return out

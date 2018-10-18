import numpy


class MathToken:
    alias = None
    function = None
    arity = None
    is_symbolical = None
    priority = None
    is_right_assoc = None
    type = None

    def __init__(self, alias, funct, arity, is_symb, priority, is_right_associative, op_type):
        self.alias = alias
        self.function = funct
        self.arity = arity
        self.is_symbolical = is_symb
        self.priority = priority
        self.is_right_assoc = is_right_associative
        self.type = op_type

    def __lt__(self, other):
        return numpy.sign(self.priority - other.priority) == -1

    def __gt__(self, other):
        return numpy.sign(self.priority - other.priority) == 1

    def __eq__(self, other):
        return numpy.sign(self.priority - other.priority) == 0
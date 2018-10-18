import numpy


class Solver:
    def euler(self, start, finish, step, expression):
        result = numpy.empty([(finish - step) / step, 1])
        while start <= finish:
            pass

    def runge_kutta(self, start, finish, step, expression):
        pass

    def improved_euler(self, start, finish, step, expression):
        pass

    def evaluate(self, expression):
        stack = numpy.empty([len(expression), 1])  # again a lil bit unpythonic, but fast
        stack_top = 0
        for x in expression:
            if x[1]:
                stack[stack_top] = x[0]
                stack_top += 1
            else:
                x[0](stack[stack_top], stack[stack_top-1])

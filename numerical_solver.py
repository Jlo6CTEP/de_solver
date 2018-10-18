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

    def evaluate(self, expression, stack):
        # again a lil bit unpythonic, but here i do everything for speed
        stack_top = -1
        i = 0
        j = 0
        while i < len(expression):
            if not expression[i][1]:
                stack_top += 1
                stack[stack_top][0] = expression[i][0]
                stack[stack_top][1] = None
            else:
                if expression[i][1] == 1:
                    stack[stack_top] = expression[i][0](stack[stack_top][0])
                    stack[stack_top][1] = None
                else:
                    stack[stack_top - 1][0] = expression[i][0](stack[stack_top - 1][0], stack[stack_top][0])
                    stack[stack_top], stack[stack_top][1], stack[stack_top - 1][1] = None, None, None
                    stack_top -= 1
            i += 1
        return stack[stack_top][0]

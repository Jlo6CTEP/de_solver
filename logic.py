import sys

import time
from PyQt5 import QtWidgets
import project
import numpy
from numba import autojit

symbolical_op = ['(', ')', '+', '-', '/', '*', '^', '!']
literal_op = ['sin', 'cos', 'tg', 'ctg', 'arcsin', 'arccos', 'arctg', 'arcctg', 'ln', 'log', 'sqrt', 'e', 'pi']

prior = {'+': (0, False), '-': (0, False), '/': (1, False), '*': (1, False), '^': (2, True)}


class Token:
    value = None
    type = None
    r_assoc = None
    priority = None

    def __init__(self, value, name):
        self.value = value
        self.type = name
        if self.type == 'op':
            self.r_assoc = prior.get(value, None)[1]
            self.priority = prior.get(value, None)[0]

    def __lt__(self, other):
        kek = numpy.sign(self.priority - other.priority) == -1
        return kek

    def __gt__(self, other):
        kek = numpy.sign(self.priority - other.priority) == 1
        return kek

    def __eq__(self, other):
        kek = numpy.sign(self.priority - other.priority) == 0
        return kek


def parse_function(func):
    parsed_func = []
    letters = ""
    digits = ""
    x = 0
    func = func.replace(" ", "")

    while x < len(func):
        if func[x] in symbolical_op:
            if func[x] in symbolical_op[2:]:
                parsed_func.append(Token(func[x], 'op'))
            else:
                parsed_func.append(Token(func[x], 'brk'))
            x += 1
        elif func[x].isalpha():
            while x < len(func) and func[x].isalpha():
                letters += func[x]
                x += 1
            if letters in literal_op:
                if letters in literal_op[11:]:
                    parsed_func.append(Token(letters, 'const'))
                else:
                    parsed_func.append(Token(letters, 'funct'))
                letters = ""
            else:
                parsed_func.append(Token(letters, 'var'))
                letters = ""
        elif func[x].isdigit():
            while x < len(func) and (func[x].isdigit() or func[x] == "."):
                digits += func[x]
                x += 1
            parsed_func.append(Token(str(float(digits)), 'const'))
            digits = ""
        else:
            raise ValueError

    return parsed_func


def shunting_yard(func):
    parsed_func = parse_function(func)

    stack = []
    out = []

    for token in parsed_func:
        if token.type == 'const':
            if token.value == 'e':
                out.append(numpy.e)
            elif token.value == 'pi':
                out.append(numpy.pi)
            else:
                out.append(float(token.value))
        elif token.type == 'funct':
            stack.insert(0, token)
        elif token.type == 'op':
            while len(stack) != 0 and stack[0].value != '(' and ((stack[0].type == 'funct' or stack[0] > token or
                                                                  stack[0] == token and not token.r_assoc)):
                out.append(stack.pop(0).value)
            stack.insert(0, token)
        elif token.value == '(':
            stack.insert(0, token)
        elif token.value == ')':
            while len(stack) != 0 and stack[0].value != '(':
                out.append(stack.pop(0).value)
            stack.pop(0)

    for token in stack:
        if token.type == 'brk':
            raise ValueError
        out.append(token.value)

    return out


class ExampleApp(QtWidgets.QMainWindow, project.Ui_MainWindow):
    i = 0

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.buttonLeft.clicked.connect(self.on_click)

    def on_click(self):
        self.textField.addItem(str(self.i))
        self.i += 1


def lel(x, kek):
    for x in range(x):
        kek[x][0] = (x / 1000.0) ** 2
    return kek


def main():
    x = 10000000
    # app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    # window = ExampleApp()  # Создаём объект класса ExampleApp
    # window.show()  # Показываем окно
    # app.exec_()  # и запускаем приложение
    # lol = autojit(lel)

    print(shunting_yard("(1+2)*4+3"))


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()

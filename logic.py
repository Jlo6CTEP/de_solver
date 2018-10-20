import numpy
from PyQt5 import QtWidgets
import time

import solver
import importlib
import project


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


def main():
    # app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    # window = ExampleApp()  # Создаём объект класса ExampleApp
    # window.show()  # Показываем окно
    # app.exec_()  # и запускаем приложение

    print("ready here")
    x = 0

    funct = input().replace("x", "x_0").replace("y", "z")

    code = open('methods.py', 'r+').read()
    code = code[code.index("euler start") + 14:code.index("euler end") - 4].replace("\"$$\"", funct)

    f = open('solver.py', 'w+')
    f.write(code)
    f.close()
    importlib.reload(solver)
    time.clock()
    arr = numpy.empty([10000000, 1])
    solver.calculate(1, 1, 10, 10000000, arr)
    print(time.clock())


if __name__ == '__main__':  # Если мы запускаем фай л напрямую, а не импортируем
    main()  # то запускаем функцию main()

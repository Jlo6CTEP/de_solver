from operator import sub, mul

from PyQt5 import QtWidgets
import time

import project
from  math_parser import Expression
from numba import autojit
from operators import operators_dict


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

    a = Expression("e * sin(x*2/z)")
    kek = a.parse_function()
    print(kek)


if __name__ == '__main__':  # Если мы запускаем фай л напрямую, а не импортируем
    main()  # то запускаем функцию main()

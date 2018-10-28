import numpy as np
from PyQt5 import QtWidgets
import time

import importlib
import project
import matplotlib

# matplotlib.use('GTKAgg')
import matplotlib.pyplot as plt
from glumpy import app


class ExampleApp(QtWidgets.QMainWindow, project.Ui_MainWindow):
    i = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonLeft.clicked.connect(self.on_click)

    def on_click(self):
        self.textField.addItem(str(self.i))
        self.i += 1


def main():
    # app = QtWidgets.QApplication(sys.argv)
    # window = ExampleApp()
    # window.show()
    # app.exec_()

    print("ready here")

    funct = input().replace("x", "x_0").replace("y", "z")  # obtain function for evaluation

    code = open('methods.py', 'r+').read()  # open back-up code file

    # modify code from back-up file, putting function into right place
    code = code[code.index("euler start") + 14:code.index("euler end") - 4].replace("\"$$\"", funct)

    open('solver.py', 'w+').write(code)  # write modified code to file

    solver = importlib.import_module("solver")

    x_axis = np.empty([10000000])
    y_axis = np.empty([10000000])

    solver.calculate(0, 1, 2, 10000000, x_axis, y_axis)

    plt.plot(x_axis, y_axis)

    plt.show()

    print(time.clock())
    input()


if __name__ == '__main__':
    main()

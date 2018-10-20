import numpy
from PyQt5 import QtWidgets
import time

import solver
import importlib
import project


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
    x = 0

    funct = input().replace("x", "x_0").replace("y", "z")  # obtain function for evaluation

    code = open('methods.py', 'r+').read()  # open back-up code file

    # modify code from back-up file, putting function into right place
    code = code[code.index("euler start") + 14:code.index("euler end") - 4].replace("\"$$\"", funct)

    open('solver.py', 'w+').write(code)  # write modified code to file

    importlib.reload(solver)  # reload module to apply changes in code
    time.clock()
    arr = numpy.empty([10000000, 1])  # and now the warp engine is engaged!
    solver.calculate(1, 1, 10, 10000000, arr)  # we're ready to ROCK
    print(time.clock())


if __name__ == '__main__':
    main()

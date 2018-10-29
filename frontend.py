import sys

import time

from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QPushButton, QCheckBox, QVBoxLayout, \
    QHBoxLayout, QFormLayout, QFrame, QScrollArea, QApplication
from PyQt5 import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigCanvas, NavigationToolbar2QT as NavToolbar
from matplotlib.figure import Figure
from backend import Canvas
import backend
import constants as c
import ctypes


class DE_solver(QWidget):

    def __init__(self, parent=None):
        super(DE_solver, self).__init__(parent)

        my_app_id = 'InnoUI.DE_Solver.smart_solver.101'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)

        # widgets and layouts for main window

        self.input_de = QLineEdit()
        self.input_solution = QLineEdit()
        self.input_initial_x = QLineEdit()
        self.input_initial_y = QLineEdit()
        self.input_n_iter = QLineEdit()
        self.input_final_x = QLineEdit()

        self.error_log = QLabel()

        self.calculate = QPushButton(c.CALCULATE)
        self.help = QPushButton(c.HELP)

        self.euler = (QCheckBox(), 'e')
        self.euler_truncation = (QCheckBox(), 'e_e')
        self.improved_euler = (QCheckBox(), 'ie')
        self.improved_euler_truncation = (QCheckBox(), 'e_ie')
        self.runge_kutta = (QCheckBox(), 'rk')
        self.runge_kutta_truncation = (QCheckBox(), 'e_rk')
        self.analytical = (QCheckBox(), 'a')

        self.input_box = QVBoxLayout()
        self.initial_box = QHBoxLayout()
        self.app_box = QHBoxLayout()
        self.upper_box = QHBoxLayout()
        self.main_box = QVBoxLayout()

        self.param_form = QFormLayout()
        self.plot_form = QFormLayout()

        self.input_frame = QFrame()
        self.param_frame = QFrame()
        self.plot_frame = QFrame()

        self.scroll_error_log = QScrollArea()

        self.canvas = Canvas(self)
        self.toolbar = NavToolbar(self.canvas, self)

        # widgets and layout for auxiliary windows
        self.aux_window = QWidget()
        self.aux_list = QLabel()
        self.aux_scroll_area = QScrollArea()
        self.aux_box = QVBoxLayout()

        # now create main window
        self.create_main_window()

    def closeEvent(self, event):
        self.aux_window.close()
        event.accept()

    def create_main_window(self):
        self.setWindowIcon(QtGui.QIcon('DE.png'))

        self.help.setFixedSize(self.help.sizeHint())

        self.upper_box.addWidget(self.toolbar)
        self.upper_box.addStretch()
        self.upper_box.addWidget(self.help)

        self.input_de.setPlaceholderText(c.INPUT_DE)
        self.input_de.setToolTip(c.DE_TOOLTIP)

        self.input_solution.setPlaceholderText(c.INPUT_SOLUTION)
        self.input_solution.setMinimumSize(self.input_solution.sizeHint() * 1.2)
        self.input_solution.setToolTip(c.SOLUTION_TOOLTIP)

        self.input_initial_x.setFixedWidth(self.input_initial_x.sizeHint().width() / 5.0)
        self.input_initial_y.setFixedWidth(self.input_initial_y.sizeHint().width() / 5.0)
        self.input_initial_x.setValidator(QtGui.QDoubleValidator())
        self.input_initial_y.setValidator(QtGui.QDoubleValidator())

        self.initial_box.addWidget(QLabel("f("))
        self.initial_box.addWidget(self.input_initial_x)
        self.initial_box.addWidget(QLabel(") = "))
        self.initial_box.addWidget(self.input_initial_y)
        self.initial_box.addStretch()

        self.input_final_x.setValidator(QtGui.QDoubleValidator())
        self.input_n_iter.setValidator(QtGui.QDoubleValidator())
        self.param_form.addRow(QLabel(c.INPUT_INIT_COND), self.initial_box)
        self.param_form.addRow(QLabel(c.INPUT_N_ITER), self.input_n_iter)
        self.param_form.addRow(QLabel(c.FINAL_X), self.input_final_x)

        self.param_frame.setFrameShape(QFrame.Panel)
        self.param_frame.setLayout(self.param_form)

        self.plot_form.addRow(QLabel(c.EULER), self.euler[0])
        self.plot_form.addRow(QLabel(c.IMPROVED_EULER), self.improved_euler[0])
        self.plot_form.addRow(QLabel(c.RUNGE_KUTTA), self.runge_kutta[0])
        self.plot_form.addRow(QLabel(c.EULER_TRUNCATION), self.euler_truncation[0])
        self.plot_form.addRow(QLabel(c.IMPROVED_EULER_TRUNCATION), self.improved_euler_truncation[0])
        self.plot_form.addRow(QLabel(c.RUNGE_KUTTA_TRUNCATION), self.runge_kutta_truncation[0])
        self.plot_form.addRow(QLabel(c.ANALYTICAL_SOLUTION), self.analytical[0])

        self.plot_frame.setFrameShape(QFrame.Panel)
        self.plot_frame.setLayout(self.plot_form)

        self.canvas.setMinimumSize(self.canvas.sizeHint() / 2.0)
        self.error_log.setStyleSheet('color: red')
        self.scroll_error_log.setWidget(self.error_log)
        self.scroll_error_log.setWidgetResizable(True)

        self.input_box.addWidget(self.input_de)
        self.input_box.addWidget(self.input_solution)
        self.input_box.addWidget(self.param_frame)
        self.input_box.addWidget(self.plot_frame)
        self.input_box.addWidget(self.scroll_error_log)
        self.input_box.addWidget(self.calculate)

        self.input_frame.setFrameShape(QFrame.Panel)
        self.input_frame.setLayout(self.input_box)

        self.app_box.addWidget(self.canvas)
        self.app_box.addWidget(self.input_frame)
        self.app_box.setStretchFactor(self.canvas, 1)

        self.main_box.addLayout(self.upper_box)
        self.main_box.addLayout(self.app_box)

        self.setLayout(self.main_box)

        self.setWindowTitle(c.TITLE)

        self.calculate.clicked.connect(self.solve)
        self.help.clicked.connect(self.create_aux_window)

        self.show()

    def create_aux_window(self):
        if not self.aux_window.isVisible():
            self.aux_window.setWindowIcon(QtGui.QIcon('DE.png'))

            self.aux_scroll_area.setWidget(self.aux_list)
            self.aux_scroll_area.setWidgetResizable(True)

            self.aux_list.setText(c.HELP_TEXT)

            self.aux_box = QVBoxLayout()
            self.aux_box.addWidget(self.aux_scroll_area)

            self.aux_window.setWindowTitle('help')
            self.aux_window.setLayout(self.aux_box)
            self.aux_window.setGeometry(self.geometry().x() + self.size().width() + 2.0, self.geometry().y(),
                                        self.size().width() / 3, self.size().height())
            self.aux_window.show()

    def solve(self):
        field = [[self.input_de.text(), c.DE],
                 [self.input_solution.text(), c.ANALYTICAL_SOLUTION],
                 [self.input_n_iter.text(), c.INPUT_N_ITER],
                 [self.input_initial_x.text(), c.INPUT_INIT_COND],
                 [self.input_initial_x.text(), c.INPUT_INIT_COND]]

        for x in field:
            if not x[0]:
                self.error_log.setText(self.error_log.text() + '\n' + x[1] + " " + c.IS_NOT_SET)
                return
        mode = []
        if self.euler[0].isChecked():
            mode.append(self.euler[1])
        if self.euler_truncation[0].isChecked():
            mode.append(self.euler_truncation[1])
        if self.improved_euler[0].isChecked():
            mode.append(self.improved_euler[1])
        if self.improved_euler_truncation[0].isChecked():
            mode.append(self.improved_euler_truncation[1])
        if self.runge_kutta[0].isChecked():
            mode.append(self.runge_kutta[1])
        if self.runge_kutta_truncation[0].isChecked():
            mode.append(self.runge_kutta_truncation[1])
        if self.analytical[0].isChecked():
            mode.append(self.analytical[1])

        return_message = self.canvas.plot_graph(self.input_de.text(), self.input_solution.text(), mode,
                                                float(self.input_final_x.text()), int(self.input_n_iter.text()),
                                                float(self.input_initial_x.text()), float(self.input_initial_y.text()))
        if return_message:
            self.error_log.setText(self.error_log.text() + '\n' + return_message)


app = QApplication(sys.argv)

a_window = DE_solver()
sys.exit(app.exec_())

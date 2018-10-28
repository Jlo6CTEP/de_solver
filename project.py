import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import constants as c
import ctypes

class DE_solver(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(DE_solver, self).__init__(parent)

        my_app_id = 'InnoUI.DE_Solver.smart_solver.101'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)

        # widgets and layout for main window
        self.input_de = QtWidgets.QLineEdit()
        self.input_solution = QtWidgets.QLineEdit()
        self.argument_from = QtWidgets.QLineEdit()
        self.argument_to = QtWidgets.QLineEdit()
        self.function_from = QtWidgets.QLineEdit()
        self.function_to = QtWidgets.QLineEdit()

        self.methods = QtWidgets.QLabel(c.METHODS)
        self.errors = QtWidgets.QLabel(c.ERRORS)
        self.scaling = QtWidgets.QLabel(c.SCALING)
        self.argument = QtWidgets.QLabel(c.X)
        self.function = QtWidgets.QLabel(c.Y)

        self.calculate = QtWidgets.QPushButton(c.CALCULATE)
        self.redraw = QtWidgets.QPushButton(c.REDRAW)
        self.save = QtWidgets.QPushButton(c.SAVE)
        self.help = QtWidgets.QPushButton(c.HELP)

        self.input_box = QtWidgets.QVBoxLayout()
        self.app_box = QtWidgets.QHBoxLayout()
        self.upper_box = QtWidgets.QHBoxLayout()
        self.main_box = QtWidgets.QVBoxLayout()
        self.argument_range_box = QtWidgets.QHBoxLayout()
        self.function_range_box = QtWidgets.QHBoxLayout()

        self.accuracy_form = QtWidgets.QFormLayout()
        self.methods_form = QtWidgets.QFormLayout()
        self.errors_form = QtWidgets.QFormLayout()
        self.rescale_form = QtWidgets.QFormLayout()

        self.input_frame = QtWidgets.QFrame()
        self.accuracy_frame = QtWidgets.QFrame()
        self.methods_frame = QtWidgets.QFrame()
        self.errors_frame = QtWidgets.QFrame()
        self.rescale_frame = QtWidgets.QFrame()

        self.canvas = Canvas([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], self)

        # widgets and layout for auxiliary windows
        self.aux_window = QtWidgets.QWidget()
        self.aux_list = QtWidgets.QLabel()
        self.aux_scroll_area = QtWidgets.QScrollArea()
        self.aux_box = QtWidgets.QVBoxLayout()

        # now create main window
        self.create_main_window()

    def create_main_window(self):
        self.setWindowIcon(QtGui.QIcon('DE.png'))

        self.save.setFixedSize(self.save.sizeHint())
        self.help.setFixedSize(self.help.sizeHint())

        self.methods.setToolTip(c.METHODS_TOOLTIP)
        self.errors.setToolTip(c.ERRORS_TOOLTIP)
        self.scaling.setToolTip(c.SCALING_TOOLTIP)

        self.upper_box.addWidget(self.save)
        self.upper_box.addWidget(self.help)
        self.upper_box.addStretch()

        self.argument_from.setFixedWidth(self.argument_from.sizeHint().width() / 2.0)
        self.argument_to.setFixedWidth(self.argument_to.sizeHint().width() / 2.0)
        self.function_from.setFixedWidth(self.function_from.sizeHint().width() / 2.0)
        self.function_to.setFixedWidth(self.function_to.sizeHint().width() / 2.0)

        self.input_de.setPlaceholderText(c.ENTER_DE)
        self.input_de.setToolTip(c.DE_TOOLTIP)

        self.input_solution.setPlaceholderText(c.ENTER_SOLUTION)
        self.input_solution.setMinimumSize(self.input_solution.sizeHint() * 1.2)
        self.input_solution.setToolTip(c.SOLUTION_TOOLTIP)

        self.accuracy_form.addRow(QtWidgets.QLabel(c.ACCURACY), QtWidgets.QLineEdit())

        self.accuracy_frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.accuracy_frame.setLayout(self.accuracy_form)
        self.accuracy_frame.setToolTip(c.ACCURACY_TOOLTIP)

        self.methods_form.addRow(QtWidgets.QLabel(c.EULER), QtWidgets.QCheckBox())
        self.methods_form.addRow(QtWidgets.QLabel(c.IMPROVED_EULER), QtWidgets.QCheckBox())
        self.methods_form.addRow(QtWidgets.QLabel(c.RUNGE_KUTTA), QtWidgets.QCheckBox())
        self.methods_frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.methods_frame.setLayout(self.methods_form)

        self.errors_form.addRow(QtWidgets.QLabel(c.LOCAL), QtWidgets.QCheckBox())
        self.errors_form.addRow(QtWidgets.QLabel(c.TRUNCATION), QtWidgets.QCheckBox())
        self.errors_frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.errors_frame.setLayout(self.errors_form)

        self.argument_range_box.addWidget(QtWidgets.QLabel(c.FROM))
        self.argument_range_box.addWidget(self.argument_from)
        self.argument_range_box.addWidget(QtWidgets.QLabel(c.TO))
        self.argument_range_box.addWidget(self.argument_to)
        self.argument_range_box.addStretch()

        self.function_range_box.addWidget(QtWidgets.QLabel(c.FROM))
        self.function_range_box.addWidget(self.function_from)
        self.function_range_box.addWidget(QtWidgets.QLabel(c.TO))
        self.function_range_box.addWidget(self.function_to)
        self.function_range_box.addStretch()

        self.rescale_form.addRow(self.argument, self.argument_range_box)
        self.rescale_form.addRow(self.function, self.function_range_box)
        self.rescale_frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.rescale_frame.setLayout(self.rescale_form)

        self.canvas.setMinimumSize(self.canvas.sizeHint() / 2.0)

        self.input_box.addWidget(self.input_de)
        self.input_box.addWidget(self.input_solution)
        self.input_box.addWidget(self.accuracy_frame)
        self.input_box.addSpacing(10)
        self.input_box.addWidget(self.methods)
        self.input_box.addWidget(self.methods_frame)
        self.input_box.addSpacing(10)
        self.input_box.addWidget(self.errors)
        self.input_box.addWidget(self.errors_frame)
        self.input_box.addSpacing(10)
        self.input_box.addWidget(self.scaling)
        self.input_box.addWidget(self.rescale_frame)
        self.input_box.addWidget(self.redraw)
        self.input_box.addWidget(self.calculate)
        self.input_box.addStretch()

        self.input_frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.input_frame.setLayout(self.input_box)

        self.app_box.addWidget(self.canvas)
        self.app_box.addWidget(self.input_frame)
        self.app_box.setStretchFactor(self.canvas, 1)

        self.main_box.addLayout(self.upper_box)
        self.main_box.addLayout(self.app_box)

        self.setLayout(self.main_box)

        self.setWindowTitle(c.TITLE)

        self.calculate.clicked.connect(self.clicked)
        self.help.clicked.connect(self.create_aux_window)

        self.show()

    def create_aux_window(self):
        if not self.aux_window.isVisible():
            self.aux_window.setWindowIcon(QtGui.QIcon('DE.png'))

            self.aux_scroll_area.setWidget(self.aux_list)
            self.aux_scroll_area.setWidgetResizable(True)

            self.aux_list.setText(c.HELP_TEXT)

            self.aux_box = QtWidgets.QVBoxLayout()
            self.aux_box.addWidget(self.aux_scroll_area)

            self.aux_window.setWindowTitle('help')
            self.aux_window.setLayout(self.aux_box)
            self.aux_window.setGeometry(self.geometry().x() + self.size().width() + 2.0, self.geometry().y(),
                                        self.size().width()/3, self.size().height())
            self.aux_window.show()
            print(self.aux_window.pos())

    def clicked(self):
        self.input_de.setText("Fork urself")


class Canvas(FigureCanvas):
    def __init__(self, x_axis, y_axis, parent=None, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.plot(x_axis, y_axis)

    def plot(self, x_axis, y_axis):
        axis = self.figure.add_subplot(111)
        axis.plot(x_axis, y_axis)


app = QtWidgets.QApplication(sys.argv)

a_window = DE_solver()
sys.exit(app.exec_())

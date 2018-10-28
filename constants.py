TITLE = "DE Solver"
HELP_TEXT = open('help.txt', 'r').read()

METHODS = 'Methods'
ERRORS = "Errors"
SCALING = "Scaling"
CALCULATE = "calculate"
REDRAW = "redraw"
SAVE = "save plot"
HELP = "help"
METHODS_TOOLTIP = "By checking this you can choose different numerical methods to solve DE"
ERRORS_TOOLTIP = "By checking this you can add plot of errors to plot"
SCALING_TOOLTIP = "You can better look at some part of plot using this"
ENTER_DE = "Enter your FO ordinary DE"
DE_TOOLTIP = "Please provide DE in form y' = f(x,y), y(x0) = y0 \nYou can also use other one-letter variables"
ENTER_SOLUTION = "Enter your analytical solution"
SOLUTION_TOOLTIP = "Provide analytical solution in form y = f(x)"
ACCURACY = "Graph accuracy"

ACCURACY_TOOLTIP = "This parameter determine percentage of points used by \n" + \
                   "plotting module. This will not affect calculations. \n" + \
                   "Decrease this to reduce lags"

EULER = "Euler"
IMPROVED_EULER = "Improved Euler"
RUNGE_KUTTA = "Runge-Kutta"

LOCAL = "Local"
TRUNCATION = "Truncation"
FROM = "from"
TO = "to"
X = "x"
Y = "y"



TITLE = "DE Solver"
HELP_TEXT = open('help.txt', 'r').read()

CALCULATE = "calculate"
SAVE = "save plot"
HELP = "help"
DE = "FO ordinary DE"
INPUT_DE = "Enter your " + DE
ANALYTICAL_SOLUTION = "Analytical solution"
DE_TOOLTIP = "Please provide DE in form y' = f(x,y), y(x0) = y0 \nYou can also use other one-letter variables"
INPUT_SOLUTION = "Enter your " + ANALYTICAL_SOLUTION
SOLUTION_TOOLTIP = "Provide analytical solution in form y = f(x)"
IS_NOT_SET = "is not set. Aborting calculations"
INPUT_N_ITER = "Number of iterations"
INPUT_INIT_COND = "Initial condition"
FINAL_X = "Final x value"

EULER = "Euler"
IMPROVED_EULER = "Improved Euler"
RUNGE_KUTTA = "Runge-Kutta"
EULER_TRUNCATION = "Truncation error: Euler"
IMPROVED_EULER_TRUNCATION = "Truncation error: Improved Euler"
RUNGE_KUTTA_TRUNCATION = "Truncation error: Runge-Kutta"

PRE_CHECK_ERROR_DE = "Error during pre-check of input differential equation"
PRE_CHECK_ERROR_AN = "Error during pre-check of analytical solution"
CALCULATION_ERROR_DE = "Error during calculation of input differential equation"
CALCULATION_ERROR_AN = "Error during calculation of analytical solution"

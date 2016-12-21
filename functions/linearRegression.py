# Takes the variables in 'list' and computes a linear fit to
# the data. The function returns the gradient of the fit, as
# well as the residual.

import numpy as np
from scipy import polyfit

def linearRegression( list ) :
    x = np.linspace(1,len(list),len(list))
    # Fit the data to y = mx + c
    linearModel = polyfit( x, list, 1, full=True)
    m = linearModel[0][0]
    res = linearModel[1]
    return m, res
# This function takes the CdA value, virtual elevation, regression
# slope and residual in order to calculate the error of the CdA value.

from calcVirtualElevation import calcVirtualElevation
from linearRegression import linearRegression
from findLocalMinima import findLocalMinima

def calcErrorOfCdA( virtElev, coef, res, CdA, m, g, Crr, rho, speed, power ) :
    T = len(virtElev)
    newCdA = CdA
    while T*coef < res :                                   # If change in y is less than the residual, then the
        newCdA -= 0.00001                                    # then the regression is potentially insignificant
        newElev = calcVirtualElevation( newCdA, m, g, Crr, rho, speed, power )
        newMin = findLocalMinima( newElev )
        coef, _ = linearRegression( newMin)
    return CdA - newCdA
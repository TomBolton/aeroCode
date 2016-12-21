# This script computes the Chung analysis in order to estimate
# the CdA value from ride data. This is the same as the Golden
# Cheetah aerolab software, with one difference: instead of the
# user adjusting the CdA value to level the virtual elevation,
# a range of CdA values are used to see where the gradient of
# the virtual elevation is closest to zero.

import matplotlib.pyplot as plt
from getTcxData import extractData
from calcVirtualElevation import calcVirtualElevation
from scipy import polyfit
from findLocalMinima import findLocalMinima
import pylab
import numpy as np

def linearRegression( list ) :
    x = np.linspace(1,len(list),len(list))
    # Fit the data to y = mx + c
    [m, c] = polyfit(x,list,1)
    return m


# Set the parameters.

m = 80.0  # Mass of person + bike in kilograms (kg).
g = 9.81  # Acceleration due to gravity (ms^(-2)).
Crr = 0.006  # Coefficient of rolling resistance (approximately).
rho = 1.279  # Air density (kgm^(-3)).

# This is the starting value of CdA (Boardman 1996 Superman Position CdA)
CdA = 0.18

# Get speed and power data from file (change file name if needed)
data = extractData( 'hoods.tcx' )
power = data[0]
speed = data[1]

# Get an initial figure ready
virtElev = calcVirtualElevation( CdA, m, g, Crr, rho, speed, power )
plt.ion()
graph = plt.plot( virtElev )[0]

# Produce an initial linear regression
minima = findLocalMinima( virtElev )
coef = linearRegression( minima )


# Incrementally increase the CdA value until the slope of the
# minima of the virtual elevation is zero
while coef > 0.0 :
    CdA += 0.001
    virtElev = calcVirtualElevation( CdA, m, g, Crr, rho, speed, power )
    minima = findLocalMinima( virtElev )
    coef = linearRegression( minima )
    graph.set_ydata( virtElev )
    plt.draw()
    plt.pause(0.01)
pylab.show(block=True)





# This script computes the Chung analysis in order to estimate
# the CdA value from ride data. This is the same as the Golden
# Cheetah aerolab software, with one difference: instead of the
# user adjusting the CdA value to level the virtual elevation,
# a range of CdA values are used to see where the gradient of
# the virtual elevation is closest to zero.

import matplotlib.pyplot as plt
import numpy as np

from functions.calcErrorOfCdA import calcErrorOfCdA
from functions.calcVirtualElevation import calcVirtualElevation
from functions.findLocalMinima import findLocalMinima
from functions.getTcxData import getTcxData
from functions.linearRegression import linearRegression

# Set the parameters.

m = 80.0  # Mass of person + bike in kilograms (kg).
g = 9.81  # Acceleration due to gravity (ms^(-2)).
Crr = 0.006  # Coefficient of rolling resistance (approximately).
rho = 1.279  # Air density (kgm^(-3)).

# This is the starting value of CdA (Boardman 1996 Superman Position CdA)
CdA = 0.18

# Get speed and power data from file (change file name if needed)
data = getTcxData( 'tcx_files/drops.tcx' )
power = data[0]
speed = data[1]

# Get an initial figure ready
virtElev = calcVirtualElevation( CdA, m, g, Crr, rho, speed, power )
time = np.linspace(1,len(virtElev),len(virtElev))
plt.ion()
plt.plot( time, np.zeros(len(time)), 'k:' )
line = plt.plot( time, virtElev, 'r' )[0]
plt.xlabel('Time (s)')
plt.ylabel('Virtual Elevation (m)')
plt.title('Virtual Elevation Estimated from Power and Speed Data')
plt.ylim([-15, 25])
txt = plt.text( 10, 20, 'CdA = ' + str( CdA ), fontsize=20 )

# Produce an initial linear regression
minima = findLocalMinima( virtElev )
coef, res = linearRegression( minima )


# Incrementally increase the CdA value until the slope of the
# minima of the virtual elevation is zero. This is when the
# CdA value is closest to the truth; this is due to the fact
# that the elevation of the lowest point in the road MUST be
# the same everytime.
while coef > 0.0 :

    # Increment CdA value and calculate new local minima of virtual elevation. Then
    # fit a linear model to the new local minima
    CdA += 0.001
    virtElev = calcVirtualElevation( CdA, m, g, Crr, rho, speed, power )
    minima = findLocalMinima( virtElev )
    coef, res = linearRegression( minima )

    # Plot the virtual elevation using the new CdA value
    line.set_ydata( virtElev )
    txt.set_visible(False)
    txt = plt.text(10, 20, 'CdA = ' + str(CdA), fontsize=20)
    plt.draw()
    plt.pause(0.01)

# Calculate CdA error
error = calcErrorOfCdA( virtElev, coef, res, CdA, m, g, Crr, rho, speed, power)
txt.set_visible(False)
txt = plt.text(10, 20, 'CdA = ' + str(CdA) + ' $\pm$' + str(error), fontsize=20)
plt.draw()
plt.pause(0.01)


plt.show(block=True)





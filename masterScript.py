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

plt.close('all')

# Set the parameters.

m = 80.0  # Mass of person + bike in kilograms (kg).
g = 9.81  # Acceleration due to gravity (ms^(-2)).
Crr = 0.006  # Coefficient of rolling resistance (approximately).
rho = 1.2922  # Air density (kgm^(-3)).

# This is the starting value of CdA
CdA = 0.2

# Get speed and power data from file (change file name if needed)
data = getTcxData( 'tcxFiles/2016-12-30_tt_bars_tucked.tcx' )
power = data[0]
speed = data[1]

# Get an initial figure ready
virtElev = calcVirtualElevation( CdA, m, g, Crr, rho, speed, power )
time = np.linspace(1,len(virtElev),len(virtElev))
plt.ion()

f, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot( time, np.zeros(len(time)), 'k:' )
line1 = ax1.plot( time, virtElev, 'r' )[0]
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Virtual Elevation (m)')
ax1.set_title('Virtual Elevation (VE)')
ax1.set_ylim([ min( virtElev ) - 15, max( virtElev ) + 15])
ax1.set_xlim([ 0, len( virtElev ) ] )
txt1 = ax1.text( 11, min(virtElev) - 8, 'CdA = ' + str( CdA ), fontsize=15 )


# Produce an initial linear regression
minima = findLocalMinima( virtElev )
coef, res = linearRegression( minima )
line2 = ax2.plot( minima )[0]
ax2.set_ylim([ minima[0] - 3, minima[0] + 3])
ax2.set_ylabel('Virtual Elevation (m)')
ax2.set_xlabel('Local Minimum')
ax2.set_title('Linear Regression of VE Minima')
txt2 = ax2.text( 0.2, minima[0]-2,'Regression slope = ' + str( round( coef, 3 ) ), fontsize=15 )


# Incrementally increase the CdA value until the slope of the
# minima of the virtual elevation is zero. This is when the
# CdA value is closest to the truth; this is due to the fact
# that the elevation of the lowest point in the road MUST be
# the same everytime.
while coef > 0.0 :

    # Increment CdA value and calculate new local minima of virtual elevation. Then
    # fit a linear model to the new local minima
    CdA += 0.0001
    virtElev = calcVirtualElevation( CdA, m, g, Crr, rho, speed, power )
    minima = findLocalMinima( virtElev )
    coef, res = linearRegression( minima )

    # Plot the virtual elevation using the new CdA value
    line1.set_ydata( virtElev )
    txt1.set_visible(False)
    txt1 = ax1.text(11, min(virtElev) - 8, 'CdA = ' + str(CdA), fontsize=15)

    # Plot the local minima with the regression slope value
    line2.set_ydata( minima )
    txt2.set_visible(False)
    txt2 = ax2.text( 0.2, minima[0] - 2, 'Regression slope = ' + str( round( coef, 3 ) ), fontsize=15 )

    plt.draw()
    plt.pause(0.01)

# Calculate CdA error
error = calcErrorOfCdA( virtElev, coef, res, CdA, m, g, Crr, rho, speed, power)
txt1.set_visible(False)
txt1a = ax1.text( 11, minima[0] - 8, 'CdA = ' + str(CdA), fontsize=15)
txt1b = ax1.text( 11, minima[0] - 11, '$\pm$' + str( error ), fontsize=15 )
plt.draw()
plt.pause(0.01)

# Change figure size
fig = plt.gcf()
fig.set_size_inches( 12, 6)


plt.show(block=True)





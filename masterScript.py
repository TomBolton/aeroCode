# This script computes the Chung analysis in order to estimate
# the CdA value from ride data. This is the same as the Golden
# Cheetah aerolab software, with one difference: instead of the
# user adjusting the CdA value to level the virtual elevation,
# a range of CdA values are used to see where the gradient of
# the virtual elevation is closest to zero.

import matplotlib.pyplot as plt
from calcSlope import calcSlope
from getTcxData import extractData
import pylab

# Get speed and power data from file.
data = extractData( 'test.tcx' )
power = data[0]
speed = data[1]

# Set the parameters.
m = 80.0                    # Mass of person + bike in kilograms (kg).
g = 9.81                    # Acceleration due to gravity (ms^(-2)).
Crr = 0.005                 # Coefficient of rolling resistance (approximately).
rho = 1.225                 # Air density (kgm^(-3)).
CdA = 0.18                 # Starting value of CdA (Boardman Superman Position).

s = [0]*( len( power ) - 2 )      # Pre-allocate for the slope and virtual elevation..
virtElev = [0]*( len( power ) - 2 )
sum = 0

for i in range(1,len(power)-1) :
    a = ( speed[i+1] - speed[i-1] )/2               # Calculate acceleration for this time-step.
    s[i-1] = calcSlope( m, g, Crr, rho, CdA, power[i], speed[i], a )  # Calculate the gradient at this time-step.
    sum = sum + s[i-1]*speed[i-1]
    virtElev[i-1] = sum           # Calculate virtual elevation from summing changes in elevation.

#plt.plot(virtElev)


pylab.show()



# This script takes the speed and power data, and calculates the
# virtual elevation usings the input parameters.

from calcSlope import calcSlope

def calcVirtualElevation( CdA, m, g, Crr, rho, speed, power ) :


    s = [0] * (len(power) - 2)  # Pre-allocate for the slope and virtual elevation..
    virtElev = [0] * (len(power) - 2)
    sum = 0

    for i in range(1, len(power) - 1):
        a = (speed[i + 1] - speed[i - 1]) / 2  # Calculate acceleration for this time-step.
        s[i - 1] = calcSlope(m, g, Crr, rho, CdA, power[i], speed[i], a)  # Calculate the gradient at this time-step.
        sum = sum + s[i - 1] * speed[i - 1]
        virtElev[i - 1] = sum  # Calculate virtual elevation from summing changes in elevation.

    return virtElev
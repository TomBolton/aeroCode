# This is a script which estimates the gradient of the road
# given the rider data (power, CdA, air density, etc). The formula
# can be found here:
#
# http://anonymous.coward.free.fr/wattage/cda/indirect-cda.pdf

def calcSlope( m, g, Crr, rho, CdA, p, v, a ) :
    slope = p/(m*g*v) - Crr - a/g - ( rho * CdA * v**2 )/(2*m*g)
    return slope
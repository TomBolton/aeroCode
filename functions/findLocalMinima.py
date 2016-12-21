# This script takes a list of real values and finds the locations
# of all local minima. The list of values is first smooth to reduce
# noise and only return more 'legitimate' local minima. The function
# returns the values of the list, at the minima.

import numpy as np

def findLocalMinima( list ) :
    # First use a running average to smooth the data.
    # This is done using the numpy function 'convolve'
    smoothList = np.convolve( list, np.ones(5)/5 )

    # Loop through the values in the list, and see if it's nearest
    # neighbours are greater in value. If so, store the value
    localMinima = []
    x = []
    for i in range(1, len(list)-1 ) :
        if smoothList[i] < smoothList[i-1] and smoothList[i] < smoothList[i+1] :
            localMinima.append( smoothList[i] )
            x.append( i )

    return localMinima




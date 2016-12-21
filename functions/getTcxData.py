# This script will extract the important ride data from a .tcx
# file specified by the user. The code below will then extract
# the speed and power values at each time step. The data recording
# of the Garmin MUST be set to one data point per second, as the
# analysis assumes a time-step of 1 second.

import lxml.etree as ET
import os
from os import path

def getTcxData( fileName ) :       # Input is the filename, e.g. my_ride.tcx.

    # Make a string of the path to the tcx file.
    pathStr = str( path.realpath( fileName ) )

    # Read .tcx file into a Document Object Model (DOM).
    dom = ET.parse( pathStr )
    root = dom.getroot()

    # We're interested in the distance travelled and watts. The route to
    # watts is the following:
    #
    # <Element>
    #   <TraingCenterDatabase ...>
    #       <Activities>
    #           <Activity Sport="Biking">
    #               <Lap StartTime="...">
    #                  <Track>
    #                      <Trackpoint>
    #                           <Extensions>
    #

    trackPoints = root[0][0][1][9]      # This extracts the moment-by-moment data from the xml tree.

    powerList = []
    speedList = []

    for i in range(2,len(trackPoints)-1) :
        powerList.append( int( trackPoints[i][7][0][0].text ) )
        speedList.append( float( trackPoints[i][3].text ) - float( trackPoints[i-1][3].text ) )

    # The turning around points sometimes register as zero speed even though
    # the cyclist is still moving. Therefore replace the zero values with a
    # small value of 0.5m/s.
    for i in range(0, len(speedList)) :
        if speedList[i] < 0.2 :
            speedList[i] = 0.5

    return [powerList,speedList]


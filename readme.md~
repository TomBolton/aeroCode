Author: Tom Bolton
Contact: thomasmichaelbolton@gmail.com
Data: 21/12/2016
Repository: aeroCode

---

![alt text](https://github.com/TomBolton/aeroCode/blob/master/aeroCode_screenshot.png "Screenshot of Chung analysis using aeroCode")

This collection of Python scripts takes a .tcx file recorded by some GPS tracking device (e.g. Garmin) while cycling according to the Chung method protocol; for more information on the Chung method, see http://anonymous.coward.free.fr/wattage/cda/indirect-cda.pdf. 

The code assumes the ride is a 'half-pipe' ride, where you repeatedly cycle in and out of a dip in the road. You should NOT use your brakes during the ride, nor significantly change your position during the recording of the .tcx file. You should also aim to complete the ride on a stretch of road with very little traffic and low wind. If you cannot avoid strong winds, then at least complete the ride on a day where the wind is consistent i.e. little variability in time.

The code then computes the Chung analysis in order to estimate the CdA value. In order to use these scripts, you only want to open 'masterScript.py', and follow the following instructions:

1.) Change the mass (m), rolling resistance (Crr) and air density (rho) to match your specific situation. There are many air density calculators on the internet (for example https://www.gribble.org/cycling/air_density.html).

2.) Within the 'extractData' function, change the  name of the tcx file to the file you want to analyse. You should put all your .tcx files in the tcxFiles folder.

3.) Run 'masterScript.py'. What the code will do is start at some low value of CdA, and keep incrementally increasing it until the virtual elevation profile is level. In order to quantify how 'level' the elevation profile is, the local minima are calculated and a linear regression is used to estimate the slope. When the slop reaches zero, the loop stops and the CdA value is now optimized.

4.) Finally, the error of the CdA value is estimated using the residuals from the linear regression. Run the script again on multiple .tcx files in order to compare CdA values. If two CdA values and within the error bounds of each other, then there's a chance that their differences were likely due to random chance.

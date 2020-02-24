"""
Written by Daniel Isenberg in Intellij Idea using Python community plugin.
Full project repository is available at https://github.com/Chronographer/bicycleSimulator

This file serves as a single location from which all other components of this project can be easily called by changing
which file/function you are calling. It also serves as a unified location from which a plot can be shown, so that plots
from multiple different functions can be overlaid on top of each other. Note that the axis and plot titles will not
update automatically when changing which function you are calling, and must be changed at the bottom of this file.

All functions in this project assume the rider is on flat ground.
All values are expressed as standard SI units unless otherwise noted.
"""

import matplotlib.pyplot as plt
import bicycleDragMass
import bicycle_lossless
import bicycleDragAreaTrend
import bicycleDragArea
import bicycleDragPowerSearch

#bicycle_lossless.run()
#bicycleDragMass.run()
#bicycleDragArea.run()
#bicycleDragAreaTrend.run()
bicycleDragPowerSearch.run()

plt.suptitle("Power required to reach a speed of 13 m/s as area increases")
plt.xlabel("Cross sectional area (m^2)")
plt.ylabel("Power required to reach speed of 13 m/s (watts)")
plt.grid()
plt.show()

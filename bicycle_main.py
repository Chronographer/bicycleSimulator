import bicycleDragMass
import bicycle_lossless
import bicycleDragArea
import matplotlib.pyplot as plt

#bicycleDragMass.bicycleMass()
bicycleDragArea.bicycleArea()
#bicycle_lossless.bicycleLossless()

plt.suptitle("Bicycle terminal velocity with varying cross sectional area")
plt.xlabel("Cross sectional area (m^2)")
plt.ylabel("Final Velocity (m/s)")
#plt.legend(loc="best")
#plt.legend(fontsize="small")
plt.grid()
plt.show()

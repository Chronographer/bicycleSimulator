import bicycleDragMass
import bicycle_lossless
import bicycleDragAreaTrend
import bicycleDragArea
import bicycleDragPowerSearch
import matplotlib.pyplot as plt

#bicycleDragMass.bicycleMass()
#bicycleDragAreaTrend.run()
#bicycleDragArea.run()
#bicycle_lossless.bicycleLossless()
bicycleDragPowerSearch.run()

plt.suptitle("Power required to reach a speed of 13 m/s as area increases")
plt.xlabel("Power required to reach speed of 13 m/s (watts)")
plt.ylabel("Cross sectional area (m^2)")
plt.legend(loc="best")
#plt.legend(fontsize="small")
plt.grid()
plt.show()

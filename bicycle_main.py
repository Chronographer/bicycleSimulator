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

plt.suptitle("Comparison of terminal velocities between leading and trailing cyclists")
plt.xlabel("Time (sec)")
plt.ylabel("Velocity (m/s)")
plt.legend(loc="best")
#plt.legend(fontsize="small")
plt.grid()
plt.show()

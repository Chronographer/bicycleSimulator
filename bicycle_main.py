import bicycleDragMass
import bicycle_lossless
import bicycleDragArea
import matplotlib.pyplot as plt

#bicycleDragMass.bicycleMass()
bicycleDragArea.bicycleArea()
#bicycle_lossless.bicycleLossless()

plt.suptitle("Bicycle velocity with varying area")
plt.xlabel("Time (sec)")
plt.ylabel("Velocity (m/s)")
plt.legend(loc="best")
plt.legend(fontsize="small")
plt.grid()
plt.show()

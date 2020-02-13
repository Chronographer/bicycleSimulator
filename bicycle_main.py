import bicycleDrag
import bicycle_lossless
import matplotlib.pyplot as plt

bicycleDrag.bicycleDrag()
bicycle_lossless.bicycleLossless()

plt.suptitle("Bicycle Velocity vs. Time")
plt.xlabel("Time (sec)")
plt.ylabel("Velocity (m/s)")
plt.legend(loc="best")
plt.legend(fontsize="small")
plt.grid()
plt.show()

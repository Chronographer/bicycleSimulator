"""
Written by Daniel Isenberg in Intellij Idea using Python community plugin.
1-31-2020
Bicycle motion simulator: Uses a numerical approach to predict and plot the
velocity of a bicycle and rider for a period of time given the mass of the
bike and rider, the sustained power produced by the rider, the initial
velocity of the bike and rider, the bike and riders cross sectional area,
the air density, and the drag coefficient of the bike and rider.

This program assumes the rider is on flat ground.
Unless otherwise noted all values are expressed in standard SI units
"""
import matplotlib.pyplot as plt

powerOutput = 400.0
dragCoefficient = 0.5
crossSectionArea = 0.33
airDensity = 1.2
initialVelocity = 4.0
dragVelocity = initialVelocity
timeStep = 0.1
maxTime = 200.0
initialTime = 0.0
currentTime = initialTime
tableIndex = 0

timeDataList = []
dragVelocityDataList = []
massTable = [70, 75, 399]
labelTable = []
for i in range(0, len(massTable)):
    label = "mass = " + str(massTable[i]) + " kg"
    labelTable.append(label)

while tableIndex <= len(massTable) - 1:
    while currentTime <= maxTime:
        if currentTime == initialTime:
            timeDataList.append(initialTime)
            dragVelocityDataList.append(dragVelocity)

        mass = massTable[tableIndex]
        dragVelocity = dragVelocity + ((powerOutput / (mass * dragVelocity)) - ((dragCoefficient * airDensity * crossSectionArea * dragVelocity**2)/(2*mass))) * timeStep
        currentTime = currentTime + timeStep
        dragVelocityDataList.append(dragVelocity)
        timeDataList.append(currentTime)
        #print(currentTime, dragVelocity)
    plt.plot(timeDataList, dragVelocityDataList, label=labelTable[tableIndex])

    tableIndex = tableIndex + 1
    currentTime = initialTime
    dragVelocity = initialVelocity
    dragVelocityDataList.clear()
    timeDataList.clear()

plt.suptitle("Bicycle Velocity vs. Time")
plt.xlabel("Time (sec)")
plt.ylabel("Velocity (m/s)")
plt.legend(loc="best")
plt.legend(fontsize="small")
plt.grid(True)
plt.show()

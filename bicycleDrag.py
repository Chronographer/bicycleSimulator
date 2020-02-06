"""
Written by Daniel Isenberg in Intellij Idea using Python community plugin.
1-31-2020
Bicycle motion simulator: Predicts the velocity of a bicycle and rider given
the mass of the bike and rider, the sustained power produced by the rider, and
the initial velocity of the bike and rider using a numerical approach. Also
simultaneously computes the velocity of the bike and rider using an analytical
method at each time step. Program will then graph the two lists of data points
against each other. This program does not account for any wind resistance or
losses of any kind, and assumes the rider is on flat ground.

Unless otherwise noted all values are expressed in standard SI units
"""
import matplotlib.pyplot as plt


powerOutput = 400.0
dragCoefficient = 0.5
crossSectionArea = 0.33
airDensity = 1.2
initialVelocity = 4.0
losslessVelocity = initialVelocity
dragVelocity = initialVelocity
timeStep = 0.1
maxTime = 200.0
initialTime = 0.0
currentTime = initialTime
tableIndex = 0


timeDataList = []
losslessVelocityDataList = []
dragVelocityDataList = []
massTable = [70, 75, 100, 65, 200, 645]
labelTable = []

for i in range(0, len(massTable)):
    label = "mass = " + str(massTable[i]) + " kg"
    labelTable.append(label)

while tableIndex <= len(massTable) - 1:
    while currentTime <= maxTime:
        if currentTime == initialTime:
            timeDataList.append(initialTime)
            losslessVelocityDataList.append(losslessVelocity)
            dragVelocityDataList.append(dragVelocity)
        mass = massTable[tableIndex]
        losslessVelocity = losslessVelocity + (powerOutput / (mass * losslessVelocity)) * timeStep
        dragVelocity = dragVelocity + ((powerOutput / (mass * dragVelocity)) - ((dragCoefficient * airDensity * crossSectionArea * dragVelocity**2)/(2*mass))) * timeStep

        currentTime = currentTime + timeStep
        timeDataList.append(currentTime)
        losslessVelocityDataList.append(losslessVelocity)
        dragVelocityDataList.append(dragVelocity)
        #print(currentTime, losslessVelocity, dragVelocity)

    plt.plot(timeDataList, losslessVelocityDataList, label=labelTable[tableIndex])
    plt.plot(timeDataList, dragVelocityDataList, label=labelTable[tableIndex] + " with drag")

    tableIndex = tableIndex + 1
    currentTime = initialTime
    dragVelocity = initialVelocity
    losslessVelocity = initialVelocity
    dragVelocityDataList.clear()
    losslessVelocityDataList.clear()
    timeDataList.clear()

plt.legend(loc="best")
plt.legend(fontsize="small")
plt.xlabel("Time (sec)")
plt.ylabel("Velocity (m/s)")
plt.grid(True)
plt.show()



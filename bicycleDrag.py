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
massTable = [70, 75]
labelTable = []
for i in range(0, len(massTable)):
    label = "mass = " + str(massTable[i]) + " kg"
    labelTable.append(label)

showLossless = True
showDrag = True

while tableIndex <= len(massTable) - 1:

    if showDrag == True:
        while currentTime <= maxTime:
            if currentTime == initialTime:
                timeDataList.append(initialTime)
                dragVelocityDataList.append(dragVelocity)
            mass = massTable[tableIndex]
            dragVelocity = dragVelocity + ((powerOutput / (mass * dragVelocity)) - ((dragCoefficient * airDensity * crossSectionArea * dragVelocity**2)/(2*mass))) * timeStep
            dragVelocityDataList.append(dragVelocity)
            currentTime = currentTime + timeStep
            timeDataList.append(currentTime)
            #print(currentTime, dragVelocity)
        plt.plot(timeDataList, dragVelocityDataList, label=labelTable[tableIndex])
        tableIndex = tableIndex + 1
        currentTime = initialTime
        dragVelocity = initialVelocity
        dragVelocityDataList.clear()
        timeDataList.clear()

    if showLossless == True:
        while currentTime <= maxTime:
            if currentTime == initialTime:
                timeDataList.append(initialTime)
                losslessVelocityDataList.append(losslessVelocity)
            mass = massTable[tableIndex]
            losslessVelocity = losslessVelocity + (powerOutput / (mass * losslessVelocity)) * timeStep
            losslessVelocityDataList.append(losslessVelocity)
            currentTime = currentTime + timeStep
            timeDataList.append(currentTime)
            #print(currentTime, losslessVelocity)
        plt.plot(timeDataList, losslessVelocityDataList, label=labelTable[tableIndex])
        tableIndex = tableIndex + 1
        currentTime = initialTime
        losslessVelocity = initialVelocity
        losslessVelocityDataList.clear()
        timeDataList.clear()


if showLossless == True and showDrag == True:
    plt.suptitle("Velocity vs. Time (drag and lossless)")
elif showLossless == True and showDrag == False:
    plt.suptitle("Velocity vs. Time (lossless only)")
elif showLossless == False and showDrag == True:
    plt.suptitle("Velocity vs. Time (drag only")
else:
    plt.suptitle("Congratulations! You made an empty graph!")
plt.xlabel("Time (sec)")
plt.ylabel("Velocity (m/s)")
plt.legend(loc="best")
plt.legend(fontsize="small")
plt.grid(True)
plt.show()
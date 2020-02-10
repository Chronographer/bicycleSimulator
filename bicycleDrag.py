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
dragCoefficient = 1.0
crossSectionArea = 0.33
airDensity = 1.2
initialVelocity = 4.0
dragVelocity = initialVelocity
timeStep = 0.1
maxTime = 6000.0
initialTime = 0.0
currentTime = initialTime
tableIndex = 0

terminalFlag = False
lastVelocity = 0
deltaVelocity = 0
terminalVelocityBaseline = 999999

timeDataList = []
dragVelocityDataList = []
massTable = [70.0, 4845.0, 5647.5]
labelTable = []
for i in range(0, len(massTable)):  # This automatically populates the table that holds the labels for each line shown in the plot with both the correct number of elements and the values for each of those elements.
    label = "mass = " + str(massTable[i]) + " kg"
    labelTable.append(label)

while tableIndex <= len(massTable) - 1:
    while currentTime <= maxTime:
        if currentTime == initialTime:
            timeDataList.append(initialTime)
            dragVelocityDataList.append(dragVelocity)

        mass = massTable[tableIndex]
        lastVelocity = dragVelocity

        dragVelocity = dragVelocity + ((powerOutput / (mass * dragVelocity)) - ((dragCoefficient * airDensity * crossSectionArea * dragVelocity**2)/(2*mass))) * timeStep
        currentTime = currentTime + timeStep
        dragVelocityDataList.append(dragVelocity)
        timeDataList.append(currentTime)

        deltaVelocity = dragVelocity - lastVelocity
        if (deltaVelocity < 0.0001) and (terminalFlag == False) and (mass == massTable[0]):
            terminalVelocityBaseline = dragVelocity
            print("Terminal velocity of " + str(terminalVelocityBaseline) + " m/s for a mass of " + str(mass) + " kg detected after " + str(currentTime) + " seconds")
            terminalFlag = True

        elif dragVelocity >= terminalVelocityBaseline and terminalFlag == False:
            terminalFlag = True
            print("Terminal velocity for a mass of " + str(mass) + " kg reached in " + str(currentTime) + " seconds")

        #print(currentTime, dragVelocity)
    plt.plot(timeDataList, dragVelocityDataList, label=labelTable[tableIndex])

    terminalFlag = False
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

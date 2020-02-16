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


def run():
    import matplotlib.pyplot as plt

    powerOutput = 400.0
    dragCoefficient = 1.0
    airDensity = 1.2
    mass = 70.0
    initialVelocity = 4.0
    dragVelocity = initialVelocity
    timeStep = 0.1
    maxTime = 150.0
    initialTime = 0.0
    currentTime = initialTime

    timeDataList = []
    dragVelocityDataList = []
    finalSpeedList = []
    areaTable = [0.33, 0.1]
    descriptionTable = ["Leading cyclist", "Trailing cyclist"]

    labelTable = []
    for i in range(0, len(areaTable)):  # This automatically populates the table that holds the labels for each line shown in the plot with both the correct number of elements and the values for each of those elements.
        label = "cross section = " + str(areaTable[i]) + " m^2"
        labelTable.append(label)

    for i in range(0, len(areaTable)):
        while currentTime <= maxTime:
            if currentTime == initialTime:
                timeDataList.append(initialTime)
                dragVelocityDataList.append(dragVelocity)

            crossSectionArea = areaTable[i]

            dragVelocity = dragVelocity + ((powerOutput / (mass * dragVelocity)) - ((dragCoefficient * airDensity * crossSectionArea * dragVelocity**2)/(2*mass))) * timeStep
            currentTime = currentTime + timeStep
            dragVelocityDataList.append(dragVelocity)
            timeDataList.append(currentTime)
            if currentTime >= maxTime:
                #print("cross section is: " + str(areaTable[i]) + ". Time is: " + str(currentTime) + ". Final velocity is: " + str(dragVelocity))
                finalSpeedList.append(dragVelocity)
        plt.plot(timeDataList, dragVelocityDataList, label=descriptionTable[i] + " (" + labelTable[i] + ")")
        currentTime = initialTime
        dragVelocity = initialVelocity
        dragVelocityDataList.clear()
        timeDataList.clear()
    #plt.plot(areaTable, finalSpeedList, label="mass: 70 kg\npower: 400 watts\ndrag coefficient: 1\nair density: 1.2 kg/m^3\ntime step: 0.1 seconds")


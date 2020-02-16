def run():
    import matplotlib.pyplot as plt

    powerOutput = 400.0
    dragCoefficient = 1.0
    airDensity = 1.2
    mass = 70.0
    initialVelocity = 4.0
    dragVelocity = initialVelocity
    targetSpeed = 13.0
    finalVelocity = 0.0
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
            while finalVelocity < targetSpeed:
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
                    finalVelocity = dragVelocity
                    print("power is: " + str(powerOutput) + ". final speed is: " + str(finalVelocity))
                    if finalVelocity < targetSpeed:
                        powerOutput = powerOutput + 1
        plt.plot(timeDataList, dragVelocityDataList, label=descriptionTable[i] + " (" + labelTable[i] + ")")
        currentTime = initialTime
        dragVelocity = initialVelocity
        dragVelocityDataList.clear()
        timeDataList.clear()

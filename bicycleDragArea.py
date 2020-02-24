"""
Written by Daniel Isenberg in Intellij Idea using Python community plugin.
Full project repository is available at https://github.com/Chronographer/bicycleSimulator

This function computes the velocity over time for multiple systems with different cross sectional areas. A plot of
velocity vs. time will be generated for each value in areaList[] and plotted on the same graph.
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
    areaList = [0.33, 1.2]

    labelList = []
    for i in range(0, len(areaList)):  # This automatically populates the table that holds the labels for each line shown in the plot with both the correct number of elements and the values for each of those elements.
        label = "cross section = " + str(areaList[i]) + " m^2"
        labelList.append(label)

    for i in range(0, len(areaList)):
        while currentTime <= maxTime:
            if currentTime == initialTime:
                timeDataList.append(initialTime)
                dragVelocityDataList.append(dragVelocity)

            crossSectionArea = areaList[i]

            dragVelocity = dragVelocity + ((powerOutput / (mass * dragVelocity)) - ((dragCoefficient * airDensity * crossSectionArea * dragVelocity**2)/(2*mass))) * timeStep
            currentTime = currentTime + timeStep
            dragVelocityDataList.append(dragVelocity)
            timeDataList.append(currentTime)
            if currentTime >= maxTime:
                finalSpeedList.append(dragVelocity)
        plt.plot(timeDataList, dragVelocityDataList, label=labelList[i])
        currentTime = initialTime
        dragVelocity = initialVelocity
        dragVelocityDataList.clear()
        timeDataList.clear()

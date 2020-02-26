"""
Written by Daniel Isenberg in Intellij Idea using the Python community plugin.
Full project repository is available at https://github.com/Chronographer/bicycleSimulator

This function computes the velocity of a bicycle over time (taking atmospheric drag into consideration) given a
sustained power output, a drag coefficient, the cross sectional area of the system, the density of the air, and the
initial velocity of the system.
"""


def run():
    import matplotlib.pyplot as plt

    powerOutput = 400.0
    dragCoefficient = 1.0
    crossSectionArea = 0.33
    airDensity = 1.2
    initialVelocity = 4.0
    dragVelocity = initialVelocity
    timeStep = 0.1
    maxTime = 60.0
    initialTime = 0.0

    currentTime = initialTime

    timeDataList = []
    dragVelocityDataList = []
    massList = [65.0, 70.0, 75.0, 80.0]
    labelList = []
    for i in range(0, len(massList)):  # This automatically populates the table that holds the labels for each line shown in the plot with both the correct number of elements and the values for each of those elements.
        label = "mass = " + str(massList[i]) + " kg"
        labelList.append(label)

    for i in range(0, len(massList)):
        while currentTime <= maxTime:
            if currentTime == initialTime:
                timeDataList.append(initialTime)
                dragVelocityDataList.append(dragVelocity)

            mass = massList[i]
            dragVelocity = dragVelocity + ((powerOutput / (mass * dragVelocity)) - ((dragCoefficient * airDensity * crossSectionArea * dragVelocity**2)/(2*mass))) * timeStep
            currentTime = currentTime + timeStep
            dragVelocityDataList.append(dragVelocity)
            timeDataList.append(currentTime)
            # print(currentTime, dragVelocity)
        plt.plot(timeDataList, dragVelocityDataList, label=labelList[i])
        currentTime = initialTime
        dragVelocity = initialVelocity
        dragVelocityDataList.clear()
        timeDataList.clear()

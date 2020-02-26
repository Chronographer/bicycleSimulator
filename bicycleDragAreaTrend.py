"""
Written by Daniel Isenberg in Intellij Idea using the Python community plugin.
Full project repository is available at https://github.com/Chronographer/bicycleSimulator

This function plots the trend between the cross sectional area of the system and that systems terminal velocity by
computing the velocity reached after an elapsed time of maxTime seconds for each value of the cross sectional area in
areaList[]. Note that they y-axis represents only the FINAL velocity of a system after maxTime seconds, and the x-axis
represents the cross sectional area of a system, NOT time. In other words, each point on the plot represents the
velocity after a given period of time for a particular system, as opposed to the velocity over time of a single system.
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
    maxTime = 120.0
    initialTime = 0.0
    currentTime = initialTime

    timeDataList = []
    dragVelocityDataList = []
    finalSpeedList = []
    areaList = []
    counter = 0
    areaStep = 0.2

    while counter <= 10.0:  # Used to populate the areaList with values that get increasingly larger
        areaList.append(counter)
        counter = counter + areaStep

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
        currentTime = initialTime
        dragVelocity = initialVelocity
        dragVelocityDataList.clear()
        timeDataList.clear()
    plt.plot(areaList, finalSpeedList, label="mass: 70 kg\npower: 400 watts\ndrag coefficient: 1\nair density: 1.2 kg/m^3\ntime step: 0.1 seconds")

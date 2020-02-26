"""
Written by Daniel Isenberg in Intellij Idea using the Python community plugin.
Full project repository is available at https://github.com/Chronographer/bicycleSimulator

This function identifies how much power is required for a system to reach a velocity of targetVelocity within maxTime
seconds as the cross sectional area of that system is gradually increased. The graph produced plots the power required
to reach the target velocity against the cross sectional area of the system.
"""


def run():
    import matplotlib.pyplot as plt
    initialPower = 1.0
    powerOutput = initialPower
    dragCoefficient = 1.0
    airDensity = 1.2
    mass = 70.0
    initialVelocity = 4.0
    targetSpeed = 13.0
    timeStep = 0.1
    maxTime = 150.0
    initialTime = 0.0

    finalSpeedList = []
    powerList = []
    areaList = []
    areaTablePopulator = 0.01
    while areaTablePopulator < 0.34:
        areaList.append(areaTablePopulator)
        areaTablePopulator = areaTablePopulator + 0.01

    for i in range(0, len(areaList)):
        crossSectionArea = areaList[i]
        currentTime = initialTime
        dragVelocity = initialVelocity

        while currentTime <= maxTime:
            dragVelocity = dragVelocity + ((powerOutput / (mass * dragVelocity)) - ((dragCoefficient * airDensity * crossSectionArea * dragVelocity**2)/(2*mass))) * timeStep
            currentTime = currentTime + timeStep
            if currentTime >= maxTime:
                if dragVelocity >= targetSpeed:
                    finalSpeedList.append(dragVelocity)
                    powerList.append(powerOutput)
                    #print("power is: " + str(powerOutput) + ". final speed is: " + str(dragVelocity) + ". current area is: " + str(crossSectionArea))
                if dragVelocity < targetSpeed:
                    #print("target velocity not reached! power is: " + str(powerOutput) + ". current velocity is: " + str(dragVelocity) + ". currentTime is: " + str(currentTime) + ". current area is: " + str(crossSectionArea))
                    powerOutput = powerOutput + 1
                    currentTime = initialTime
    plt.plot(areaList, powerList, label="mass: 70 kg\ndrag coefficient: 1\ninitialVelocity: 4.0 m/s\nair density: 1.2 kg/m^3\ntimeStep: 0.1 seconds")

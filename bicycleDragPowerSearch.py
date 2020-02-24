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
    areaTable = []
    areaTablePopulator = 0.01
    while areaTablePopulator < 0.34:
        areaTable.append(areaTablePopulator)
        areaTablePopulator = areaTablePopulator + 0.01

    for i in range(0, len(areaTable)):
        crossSectionArea = areaTable[i]
        currentTime = initialTime
        dragVelocity = initialVelocity

        while currentTime <= maxTime:
            dragVelocity = dragVelocity + ((powerOutput / (mass * dragVelocity)) - ((dragCoefficient * airDensity * crossSectionArea * dragVelocity**2)/(2*mass))) * timeStep
            currentTime = currentTime + timeStep
            if currentTime >= maxTime:
                if dragVelocity >= targetSpeed:
                    finalSpeedList.append(dragVelocity)
                    powerList.append(powerOutput)
                    print("power is: " + str(powerOutput) + ". final speed is: " + str(dragVelocity) + ". current area is: " + str(crossSectionArea))
                if dragVelocity < targetSpeed:
                    #print("target velocity not reached! power is: " + str(powerOutput) + ". current velocity is: " + str(dragVelocity) + ". currentTime is: " + str(currentTime) + ". current area is: " + str(crossSectionArea))
                    powerOutput = powerOutput + 1
                    currentTime = initialTime
    plt.plot(powerList, areaTable, label="mass: 70 kg\ndrag coefficient: 1\ninitialVelocity: 4.0 m/s\nair density: 1.2 kg/m^3\ntimeStep: 0.1 seconds")

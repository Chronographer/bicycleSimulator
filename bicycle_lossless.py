"""
Written by Daniel Isenberg in IntelliJ Idea using Python community plugin. 1-31-2020
Bicycle motion simulator: Predicts the velocity of a bicycle and rider given
the mass of the bike and rider, the sustained power produced by the rider, and
the initial velocity of the bike and rider using a numerical approach. Also
simultaneously computes the velocity of the bike and rider using an analytical
method at each timestep. Program will then graph the two lists of data points
against each other. This program does not account for any wind resistance or
losses of any kind, and assumes the rider is on flat ground.

Unless otherwise noted all values are expressed in standard SI units
"""
def bicycleLossless():
    import matplotlib.pyplot as plt
    import numpy

    # initial values
    mass = 70.0
    powerOutput = 400.0
    initialVelocity = 4.0
    initialTime = 0.0
    maxTime = 90.0
    timeStep = 0.1

    currentVelocity = initialVelocity
    theoreticalVelocity = initialVelocity
    currentTime = initialTime

    timeDataList = []
    computationalVelocityDataList = []
    analyticalVelocityDataList = []

    computationalVelocityDataList.append(currentVelocity) # these three operations are here so that the initial point is plotted.
    analyticalVelocityDataList.append(theoreticalVelocity)
    timeDataList.append(currentTime)

    while currentTime <= maxTime:
        currentVelocity = currentVelocity + (powerOutput / (mass * currentVelocity)) * timeStep
        theoreticalVelocity = numpy.sqrt(initialVelocity ** 2 + 2.0 * powerOutput * currentTime / mass)
        currentTime = currentTime + timeStep
        timeDataList.append(currentTime)
        computationalVelocityDataList.append(currentVelocity)
        analyticalVelocityDataList.append(theoreticalVelocity)
        #print(currentTime, currentVelocity, theoreticalVelocity) # uncomment this line to print out the results to the terminal.
    plt.suptitle("Analytical vs. computational calculation of bicycle speed")
    plt.plot(timeDataList, computationalVelocityDataList, label="Computational")
    plt.plot(timeDataList, analyticalVelocityDataList, label="Theoretical")
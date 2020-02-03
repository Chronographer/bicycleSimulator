"""
Written by Daniel Isenberg in IntelliJ Idea using Python community plugin.
1-31-2020
Bicycle motion simulator: Predicts the velocity of a bicycle and rider given
the mass of the bike and rider, the sustained power produced by the rider, and
the initial velocity of the bike and rider using a numerical approach. Also
simultaneously computes the velocity of the bike and rider using an analytical
method at each timestep. Program will then graph the two lists of data points
against each other. This program does not account for any wind resistance or
losses of any kind, and assumes the rider is on flat ground.

Unless otherwise noted all values are expressed in standard SI units
"""
import matplotlib.pyplot as plt
import numpy

# initial values
mass = 70.0
powerOutput = 400.0
initialVelocity = 1.0
currentVelocity = initialVelocity
theoreticalVelocity = initialVelocity
timeStep = 0.01
maxTime = 5.0
initialTime = 0.0
currentTime = initialTime

timeDataList = []
computationalVelocityDataList = []
analyticalVelocityDataList = []

# Euler loop
while currentTime <= maxTime:
    currentVelocity = currentVelocity + (powerOutput / (mass * currentVelocity)) * timeStep
    theoreticalVelocity = numpy.sqrt(initialVelocity ** 2 + 2.0 * powerOutput * currentTime / mass)
    currentTime = currentTime + timeStep
    timeDataList.append(currentTime)
    computationalVelocityDataList.append(currentVelocity)
    analyticalVelocityDataList.append(theoreticalVelocity)
    #print(currentTime, currentVelocity, theoreticalVelocity)
plt.xlabel("Time (sec)")
plt.ylabel("Velocity (m/s)")
plt.grid(True)
plt.plot(timeDataList, computationalVelocityDataList, label="Computational")
plt.plot(timeDataList, analyticalVelocityDataList, label="Theoretical")
plt.legend(loc="center right")
plt.show()

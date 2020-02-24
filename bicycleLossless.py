"""
Written by Daniel Isenberg in Intellij Idea using Python community plugin.
1-31-2020
Full project repository is available at https://github.com/Chronographer/bicycleSimulator

DEPRECATED: use "bicycle_lossless.py" instead. This file is included only for the sake of completeness, and can not
be called from bicycle_main.py the way the other files can. It is functionally equivalent to "bicycle_lossless.py"

Bicycle motion simulator: Predicts the velocity of a bicycle and rider given the mass of the bike and rider, the
sustained power produced by the rider, and the initial velocity of the bike and rider using a numerical approach. Also
simultaneously computes the velocity of the bike and rider using an analytical method at each time step. Program will
then graph the two lists of data points against each other.
"""
import matplotlib.pyplot as plt
import numpy

# initial values
mass = 70.0
powerOutput = 400.0
initialVelocity = 1.0
currentVelocity = initialVelocity
theoreticalVelocity = initialVelocity
timeStep = 0.1
maxTime = 200.0
initialTime = 0.0
currentTime = initialTime
netForce = 0.0
riderForce = 0.0

timeDataList = []
computationalVelocityDataList = []
analyticalVelocityDataList = []

timeDataList.append(initialTime)
computationalVelocityDataList.append(currentVelocity)
analyticalVelocityDataList.append(theoreticalVelocity)

# Euler loop
while currentTime <= maxTime:
    currentVelocity = currentVelocity + (powerOutput / (mass * currentVelocity)) * timeStep
    theoreticalVelocity = numpy.sqrt(initialVelocity ** 2 + 2.0 * powerOutput * currentTime / mass)
    currentTime = currentTime + timeStep
    timeDataList.append(currentTime)
    computationalVelocityDataList.append(currentVelocity)
    analyticalVelocityDataList.append(theoreticalVelocity)
    # print(currentTime, currentVelocity, theoreticalVelocity)
plt.xlabel("Time (sec)")
plt.ylabel("Velocity (m/s)")
plt.grid(True)
plt.plot(timeDataList, computationalVelocityDataList, label="Computational")
plt.plot(timeDataList, analyticalVelocityDataList, label="Theoretical")
plt.legend(loc="center right")
plt.show()

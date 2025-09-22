import math
n = float(input())

root2pi = math.sqrt(2*math.pi)
nPower = n**(n+0.5)
lowerPower = -n + (1 / (12*n + 1))
ePowerLower = math.e ** (lowerPower)
upperPower = -n + (1 / (12*n))
ePowerUpper = math.e**(upperPower)

lower = root2pi*nPower*ePowerLower
upper = root2pi*nPower*ePowerUpper

print(lower)
print(upper)

import math
first = math.pi
second = math.factorial(10)/(8**8)
thirdPowerOne = 7 / (math.sqrt(71))
thirdPowerTwo = math.sin(40 * (math.pi/180)) # .sin() uses radians
thirdPower = thirdPowerOne - thirdPowerTwo
thirdSub = math.log(9.7,math.e)
third = thirdSub**(thirdPower)
numerator = first - second + third
denominator = 1.2**(2.3**(1/3))

answer = round(numerator/denominator,6)
print(answer)

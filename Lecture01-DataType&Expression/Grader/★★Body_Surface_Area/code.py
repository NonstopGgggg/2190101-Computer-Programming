import math
weight = float(input()) # in kg
height = float(input()) # in cm

monsteller = ((weight*height)**(1/2))/60
haycock = 0.024265 * (weight**0.5378) * (height**0.3964)
boydComponent = 0.6157 - 0.0188 * math.log(weight,10)
boyd = 0.0333 * (weight**boydComponent) * (height**0.3)

print(monsteller)
print(haycock)
print(boyd)

from math import sqrt
a = float(input())
b = float(input())
c = float(input())

denominator = 2*a

x1 = round((-b + sqrt((b*b) - 4*a*c)) / denominator,3)
x2 = round((-b - sqrt((b*b) - 4*a*c)) / denominator,3)

print(x2, x1)

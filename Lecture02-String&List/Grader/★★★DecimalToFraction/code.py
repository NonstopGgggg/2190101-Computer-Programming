import math
num = input().split(",")
num = ["0" if i == "0" else i for i in num]

frac1 = int(num[0] + num[1] + num[2]) - int(num[0] + num[1])
frac2 = int("9" * int(len(num[2])) + "0" * int(len(num[1])))

g = math.gcd(frac1, frac2)

print(frac1//g,"/",frac2//g)

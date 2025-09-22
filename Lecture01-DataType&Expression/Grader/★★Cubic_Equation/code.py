import math
coef = list(map(float,input().split()))
a = coef[0]
b = coef[1]
c = coef[2]
d = coef[3]

innerRootValueOne = 2*(b**3) - 9*a*b*c + 27*(a**2)*d
innerRootValueTwo = 4 * (b**2 - 3*a*c)**3
innerRootValue = math.sqrt(innerRootValueOne**2 - innerRootValueTwo)
innerRootPositive = 0.5 * (innerRootValueOne + innerRootValue)
innerRootNegative = 0.5 * (innerRootValueOne - innerRootValue)
rootPositive = innerRootPositive**(1/3)
rootNegative = innerRootNegative**(1/3)
negativeAnswer = ((-1)/(3*a)) * rootNegative
positiveAnswer = (-b)/(3*a) + (-1)/(3*a) * rootPositive
answer = round(positiveAnswer + negativeAnswer,3)

print(answer)

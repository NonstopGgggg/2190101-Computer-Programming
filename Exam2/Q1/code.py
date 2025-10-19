import math

# input
num = [float(i) for i in input().split()]
N = int(input())

maxVal = -math.inf
length = len(num)
numList = []

# rotate and find the sum
for i in range(length):
    # rotate the list
    num = num[-1:] + num[:-1]
  
    # find the sum of first N terms
    target = num[:N]
    sumVal = sum(target)
    
    # update the max value and list with that value
    if sumVal >= maxVal:
        maxVal = sumVal
        numList = target
        
print(f"{maxVal:.2f}\n{numList}")

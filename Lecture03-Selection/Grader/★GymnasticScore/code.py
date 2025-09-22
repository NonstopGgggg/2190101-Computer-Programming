numbers = [float(i) for i in input().split()]

# initialize value
maxVal = numbers[0]
minVal = numbers[0]
sumVal = sum(numbers)

if maxVal < numbers[1]:
    maxVal = numbers[1]
    
if minVal > numbers[1]:
    minVal = numbers[1]
    
if maxVal < numbers[2]:
    maxVal = numbers[2]
    
if minVal > numbers[2]:
    minVal = numbers[2]
    
if maxVal < numbers[3]:
    maxVal = numbers[3]
    
if minVal > numbers[3]:
    minVal = numbers[3]

answer = (sumVal - maxVal - minVal) / 2

print(round(answer,2))

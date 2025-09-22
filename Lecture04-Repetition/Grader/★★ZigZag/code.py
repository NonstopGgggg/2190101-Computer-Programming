n = int(input())
list1 = []
list2 = []

for i in range(n):
    val1, val2 = input().split() 
    
    if i % 2 == 0:
        list1.append(int(val1))
        list2.append(int(val2))
        
    else:
        list2.append(int(val1))
        list1.append(int(val2))
        
decider = input()
minVal = 0
maxVal = 0

if decider == "Zig-Zag":
    minVal,maxVal = list1[-1], list2[-1]
    
    for i in list1:
        minVal = (minVal if minVal < i else i)
        
    for i in list2:
        maxVal = (maxVal if maxVal > i else i)
        
else:
    minVal,maxVal = list2[-1], list1[-1]
    
    for i in list2:
        minVal = (minVal if minVal < i else i)
        
    for i in list1:
        maxVal = (maxVal if maxVal > i else i)
        
print(minVal,maxVal)

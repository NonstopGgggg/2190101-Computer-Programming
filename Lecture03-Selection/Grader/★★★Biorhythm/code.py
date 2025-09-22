import math
bd,bm,by,d,m,y = [int(e) for e in input().split()]

length = 0

# Red part calculation
month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

# Calculate number of days in birth month
# if leap year add 1
if bm <= 2 and (by-543) % 4 == 0:
    length += (month_days[bm-1] - bd + 1) + 1
    
else:
    length += (month_days[bm-1] - bd + 1)

# add all the days after birth month
length += sum(month_days[bm:])

#print(length)

# Black part calculation
val = 0
val += 365 * (y - by - 1)

length += val
#print(val)

# Blue part calculation
val = 0

# Add days before current month
val += sum(month_days[:m-1])

# add current month
val += d - 1

# check for leap year
if m > 2 and (y - 543) % 4 == 0:
    val += 1

length += val
#print(val)
    
physicalCycle = math.sin((2 * math.pi * length) / (23))
physicalCycle = round(physicalCycle,2)
physicalCycle = "{:.2f}".format(physicalCycle)

emotionCycle = math.sin((2 * math.pi * length) / (28))
emotionCycle = round(emotionCycle,2)
emotionCycle = "{:.2f}".format(emotionCycle)

intellectCycle = math.sin((2 * math.pi * length) / (33))
intellectCycle = round(intellectCycle,2)
intellectCycle = "{:.2f}".format(intellectCycle)

print(length,physicalCycle,emotionCycle,intellectCycle)


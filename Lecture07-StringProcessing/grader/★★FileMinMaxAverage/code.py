# our input will be a file name and the starting year, we want to consider
# The first two characters of every line from the file will be the year of admission
# which is equivalence of the last two characters from the starting year.

name, year = input().split()
maxVal = 0
minVal = 101
avg = 0
count = 0

# extract scores from the valid lines (id[:2] >= year[-2:])
for i in open(name).readlines():
    if i[:2] >= year[-2:]:
        value = float(i[-5:-1])
        count += 1
        
        # Find the maximum, minimum and average
        avg += value
        maxVal = max(maxVal, value)
        minVal = min(minVal, value)

if count == 0:
    print("No data")

else:
    print(minVal,maxVal,round(avg/count,1))

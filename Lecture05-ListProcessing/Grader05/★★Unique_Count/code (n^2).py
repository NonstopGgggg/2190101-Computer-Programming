
# We are given a list of integers separated by space
# Our goal is to find the unique values from this list
# Then print it in ascending order.
# However, we will only print the first 10 numbers
# When we move to a new integer, we will check if it exists in the current unique list.
# Then we will insertion sort it into the unique list.

def insertion(num,numList):
    n = len(numList)
    
    # Loop to find the spot that num is less than the element
    i = 0
    while i < n and num > numList[i]:
        i += 1
            
    numList.insert(i,num)
    
number = [int(i) for i in input().split()]
uniqueList = []

for i in number:
    if i not in uniqueList:
        insertion(i,uniqueList)
        
print(len(uniqueList))
print(uniqueList[:10])

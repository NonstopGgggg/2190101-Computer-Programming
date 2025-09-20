# We are given a list of integers separated by space
# Our goal is to find the unique values from this list
# Then print it in ascending order.
# However, we will only print the first 10 numbers
# When we move to a new integer, we will check if it exists in the current unique list.
# Then we will insertion sort it into the unique list.

# This code is optimized for finding ascending list only
# If we sort from the start, then our input will be ascending.

number = [int(i) for i in input().split()]
number.sort()
uniqueList = []

# We are going to make a list that acts as a checklist for unique values, so we can avoid going through all the elements.
maxRange = max(number)
# 0 means not in the list, 1 means already existed
numCheck = [0] * (maxRange + 1) # +1 for 0-indexing
length = 0

for i in number:
    if numCheck[i] != 1:
        uniqueList.append(i)
        numCheck[i] = 1
        length += 1
        
print(length)
print(uniqueList[:10])


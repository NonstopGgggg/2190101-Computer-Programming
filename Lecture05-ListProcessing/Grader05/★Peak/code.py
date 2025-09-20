# We are given a list of real numbers, and we have to find the number of peaks
# Peak is defined as a value that is more than both the previous and the next values.
# Let's say we are given n numbers, the peak can only be between 1->(n-1)
# Thus, we will loop from 1 to n-1 and check if the i-th is a peak.

# Possible test case:
# [], [1], [1 3], [2 3 5], [2 4 3], [5 -5 4 3], [2 4 -8 7 -5 5 9 2]
def peakCount(number):
    n = len(number)
    peaks = 0
    
    for i in range(1,n-1):
        if number[i] > number[i-1] and number[i] > number[i+1]:
            peaks += 1
            
    return peaks
    
num = [int(i) for i in input().split()]
print(peakCount(num))

# We are given two strings of number in binary. These numbers are given in a single line separated by space.
# Our task is to add them up
# We must use to functions provided: bin and int
# bin(i) return binary of number i with prefix "0b".
# int(i, base) return number i in the given base. For this exercise, base 2 will be used.

# Receive the two numbers in binary 
num = [i for i in input().split()]

# Calculate the sum of the two numbers
sum = sum([int(i,2) for i in num])

# print the sum in binary format but emit the prefix "0b"
print(bin(sum)[2:])

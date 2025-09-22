num = input()
n = int(input())
length = len(num)

add_zero = max(0,n-length)

print("0" * add_zero + num)

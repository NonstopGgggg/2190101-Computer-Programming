n = int(input())
num = []

# First set (red)
for i in range(n):
    num.append(int(input()))
    
# Second set (blue)
num += [int(i) for i in input().split()]

# Third set (purple)
while True:
    val = int(input())
    
    if val == -1:
        break
    
    num.append(val)
    
# Display list by alternating front and back
frontList = [num[i] for i in range(len(num)-1,-1,-2)]
backList = [num[i] for i in range(len(num)-2,-1,-2)][::-1]

print(frontList + backList)


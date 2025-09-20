# We are given a positive integer and rules for collatz conjecture
# Collatz conjecture states that any positive integer modify by these rules will end at 1
# Thre rules:
# if number is even, n = n/2
# if number is odd, n = 3*n + 1
# We have to print the path this integer go through before reaching 1
# However, we are only allowed to print the last 15 integers or less

def collatz(num):
    path = [num]

    while num != 1:
        # The first rule
        if num % 2 == 0:
            num /= 2
            
        # The second rule
        else:
            num = num*3 + 1
            
        # add the current number to the path
        path.append(int(num))
    
    return path

num = int(input())
path = collatz(num)

# Print the last 15 integers of the path
for number in path[-15:]:
    print(number,end='')
    
    # only add -> if the current number is not 1
    if number != 1:
        print("->",end='')

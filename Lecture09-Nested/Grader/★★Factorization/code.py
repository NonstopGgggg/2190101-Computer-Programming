# performing naive factorization

# find the number of time the current number can be divided by k
def divTime(n,k):
    count = 0
    while n % k == 0:
        count += 1
        n /= k
        
    return count,n

def factor(num):
    divisor = 2
    factors = []

    # check for divisible factor
    while divisor <= num:
        value,num = divTime(num,divisor)
        if value:
            factors.append([divisor,value])
            
        divisor += 1
        
    return factors
        
# output
exec(input().strip())

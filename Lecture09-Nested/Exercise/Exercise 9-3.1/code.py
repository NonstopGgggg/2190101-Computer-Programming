# Count the number of time a digit d appears in number n
# digitInNumber(3324,3) = 2 because it has two 3s in it
def digitInNumber(n,d):
    sum = 0

    # use modular 10 to look at the last digit of number n
    # use // 10 to remove the rightmost digit we just checked
    while n > 0:
        if n%10 == d:
            sum += 1
        n //= 10
    
    return sum

# Given a list of numbers x, count the number of times digit d appears in the list.
def count_digit(x, d):
    c = 0
    for n in x:
        c += digitInNumber(n,d)
    return c

print(count_digit([333, 23, 4], 3))

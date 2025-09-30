# We are to implement 4 functions as commented

def make_int_list(x):
    # receive x as string input and convert them into int lit
    # Ex: x = '12 34 5' returns [12,34,5]
    return [int(i) for i in x.split()]

def is_odd(e):
    # return true if e is an odd number, otherwise return false
    return True if e % 2 == 1 else False

def odd_list(alist):
    # return a list which is like "alist" but contains only odd numbers
    # Ex: alist = [10, 11, 13, 24, 25] returns [11,13,25]
    return [i for i in alist if is_odd(i)]

def sum_square(alist):
    # return a sum of square of each number in alist
    # EX: alist = [1,3,4] returns (1*1 + 3*3 + 4*4), which is 26
    return sum([i*i for i in alist])

exec(input().strip())

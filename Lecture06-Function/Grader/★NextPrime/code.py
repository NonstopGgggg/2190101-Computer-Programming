# We are given a function is_prime(n) which checks if n is a prime number.
# Our task is to create two new functions by analyzing the given function.
# We have to create next_prime(n) which print the next prime number after n.
# The other function is next_twin_prime(n) which print the twin prime numbers more than n.

def is_prime(n):
    # check if n is a prime number
    if n <= 1:
        return False
    
    # When the loop reaches sqrt(n), all pairs have been identified.
    # The pairs after sqrt(n) are the previous pairs but swapped their places.
    for k in range(2, int(n**0.5) + 1):
        
        if n%k == 0:
            return False
        
    return True
    
def next_prime(n):
    k = n + 1
    
    # Return when a prime is found after the current number.
    while k > n:
        
        if is_prime(k):
            return k
        
        k += 1
    
def next_twin_prime(n):
    # Twin prime are separated by 2.
    # If we found a prime after n, we can return both numbers if that number plus 2 is also a prime.
    k = n + 1
    
    # Find the prime number after n
    while k > n:
        
        if is_prime(k):
            
            if is_prime(k+2):
                return (k,k+2)
            
        k += 1
        
# Our input will be in the form of "print(function(n))"
# function can be either next_prime or next_twin_prime
# n can be any integer
# exec is used to execute code from input
exec(input().strip())

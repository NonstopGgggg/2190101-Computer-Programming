# We are to write two functions: reverse() and key()
# Reverse(d) returns a dictionary where keys and values are swapped
# Key(d,v) returns a list of key containing value "v"

def reverse(d):
    # dictionary has no repeated value
    return {v:k for k, v in d.items()}
    
exec(input().strip())

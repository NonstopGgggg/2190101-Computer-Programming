n = int(input())

for i in range(1,n):
    print(" " * (n-i), end="")
    print("*",end="")
    
    if i > 1:
        print(" " * (2 * (i-1) - 1),end="")
        print("*",end="")
        
    print(" " * (n-i),end="\n")
    
print("*" * ((2 * n) - 1))

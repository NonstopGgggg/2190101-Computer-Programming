# given n sets, find the union and intersection of them.
# input
n = int(input())
ans = [set(),set()]

# find union and intersection
for i in range(n):
    val = set(input().split())
    
    if i != 0:
        ans[1] = ans[1].intersection(val)
        ans[0] = ans[0].union(val)
        
    else:
        ans = [val,val]

# output
print(len(ans[0]))
print(len(ans[1]))

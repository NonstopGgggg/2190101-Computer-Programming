# We are given "N" strings of nicknames and full names
# Our input will be "n" names
# Our task is to print out the names that matched with our input.
# However, if the name is not a match returns "Not found"

N = int(input())
names = {}

# dictionary of nicknames and full names
for i in range(N):
    key,value = input().strip().split()
    # we include both nickname and full name in the keys, so we can search both of them.
    names[key] = value
    names[value] = key
    
n = int(input())

for i in range(n):
    val = input().strip()
    print(names.get(val,"Not found"))
    

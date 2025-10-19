store = int(input())
users = {}

for i in range(store):
    n = int(input())
    
    # find users points
    for j in range(n):
        # input
        name,point = input().split()
        
        # update users' points
        users[name] = users.get(name,0) + int(point)
        
# sort the users by point then alphabetically
sortedUsers = sorted(users.items(),key = lambda d: (-d[1],d[0]))
for i in sortedUsers:
    print(i[0],i[1])

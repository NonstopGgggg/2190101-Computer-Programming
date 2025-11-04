# input
n = int(input())
cities = {}
people = []

for _ in range(n):
    ID,city = input().strip().split(":")
    city = [text.strip() for text in city.split(",")]
    people += [ID]
    
    for name in city:
        cities[name] = cities.get(name,[]) + [ID]
    
keyID = input()
found = set()

# output
for visitors in cities.values():
    #print(f"{keyID} {visitors}")

    if keyID in visitors:
        #print(keyID, visitors)
        found = found.union(set(visitors))
      
if len(found) <= 1:
    print("Not Found")
      
else:
    for ID in people:
        if ID in found and ID != keyID:
            print(ID)
        
#print(found)

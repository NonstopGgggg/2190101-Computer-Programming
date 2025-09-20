# We are given a coordinate set and we have to find the third closest coordinate from origin and print it
n = int(input())
coordinate = []

for i in range(n):
    val = [float(i) for i in input().split()]
    
    # Distance calculation
    xDist = (val[0])**2
    yDist = (val[1])**2
    dist = (xDist+yDist)**(1/2)
    
    val.insert(0,dist)
    val.insert(1,i+1)
    
    coordinate.append(val)
    
coordinate.sort()

print(f"#{coordinate[2][1]}: ({coordinate[2][2]}, {coordinate[2][3]})")

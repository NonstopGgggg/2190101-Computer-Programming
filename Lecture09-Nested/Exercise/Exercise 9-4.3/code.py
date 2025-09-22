# We are given a list of coordinates in 2D space.
# We are to find all pairs of points that have the minimum distance (There can be many pairs that have the same minimum distance).
# Our output will be in the form of index of these pairs.
# all_closest_pairs([[30,30], [30,31], [31,30], [30,32]]) = [[0, 1], [0, 2], [1, 3]]
# The minimum distance is 1.0
# [0,1] = the pair of points at index 0 and 1
# [0,2] = the pair of points at index 0 and 2
# [1,3] = the pair of points at index 1 and 3

from math import inf

def distance(p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def all_closest_pairs(points):
    # To find the minimum distance, we have to compare all pairs of points
    minDist = float(inf)

    # We will store the distance of each pair in a list
    # If we have four points, we will have this list [[d01,d02,d03],[d12,d13],[d23]]
    # Where dij is the distance between point i and point j
    # We will use this list to find the minimum distance

    distances = []
    n = len(points)
    # If we have a,b,c,d points
    # We will compare a with b,c,d
    # Then b with c,d
    # Then c with d
    for i in range(n):
        dist = []

        for j in range(i+1,n):
            dist.append(distance(points[i], points[j]))

            # Finding the minimum distance by comparing the distance of each pair
            if dist[-1] < minDist:
                minDist = dist[-1]

        distances.append(dist)

    results = []
    # If we have n points, the distance list will have n-1 lists
    for i in range(n-1):
        for j in range(len(distances[i])):
            if distances[i][j] == minDist:
                results.append([i,i+1+j])

    return results

print(all_closest_pairs([[30,30], [30,31], [31,30], [30,32]]))

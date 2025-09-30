import math

def distance1(x1, y1, x2, y2):
    # returns the distance between points (x1, y1) and (x2, y2)
    # Usage example: d1 = distance1(0.0, 0, 3, 4) -> d1 = 5.0
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def distance2(p1, p2):
    # p1 and p2 are lists
    # each list is a point, which has 2 indices, storing x and y
    # returns the distance between p1 and p2
    # Usage example: d2 = distance2([0.0, 0], [3, 4]) -> d2 = 5.0
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def distance3(c1, c2):
    # c1 and c2 are lists that represent circles
    # each list has 3 indices, storing center x and y, and radius
    # returns the distance between the center of c1 and c2,
    # as well as display if the circles are overlapping or not
    # Usage example: d3, overlap = distance3([0.0, 0, 1], [5, 0, 2])
    # -> d3 = 5.0, overlap = False
    distance = math.sqrt((c2[0]-c1[0])**2 + (c2[1]-c1[1])**2)
    # Two circles overlap when the sum of their radius is more than or equal to the distance of their center
    overlap = True if c1[2] + c2[2] >= distance else False
    return distance,overlap

def perimeter(points):
    # points is a list of points
    # each point is a list with 2 indices (storing x and y)
    # these points are the corners of the polygon (for k-gon, there are k points total, k>=3)
    # returns the perimeter of the polygon defined by the input points
    
    # sum of the distance of between all points equal to perimeter
    sum = 0.0
    for i in range(1, len(points)):
        sum += distance2(points[i-1], points[i])
        
    sum += distance2(points[0], points[-1])
    
    return sum

# Required for submission to grader
exec(input().strip())



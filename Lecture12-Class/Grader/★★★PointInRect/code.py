class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

class Rect:
    def __init__(self, p1, p2):
        self.lowerleft = p1
        self.upperright = p2

    def area(self):
        a = self.lowerleft.x
        b = self.lowerleft.y
        c = self.upperright.x
        d = self.upperright.y
        
        return (d - b) * (c - a)

    def contains(self, p):
        a = self.lowerleft.x
        b = self.lowerleft.y
        c = self.upperright.x
        d = self.upperright.y
        
        if p.x >= a and p.x <= c and p.y >= b and p.y <= d:
            return True
        
        return False

x1,y1,x2,y2 = [int(e) for e in input().split()]
lowerleft = Point(x1,y1)
upperright = Point(x2,y2)
rect = Rect(lowerleft, upperright)
print(rect.area())
m = int(input())
for i in range(m):
    x,y = [int(e) for e in input().split()]
    p = Point(x,y)
    print(rect.contains(p))


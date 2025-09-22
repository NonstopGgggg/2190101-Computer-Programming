a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a > b:
    temp = a
    a = b
    b = temp
    
if c > d:
    temp = c
    c = d
    d = temp
    
if a > c:
    temp = b
    b = d
    d = temp
    c = a

a = e

if a > b:
    temp = a
    a = b
    b = temp
    
if c > a:
    temp = b
    b = d
    d = temp
    a = c
    
if a > d:
    print(d)
    
else:
    print(a)

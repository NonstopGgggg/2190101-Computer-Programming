d,m,y = [int(e) for e in input().split()]
y -= 543

month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
n = month_days[m-1]

if m == 2:
    if y % 400 == 0:
        n = 29
        
    if y % 4 == 0 and not(y % 100 == 0):
        n = 29
        
d += 15
if d > n:
    d = d-n
    m += 1
    
if m > 12:
    m = m - 12
    y = y + 1
    
y += 543
print(str(d)+"/"+str(m)+"/"+str(y))

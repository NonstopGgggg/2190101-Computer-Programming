h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
t1 = h1*60*60 + m1*60 + s1
t2 = h2*60*60 + m2*60 + s2

if t1 > t2:
  # We move from 23 to 12 within 13 hours; however, the t1-t2 will return 11 hours without considering a new day
  # Therefore, we will have to find the reverse time segment 24-(t1-t2) = 13
  dt = (24*3600)-(t1-t2)
else:
  dt = t2-t1
  
dh = dt//3600
dt -= (dh*3600)

dm = dt//60
dt -= (dm*60) # leftover is in seconds

print(str(dh) + ":" + str(dm) + ":" + str(dt))

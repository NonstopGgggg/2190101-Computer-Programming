d = int(input())
m = int(input())
y = int(input())

month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

# day calc
length = 0 + d

# month calc
length += sum(month_days[:m-1])

# leap year calc
if ((y-543)%4 == 0 and (y-543) %100 != 0) or (y-543)%400 == 0:
    if m > 2:
        length += 1
    
print(length)

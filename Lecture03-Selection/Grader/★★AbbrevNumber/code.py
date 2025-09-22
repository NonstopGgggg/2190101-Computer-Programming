num = int(input())

if num / 1000000000 >= 1:
    val = num/1000000000
    if val >= 10:
        print(str(round(val))+"B")
    else:
        print(str(round(val,1))+"B")
    
elif num / 1000000 >= 1:
    val = num/1000000
    if val >= 10:
        print(str(round(val))+"M")
    else:
        print(str(round(val,1))+"M")
    
elif num / 1000 >= 1:
    val = num/1000
    if val >= 10:
        print(str(round(val))+"K")
    else:
        print(str(round(val,1))+"K")

else:
    print(num)

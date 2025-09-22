date = input().split("/")
day = date[0]
month = date[1]
year = date[2]

monthsName = ['January', 'February', 'March', 'April', 'May', 'June', 
'July', 'August', 'September', 'October', 'November', 'December']

print(monthsName[int(month)-1],day + ", " + year)

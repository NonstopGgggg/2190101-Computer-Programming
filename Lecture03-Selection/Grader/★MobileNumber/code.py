number = input()

startCode = ["06","08","09"]

if len(number) < 10 or len(number) > 10:
    print("Not a mobile number")
    
elif number[:2] in startCode:
    print("Mobile number")
    
else:
    print("Not a mobile number")

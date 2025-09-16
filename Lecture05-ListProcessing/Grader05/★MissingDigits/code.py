string = input()
# a list of integer to check if a digit exist
digit = [0,0,0,0,0,0,0,0,0,0]

for i in string:
    if i in "1234567890":
        digit[int(i)] = 1

# use join to format the string in form 3,4,5
answer = ",".join([str(i) for i in range(10) if digit[i] == 0])

# If all digits are found, return none
if not answer:
    print("None")
    
else:
    print(answer)

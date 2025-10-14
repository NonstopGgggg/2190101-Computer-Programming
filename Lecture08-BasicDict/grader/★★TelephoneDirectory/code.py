# we are given a string of full names and numbers
# our input will be some amount of string
# our task is to map the string to the number

# Mapping string to number and vice versa
telBook = {}
N = int(input())

for i in range(N):
    # format: name surname xxx-xxx-xxxx
    val = input().split()
    fullName = val[0] + " " + val[1]
    number = val[2]
    
    telBook[fullName] = number
    telBook[number] = fullName
    
# input and print
n = int(input())
for i in range(n):
    val = input()
    print(val,"-->",telBook.get(val,"Not found"))


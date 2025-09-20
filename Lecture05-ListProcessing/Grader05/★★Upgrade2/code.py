# We are given IDs and grades after that a letter q signaling the stop
# then we are given some unique IDs
# Our task is to increase the grade of that unique ID by one level if it can be increased.
# Moreover, we have to print the ID in ascending order which matches with the grade.

# Insertion sort
def insertion(num,numList):
    n = len(numList)
    
    # Loop to find the spot that num is less than the element
    i = 0
    while i < n and num > numList[i]:
        i += 1
            
    return i

grades = ["F","D","D+","C","C+","B","B+","A"]
ID = []
grade = []

# input loop for accepting ID and grade
while True:
    val = input().split()
    
    # break the loop when input stop
    if val[0] == "q":
        break
    
    position = insertion(val[0],ID)
    ID.insert(position,val[0])
    grade.insert(position,val[1])
    
n = len(ID)
UID = input().split()

# Loop for matching the UID with ID
for unique in UID:
    
    for identify in range(n):
        if unique == ID[identify] and grade[identify] != "A":
            
            # Loop for upgrading the grade
            for toUpgrade in range(8):
                if grade[identify] == grades[toUpgrade]:
                    grade[identify] = grades[toUpgrade+1]
                    break
                    
for i in range(n):
    print(ID[i], grade[i])

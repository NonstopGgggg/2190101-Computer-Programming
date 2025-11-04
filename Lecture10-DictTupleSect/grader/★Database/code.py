# input
fileName = []
lines = []

# files to search
for _ in range(3):
    fileName.append(input().strip())

# extract data from files
for i in range(3):
    with open(fileName[i]) as file:
        lines.append(file.readlines())
          
# the first two files contain courses and teachers
# course format: index, id
course = {}
for element in lines[0]:
    index, ID = element.strip().split(",")
    course[index] = ID.strip() # remove \n
    
# teacher format: index, name
teacher = {}
for element in lines[1]:
    index, name = element.strip().split(",")
    teacher[index] = name.strip() # remove \n

#print(course, teacher)

# output
for element in lines[2]:
    index1, index2 = [str(num) for num in element.strip().split(",")]
    index2 = index2.strip()

    #print(f"{index1},{index1 in course}")
    #print(f"{index2},{index2 in teacher}")
    
    if index1 in course and index2 in teacher:
        print(f"{course[index1]}, {teacher[index2]}")
        
    else:
        print("record error")

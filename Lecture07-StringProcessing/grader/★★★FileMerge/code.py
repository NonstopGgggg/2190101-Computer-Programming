# our input will be the name of two files
# the file contains student ID and their score
# the student ID is 10 digits long and the last two digits are the faculty ID
# our output will be the sorted list of faculty IDs
# If faculty ID is the same, sort by student ID

def read_next(f):
    while True:
        t = f.readline()
        if len(t) == 0: # end loop when all lines are read
            break
    
        x = t.strip().split() # remove blank

        if len(x) == 2: # split input to 2 parts
            return x[0], x[1]
        
        return "", "" # return none if input is not valid

# input file names
file1,file2 = input().split()

# read file1 using read_next()
with open(file1, "r") as f1, open(file2, "r") as f2:
    line1 = read_next(f1)
    line2 = read_next(f2)

    while True:

        # when file1 end, print remaining lines in file2
        if line1 == None:
            while line2 != None:
                print(line2[0], line2[1])
                line2 = read_next(f2)

            break

        # when file2 end, print remaining lines in file1
        elif line2 == None:
            while line1 != None:
                print(line1[0], line1[1])
                line1 = read_next(f1)

            break

        elif line1[0][-2:] < line2[0][-2:]:
            print(line1[0], line1[1])
            line1 = read_next(f1)

        elif line1[0][-2:] > line2[0][-2:]:
            print(line2[0], line2[1])
            line2 = read_next(f2)

        else: # when faculty ID is the same, sort by student ID
            if line1[0] < line2[0]:
                print(line1[0], line1[1])
                line1 = read_next(f1)
            else:
                print(line2[0], line2[1])
                line2 = read_next(f2)

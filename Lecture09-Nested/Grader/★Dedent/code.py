# given a string with many lines, we have to reduce the number of leading space by half
# leading space will always be even

# half the leading space
def halfLeadingSpace(line):
    # count keeps track of total number of spaces
    count = 0
    for i in line:
        
        if i != ".":
            break
            
        count += 1
        
    # return half of leading space
    if count:
        return line[int(count/2):]
    
    else:
        return line

# lines for storing each line, n for number of lines
lines = []
n = int(input())

# input (one line at a time)
for i in range(n):
    line = input()
    line = halfLeadingSpace(line)
    lines.append(line)

# output
for i in lines:
    print(i)


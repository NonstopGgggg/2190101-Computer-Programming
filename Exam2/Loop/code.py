# find studentID in a string and returns a list with all found ids
def findID(string,target):
    n = len(string)
    ids = []

    # student id must be 10 characters
    if n < 10:
        return -1
    
    # find the student id that starts with specified number
    else:
        for i in range(n-9):
            if i <= n - 10 and string[i:i+10].isdigit():
                found = string[i:i+10]
                
                if found[:2] == target and found[-2:] == "21":
                    ids.append(found)
                    
    return ids

# input
string = input().strip().split()
target = input().strip()
ans = []

for word in string:
    found = findID(word,target)
    if found != -1:
        ans += found
        
#output
if not ans:
    print("Not found")
    
else:
    print("\n".join(ans))

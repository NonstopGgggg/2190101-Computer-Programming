# we are given a string
# our task is to print the amount each alphabet appears in that string in descending order
# upper and lower case are treated as the same (A == a)

# receive a dictionary and returns descending value of that list
def descendList(d):
    x = list(d.items())
    
    # sort the list descendingly for number and ascendingly for letter
    return sorted(x, key=lambda x: (-x[1],x[0]))

# count the number of characters in a string
def charCount(string):
    s = string.lower()
    chars = {}
    
    for i in s:
        chars[i] = chars.get(i,0) + 1

    return chars

string = input()
char = descendList(charCount(string))
for key,value in char:
    print(key,"->",value)

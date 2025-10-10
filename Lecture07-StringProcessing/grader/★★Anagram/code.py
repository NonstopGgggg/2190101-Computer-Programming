# We are to check if two strings are anagram or not.
# Anagram means the first string can be arranged to look exactly like the second string and vice versa.
# Moreover, anagram does not care about upper cases or lower cases.
# This means a string that contains the same characters with the same amount are anagram.

# remove spaces because we only count the characters
def clean(string):
    newString = ""
    
    for i in range(len(string)):
        if string[i] == " ":
            newString += ""
            
        else:
            newString += string[i]
            
    return newString
            
def anagram(string1,string2):
    # If both strings are anagram, their sorted version should look alike.
    char1 = sorted(clean(string1.lower()))
    char2 = sorted(clean(string2.lower()))
    
    if char1 == char2:
        return "YES"
    
    return "NO"

# input
string1 = input()
string2 = input()

print(anagram(string1,string2))

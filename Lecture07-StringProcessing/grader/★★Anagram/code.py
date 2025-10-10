# We are to check if two strings are anagram or not.
# Anagram means the first string can be arranged to look exactly like the second string and vice versa.
# Moreover, anagram does not care about upper cases or lower cases.
# This means a string that contains the same characters with the same amount are anagram.

def anagram(string1,string2):
    # If both strings are anagram, their sorted version should look alike.
    char1 = sorted(string1.lower())
    char2 = sorted(string2.lower())
    
    if char1 == char2:
        return "YES"
    
    return "NO"

# input
string1 = input()
string2 = input()

print(anagram(string1,string2))

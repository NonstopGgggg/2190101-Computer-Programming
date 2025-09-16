# Given a list of words, we are to find the longest suffix of that list.
# Suffix is the ending part of a word.
# This means if the last character of all words is the same, then the longest suffix is that character.
# Moreover, the longest suffix we can have is no longer than the shortest word in the list.

def longest_suffix(words):
    suffix = ''

    # find the longest possible suffix length
    n = min(len(word) for word in words)

    # loop from the last index until the index -n
    for i in range(-1,-n-1,-1):

        # check if all words have the same character at index i
        for j in range(1,len(words)):

            # if any words has a different character, return the suffix found so far
            if words[j][i] != words[0][i]:
                return suffix
            
        # include the character at index i if all characters are the same
        suffix = words[0][i] + suffix

    return suffix

print(longest_suffix(["programming", "scramming", "Diagramming"]))

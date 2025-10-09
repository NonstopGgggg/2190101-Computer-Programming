# To turn a sentence into Camel Case, the first word is uncapitalized and the rest has their first character capitalized.

# input
sentence = input().strip()
newString = ""

# clean non alphabet from input
for i in sentence:
    if i.isalpha() or i.isdigit():
        newString += i
        
    else:
        newString += " "
        
word = newString.split()

# uncapitalized the 1st word then capitalize the 2nd word and so on.
word[0] = word[0].lower()

for i in range(1, len(word)):
    word[i] = word[i].lower().capitalize()
    
print("".join(word))

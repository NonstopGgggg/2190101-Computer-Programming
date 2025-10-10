# Implement rot13 code
def rot13(char):
  upChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  lowChar = upChar.lower()
  
  if char.islower():
    return lowChar[(lowChar.find(char) + 13) % 26]
    
  elif char.isupper():
    return upChar[(upChar.find(char) + 13) % 26]
    
  return char

# We have to use rot13 encryption on the input
lines = []

# input
while True:
    val = input()
    
    if val == "end":
        break
    
    lines.append(val)
            
# use rot13
newLines = []

for i in range(len(lines)):
    length = len(lines[i])
    newString = ""
    
    for j in range(length):
        newString += rot13(lines[i][j])
        
    newLines.append(newString)
    
for i in newLines:
    print("".join(i))

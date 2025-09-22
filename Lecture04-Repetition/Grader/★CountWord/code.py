word = input()
string = input()

s = ""
for i in string:
    if i in "\"\'\\(),.":
        s += " "
        
    else:
        s += i

string = s.split()
  
count = 0
for i in string:
    if word == i:
        count += 1
        
print(count)

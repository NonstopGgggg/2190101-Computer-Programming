string = input()

target = ["(",")","[","]"]
replace = ["[","]","(",")"]

answer = ""
for i in range(len(string)):
    
    if string[i] in "()[]":
        
        for j in range(4):
            if string[i] == target[j]:
                answer += replace[j]
                
    else:
        answer += string[i]
        
print(answer)


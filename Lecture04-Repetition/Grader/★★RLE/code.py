string = input()
answer = []
count = 1

for i in range(1,len(string)):
    if string[i] == string[i-1]:
        count += 1
        
    else:
        answer.append(string[i-1])
        answer.append(count)
        count = 1
        
answer.append(string[-1])
answer.append(count)
        
[print(i, end=" ") for i in answer]

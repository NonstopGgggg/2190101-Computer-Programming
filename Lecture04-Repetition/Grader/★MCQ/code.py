ans = input()
student = input()

if len(ans) != len(student):
    print("Incomplete answer")
    
else:
    correct = 0
    
    for i in range(len(ans)):
        if ans[i] == student[i]:
            correct += 1
            
    print(correct)

exec(input().strip()[4:])
print("spj")
n = int(input())
answer = []

for i in range(n):

  val = int(input())
  if i == 0:
    answer.append(val)
      
  else:
    insertion = True
      
    for j in range(len(answer)):
          
      if val > answer[j]:
          answer.insert(j,val)
          insertion = False
          break
              
    if insertion:
        answer.append(val)
              
print(answer[0],answer[1])

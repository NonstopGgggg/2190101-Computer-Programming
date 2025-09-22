vector1 = input().split(",")
vector2 = input().split(",")

# clean the vector
vector1[0] = vector1[0][1:]
vector1[2] = vector1[2][0:-1]
vector2[0] = vector2[0][1:]
vector2[2] = vector2[2][0:-1]

vector3 = []

for i in range(len(vector1)):
  vector1[i] = float(vector1[i])
  vector2[i] = float(vector2[i])
  vector3.append(vector1[i] + vector2[i])

print(vector1, "+", vector2, "=", vector3)  

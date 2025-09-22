# We are given two vectors of the same size
# We are to implement the addition of these two vectors and the dot product of these two vectors
# We must use list comprehension to implement both functions
def add(u,v):
    return [u[i] + v[i] for i in range(len(u))]

def dot(u,v):
    return sum([u[i] * v[i] for i in range(len(u))])

print(add([1,2,3],[4,5,6]))
print(dot([1,2,3],[4,5,6]))

# To transpose a matrix M, we swap the rows and columns
# If M is a p*q matrix, the transposed matrix will be a q*p matrix
def transpose(M):
    transposed = []

    for i in range(len(M[0])):
        row = []

        for j in range(len(M)):
            row.append(M[j][i])

        transposed.append(row)

    return transposed

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))

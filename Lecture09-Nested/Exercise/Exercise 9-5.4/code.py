# print n*n identity matrix
def identity(n):
    matrix = []
    for i in range(n):

        row = []
        for j in range(n):
            # when i==j the element is at the diagonal, so we put 1
            if i == j:
                row.append(1)
            else:
                row.append(0)

        matrix.append(row)

    return matrix

print(identity(4))

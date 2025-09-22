# Sum of each column in matrix M
# Matrix M is garanted to be non-empty and all rows have the same number of columns

def sum_col(M):
    sums = []
    for i in range(len(M[0])):
        total = 0

        for j in range(len(M)):
            total += M[j][i]

        sums.append(total)

    return sums

print(sum_col([[1,2,3],[4,5,6],[7,8,9]]))

# Given a matrix M, return the sum of all elements in M
def sum_all(M):

    total = 0
    for row in M:

        for element in row:
            total += element

    return total

print(sum_all([[1,2,3],[4,5,6],[7,8,9]]))

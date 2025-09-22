# Sum of each row in matrix M
def sum_row(M):
    sums = []
    for row in M:
        total = 0

        for element in row:
            total += element

        sums.append(total)

    return sums

print(sum_row([[1,2,3],[4,5,6],[7,8,9]]))

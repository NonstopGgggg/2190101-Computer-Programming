N = int(input())

# Multiplication start at base 2 to N
for i in range(2,N+1):

    # Diplay mutiple of number i from 1 to 5
    for j in range(1,6):
        # print with consistent left padding (4 in this case)
        print(" " * (4 - len(str(i * j))), end='')
        print(i * j, end='')

        j += 1

    print("")
    i += 1

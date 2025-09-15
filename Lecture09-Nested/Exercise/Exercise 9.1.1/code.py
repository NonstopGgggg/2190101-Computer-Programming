N = int(input())

# Multiplication start at base 2 to N
i = 2
while i <= N:

    # Diplay mutiple of number i from 1 to 5
    j = 1
    while j <= 5:
        # print with consistent left padding (4 in this case)
        print(" " * (4 - len(str(i * j))), end='')
        print(i * j, end='')

        j += 1

    print("")
    i += 1

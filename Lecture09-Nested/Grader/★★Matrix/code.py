def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        
        for e in x:
            r.append(float(e))
            
        m.append(r)
    return m

# multiply matrix A by real number c
def mult_c(c,A):
    newA = []
    for row in A:
        
        line = []
        for col in row:
            line.append(col*c)
            
        newA.append(line)
            
    return newA

# find C[i][j] from matrix A and B
def rowColMul(A,B,n,row,col):
    sumVal = 0
    for i in range(n):
        sumVal += A[row][i] * B[i][col]
        
    return sumVal
    
# multiply matrix A and B
def mult(A, B):
    rowA = len(A)
    rowB = len(B)
    colA = len(A[0])
    colB = len(B[0])
    
    C = []
    for i in range(rowA):
        
        line = []
        for j in range(colB):
            line.append(rowColMul(A,B,colA,i,j))
            
        C.append(line)
        
    return C
exec(input().strip())


def row_number(t, e): # returns row number of t containing e (top row is row #0)
    index = 0
    n = len(t)
    for i in range(n):
        if e in t[i]:
            index = i
            
    return index
    
def flatten(t): # returns a list of ints converted from list of lists of this t
    return [element for block in t for element in block if element != 0]
    
def inversions(x): # returns the number of inversions of list x
    inverse = 0
    n = len(x)
    
    for i in range(n):
        
        for j in range(i+1,n):
            if x[i] > x[j]:
                inverse += 1
                
    return inverse

def solvable(t): # returns True if tiling t (list of lists of ints) is solvable otherwise returns False
    rows = len(t)
    # odd check
    if rows % 2 == 1:
        inverse = inversions(flatten(t))
        if inverse % 2 == 0:
            return True
        
        return False
        
    # even check
    else:
        inverse = inversions(flatten(t))
        index0 = row_number(t,0)
        if inverse % 2 == 1:
            return True if index0 % 2 == 0 else False
        
        else:
            return True if index0 % 2 == 1 else False

exec(input().strip()) # do not remove this line


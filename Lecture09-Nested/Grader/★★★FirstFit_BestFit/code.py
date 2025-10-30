def first_fit(L, e):
    # put e into sub-list inside L by using First Fit.
    n = len(L)
    include = False

    # find the block with enough space to fit e
    for i in range(n):
        if sum(L[i]) + e <= 100:
            L[i] += [e]
            include = True
            break
        
    # check if element can be fit into existing list
    # if not, append new element
    if not include:
        L.append([e])
            
    return L

def best_fit(L, e):
# put e into sub-list inside L by using Best Fit.
    n = len(L)
    maxUnder100 = 0
    pos = 0

    # find the block with enough space to fit e
    for i in range(n):
        val = sum(L[i]) + e
        if val <= 100 and val > maxUnder100:
            maxUnder100 = val
            pos = i
            
    # check if there is a space for insertion
    # if not, append new element
    if maxUnder100:
        L[pos] += [e]
    
    else:
        L.append([e])
        
    return L

def partition_FF(D):
    # return a list of partitioned data from D using First Fit.
    newD = []
    for element in D:
        newD = first_fit(newD,element)
        
    return newD

def partition_BF(D):
    # return a list of partitioned data from D using Best Fit.
    newD = []
    for element in D:
        newD = best_fit(newD,element)
        
    return newD
    
exec(input().strip()) # must have this line to submit into grader


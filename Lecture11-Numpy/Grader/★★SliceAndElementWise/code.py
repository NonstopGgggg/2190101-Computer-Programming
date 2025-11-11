import numpy as np
def sum_2_rows( M ):
 # Return summation in each column of 2 adjacent rows.
 # Ex M = [[ 0, 1, 2, 3 ], is [[ 4, 6, 8, 10 ],
 # [ 4, 5, 6, 7 ], [ 20, 22, 24, 26 ]]
 # [ 8, 9, 10, 11 ],
 # [12, 13, 14, 15]]
    return M[0::2] + M[1::2]

def sum_left_right( M ):
 # Return summation of left half and right half of M
 # Ex M = [[ 0, 1, 2, 3 ], is [[ 2, 4],
 # [ 4, 5, 6, 7 ], [ 10, 12],
 # [ 8, 9, 10, 11 ], [ 18, 20],
 # [12, 13, 14, 15]] [ 26, 28]]
    mid = M.shape[1] // 2
    return M[:,:mid] + M[:,mid:]

def sum_upper_lower( M ):
 # Return summation of upper half and lower half of M
 # Ex M = [[ 0, 1, 2, 3], is [[ 8, 10, 12, 14],
 # [ 4, 5, 6, 7], [16, 18, 20, 22]]
 # [ 8, 9, 10, 11],
 # [12, 13, 14, 15]]
    mid = M.shape[0] // 2
    return M[:mid] + M[mid:]
    
def sum_4_quadrants( M ):
 # Return summation in the same position from 4 quadrants
 # Ex M = [[ 0, 1, 2, 3], is [[20, 24],
 # [ 4, 5, 6, 7], [36, 40]]
 # [ 8, 9, 10, 11],
 # [12, 13, 14, 15]]
    return sum_upper_lower(sum_left_right(M))
 
def sum_4_cells( M ):
 # Return summation of 4 adjacent numbers according to the pattern below.
 # Ex M = [[ 0, 1, 2, 3], is [[10, 18],
 # [ 4, 5, 6, 7], [42, 50]]
 # [ 8, 9, 10, 11],
 # [12, 13, 14, 15]]
    return M[::2][:,::2] + M[::2][:,1::2] + M[1::2][:,::2] + M[1::2][:,1::2]
 
def count_leap_years( years ):
 # Years is array which contains Buddhist years
 # Return the number of leap years (years which have 366 days) in years
    years -= 543
    return np.sum((years % 400 == 0) | ((years % 100 != 0) & (years % 4 == 0)))

exec(input().strip()) # This command is necessary to grade your answer

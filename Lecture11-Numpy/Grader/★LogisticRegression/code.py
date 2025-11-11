import numpy as np
def p(x):
# x is an array with size n x 2, containing the number of
# problems solved (column 0), and GPA (column 1) of n students.
    
# Return an array with size n, containing the probability that each
# student will pass the course, calculated with the formula above.

# Using NumPy will allow you to write this function without
# using loops. (The answer is no more than 3 lines).
    logit = -3.98 + 0.1*x[::,0] + 0.5*x[::,1]
    return 1 / (1 + np.exp(-logit))

exec(input().strip()) # This line is required for Grader to work.

import numpy as np
def read_data():
 # Read data from input, then create and return 2 arrays
 # weight is array with the size of 3, contain weight of midterm, final, and project score (float)
 # data is array with nx4 shape, contain data of each n number of student, each consist of
 # student ID, midterm score, final score, and project score (int)
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight, data):
 # Show Student IDs of students with average score lower than mean
 # Show all IDs on the single line with ", " in between (a comma and one space)
 # Arrange in order appear in data, If no student has average score lower than mean, show “None”
    for i in range(data.shape[0]):
        data[i,1] = data[i,1] * weight[0]
        data[i,2] = data[i,2] * weight[1]
        data[i,3] = data[i,3] * weight[2]
        
    score = data[:,1:].sum(axis = 1)
    meanScore = np.mean(score)
    
    lower = data[score < meanScore,0]
    
    if len(lower) <= 0:
        print(None)
        
    else:
        for i in range(lower.shape[0]):
            print(lower[i], end="")
            if i < lower.shape[0]-1:
                print(", ",end="")
 
exec(input().strip()) # You must have this line when submit to grader


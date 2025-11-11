import numpy as np
def toCelsius(f):
 # f is a 1-d array storing temperatures in Fahrenheit
 # returns 1-d array storing the converted temp. from f in Celsius
    return (f -32) * (5/9)
     
def BMI(wh):
 # wh is a 2-d array of size n×2 storing weight (in kg) and height (in cm)
 # of the nth person. 0th column stores weight, 1st column stores height
 # returns 1-d array storing body mass index of everyone in wh
    return wh[:,0] / (wh[:,1]*.01)**2

def distanceTo(p, Points):
 # p is a 1-d array with size=2 representing an x, y coordinate
 # 0th index stored the coordinate of x, 1st index stored the coordinate of y
 # Points is a 2-d array of size n×2. Storing coordinates of all n points
 # returns 1-d array with the size of n. The array stores distance from p
 # to each point in Points.
    points = Points.T
    result = ((points[0]-p[0])**2 + (points[1]-p[1])**2)**0.5
    return result

exec(input().strip()) # must have this line when submitting to grader

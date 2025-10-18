# given a,b,c1,c2,c3
# a = lower boundary (start)
# b = upper boundary (stop)
# c1,c2,c3 are coefficients of f(x)
# where f(x) = c1x^2 + c2x + c3
# find the area under the curve when fixed at 10 bars

coeff = []

# input
for i in range(5):
    coeff.append(float(input()))
    
# find area with left side approximation
width = (coeff[1] - coeff[0])/10.0
area = 0

for i in range(10):
    x = coeff[0] + (width * i)
    curve = coeff[2] * (x**2) + coeff[3] * x + coeff[4]
    
    area += width * curve
    
print(area)

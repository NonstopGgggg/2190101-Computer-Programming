# All functions must use list comprehension
def to_list_of_strings(x):
    return [str(i) for i in x]

def get_positive(x):
    return [i for i in x if i>0]

def get_peak_indexes(x):
    return [i for i in range(1,len(x)-1) if x[i] > x[i-1] and x[i] > x[i+1]]

print(to_list_of_strings([1,2,3,-4,5]))
print(get_positive([1,2,3,-4,5]))
print(get_peak_indexes([1,3,2,4,3,5,4]))

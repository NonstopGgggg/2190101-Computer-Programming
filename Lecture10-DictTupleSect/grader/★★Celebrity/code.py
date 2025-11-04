def knows(R,x,y):
# return True if x knows y
    return y in R[x]
    
def is_celeb(R,x):
# return True if a is_celeb, otherwise retuen False
# return False if x knows someone who is not him/herself
# return False if there exists someone in R who don’t know x
# otherwise return True
    #print(x, R)
    if len(R[x]) >= 2:
        return False

    else:
        for person in R:
            if x != person and x not in R[person]:
                return False
            
        return True

def find_celeb(R):
# for each person x in the party
# if x is celeb - -> return x
# if no celeb in the party - - > return None
    #print(R)
    for person in R:
        #print(person)
        if is_celeb(R,person):
            return person
        
    return None

def read_relations():
# build a dictionary R from inputs
# whose structure is shown in the example
    R = dict()
    while True:
        d = input().split()
        if len(d) == 1:
            break
        
        R[d[0]] = R.get(d[0], set()).union(d[1])
        R[d[1]] = R.get(d[1], set()).union(d[1])

    return R

def main():
    R = read_relations()
    c= find_celeb(R)
    
    if c == None:
        print('Not Found')
    else:
        print(c )
        
exec(input().strip()) # do not remove this line


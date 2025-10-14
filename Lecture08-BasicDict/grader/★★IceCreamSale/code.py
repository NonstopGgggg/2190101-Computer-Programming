# get input and create an ice_cream_price dict {icecream_type:price}
n = int(input())
ice = {}

# return a list of the most popular ice cream type
def popular(icePopular):
    maxVal = 0
    ices = []
    
    for key in icePopular:
        if icePopular[key] > maxVal:
            maxVal = icePopular[key]
            ices = [key]
            
        elif icePopular[key] == maxVal:
            ices += [key]
            
    return sorted(ices)

# fixed ice cream price and type
for _ in range(n):
    iceType, icePrice = input().split()
    ice[iceType] = icePrice

# ice cream sold section
sold = int(input())

iceSum = 0
icePopular = {}
for _ in range(sold):
    iceType, iceSold = input().split()
    revenue = 0

    if iceType in ice:
        revenue = float(ice[iceType]) * int(iceSold)
        icePopular[iceType] = icePopular.get(iceType,0) + revenue
        
    iceSum += revenue
        
ices = popular(icePopular)
        
if iceSum == 0:
    print("No ice cream sales")
    
else:
    print("Total ice cream sales:",round(iceSum,1))
    print("Top sales: ", end="")
    for i in range(len(ices)):
        print(ices[i], end="")
        if i < len(ices) - 1:
            print(", ",end="")

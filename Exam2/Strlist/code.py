# pad thai!

menu,order = map(int,input().split())

# input for menu
item = {}
for i in range(menu):
    val = input().strip().split()
    name = " ".join(val[:-1])
    price = float(val[-1])
    
    item[name] = price
    
# input for orders
buy = {}
for i in range(order):
    val = input().strip().split()
    name = " ".join(val[:-1])
    amount = float(val[-1])
    
    buy[name] = amount
    
total = 0
for i in buy:
    if i in item:
        total += buy[i] * item[i]
        
if total == 0:
    print("Not found")
    
else:
    print(f"{total:.2f}")
    


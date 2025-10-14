# return total amount of cash in pocket
def total(pocket):
    # pocket format: {coin_value : amount, coin_value2 : amuount, ...}
    coinSum = 0
    
    for i in pocket:
        coinSum += i * pocket[i]
        
    return coinSum

# add cash to the pocket dictionary
def take(pocket, money_in):
    # pocket & money_in format: {coin_value : amount, coin_value2 : amuount, ...}
    for i in money_in:
        pocket[i] = pocket.get(i,0) + money_in[i]
            
    return pocket

# remove cash from the pocket dictionary
# return amount of money paid
# follow by remaining amount in pocket
def pay(pocket, amt):
    # pocket format: {coin_value : amount, coin_value2 : amuount, ...}
    paid = {}
    pocket2 = pocket.copy()
    
    for i in pocket2:
        while amt > 0 and pocket2[i] > 0 and i <= amt:
            amt -= i
            
            # record the spent coin in another dictionary
            paid[i] = paid.get(i,0) + 1
            pocket2[i] -= 1
    # if the amount cannot be paid with out pocket
    if amt:
        return {}
    
    # if it can be paid
    else:
        pocket.update(pocket2)
        return paid

exec(input().strip())


# This program will simulate a restaurant waiter
# The input will be a number "n" follow by "n" commands
# Our input will always be correctly typed and only these commands mention will appear
# These are the commands and what they perform:

# reset n | means to start the queue at number "n"
# No output

# new t | means there is a new person in the queue at time "t"
# output: ticket n | n is the latest customer

# order t1 | means to order something at time "t1"
# output: qtime n1 t2 |
# n1 is the current customer who is ordering
# t2 = the time he orders [t1] - time he enters [t]

# avg qtime | find the average of waiting time t2
# output: avg_qtime n2 | n2 = total t2 / number of t2

# We have to keep track:
# The current customer
# The customers in the queue
# The time customers enter
# Order time is not needed because we only use it to calculate wait time
# The time customers wait
# The number at which queue starts

n = int(input())
current = -1 # -1 when no customer is in the shop
start = 1
customer = []
enterTime = []
waitTime = []
ticket = []

for i in range(n):
    ticket.append(input())

for i in range(n):
    
    # Command are arranged in length to avoid index out of bound
    
    if ticket[i][:3] == "new":
        
        if not customer:
            last = start
            
        else:
            last = customer[-1] + 1
            
        print(f"ticket {last}")
        customer.append(last)
        enterTime.append(int(ticket[i][3:]))
        
    elif ticket[i][:4] == "next":
        current += 1
        print(f"Call {customer[current]}")
    
    elif ticket[i][:5] == "order":
        waitTime.append(int(ticket[i][6:]) - enterTime[current])
        print(f"qtime {customer[current]} {waitTime[-1]}")
        
    elif ticket[i][:5] == "reset":
        start = int(ticket[i][6:])
        
    elif ticket[i][:9] == "avg_qtime":
        print(f"avg_qtime {round(sum(waitTime)/len(waitTime),4)}")
        
    #print(current,customer,enterTime,waitTime)

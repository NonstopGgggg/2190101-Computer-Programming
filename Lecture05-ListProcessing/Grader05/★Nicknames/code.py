real_names = ["Robert", "William", "James", "John", "Margaret", "Edward", "Sarah", "Andrew", "Anthony", "Deborah"]
nicknames = ["Dick", "Bill", "Jim", "Jack", "Peggy", "Ed", "Sally", "Andy", "Tony", "Debbie"]

n = int(input())
names = []

# Name input
for i in range(n):
    names.append(input())

for name in names:
    # Check if name exist in real_names
    if name in real_names:
        print(nicknames[real_names.index(name)])
        
    # check if name exist in nicknames
    elif name in nicknames:
        print(real_names[nicknames.index(name)])
    
    # For unknown names
    else:
        print("Not found")

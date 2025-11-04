# given n lines of two football team
# the first team wins and the second team loses
# find the team that never lose.

# input
n = int(input())
winner = set([])
loser = set([])

# find winner with no losses
for i in range(n):
    win,lose = input().strip().split()
    
    # winner in loser does not count
    if win in loser:
        pass
    
    # winner without losses counts
    elif win not in winner:
        winner.add(win)
        
    # loser in winner must be removed
    if lose in winner:
        winner.remove(lose)
        loser.add(lose)
        
    # loser not in loser is added
    elif lose not in loser:
        loser.add(lose)
        
# output
print(sorted(winner))

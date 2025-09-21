# We are given even number of cards, our task is to follow the instructions, which will be the last line of input.
# There are two instructions:
# C = Cut | cut means to separate the cards into two equal pile and swap the two pile.
# Ex: ABCD --CUT--> CDAB
# S = Shuffle | shuffle means to separate the cards into two equal piles and put the card alternatively from left and right pile.
# Ex: AB CD --SHUFFLE--> ACBD
# We have to make two functions that accept even number of cards and perform each of the instruction

def cutCards(cards):
    # n is the midpoint between two pile
    n = len(cards) // 2
    
    # Swap the left and right piles
    return cards[n:] + cards[:n]
    
def shuffleCards(cards):
    # n is the midpoint between two pile
    n = len(cards) // 2
    
    front = cards[:n]
    back = cards[n:]
    current = 0
    
    # Alternate between the left and right piles
    return [front[i//2] if i%2 == 0 else back[i//2] for i in range(n*2)]
   
# Accept input
card = input().split()
instruction = input()

# Loop the instruction and perform accordingly.
for i in instruction:
    
    # C is to cut the cards
    if i == "C":
        card = cutCards(card)
        
    # S is to shuffle the cards
    elif i == "S":
        card = shuffleCards(card)
        
    else:
        pass
        
# Print the output
for i in card:
    print(i,end=" ")

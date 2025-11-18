class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"({self.value} {self.suit})"
    
    def getScore(self):
        if self.value == "A":
            return 1
        
        elif self.value in "JQK":
            return 10
        
        else:
            return int(self.value)
    
    def sum(self, other):
        return (self.getScore() + other.getScore())%10
    
    def __lt__(self, rhs):
        score = {"3":1,"4":2,"5":3,"6":4,"7":5,"8":6,"9":7,"10":8,"J":9,"Q":10,"K":11,"A":12,"2":13}
        suitScore = {"club":1,"diamond":2,"heart":3,"spade":4}
        
        if self.value != rhs.value:
            return False if score[self.value] > score[rhs.value] else True
        
        else:
            return False if suitScore[self.suit] > suitScore[rhs.suit] else True

n = int(input())
cards = []

for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
    
for i in range(n):
    print(cards[i].getScore())
print("----------")

for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
    
cards.sort()

for i in range(n):
    print(cards[i]) 


class Card:
    
    suits = {"club":0,"diamond":1,"heart":2,"spade":3}
    suitsName = ["club","diamond","heart","spade"]
        
    score = {'3': 0, '4': 1, '5': 2, '6': 3, '7': 4, '8': 5, '9': 6, '10': 7, 'J': 8, 'Q': 9, 'K': 10, 'A': 11, '2': 12}
    scoreName = ["3","4","5","6","7","8","9","10","J","Q","K","A","2"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"({self.value} {self.suit})"

    def next1(self):
        newSuit = Card.suitsName[(Card.suits[self.suit] + 1) % 4]
        newScore = self.value
        
        # changing from spade to club increase the value of card
        if newSuit == "club":
            newScore = Card.scoreName[(Card.score[self.value]+1)%13]
            
        return Card(newScore,newSuit)

    def next2(self):
        self.suit = Card.suitsName[(Card.suits[self.suit] + 1) % 4]
        self.value = self.value
        
        # changing from spade to club increase the value of card
        if self.suit == "club":
            self.value = Card.scoreName[(Card.score[self.value]+1)%13]

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])


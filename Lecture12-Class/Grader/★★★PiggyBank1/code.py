class piggybank:

    def __init__(self):
        # has 4 variables storing the
        # amount for each type of coins
        self.coin1 = 0
        self.coin2 = 0
        self.coin5 = 0
        self.coin10 = 0

    def add1(self, n):
        # adds n into the variable that
        # stores 1-Baht coins
        self.coin1 += n

    def add2(self, n):
        # adds n into the variable that
        # stores 2-Baht coins
        self.coin2 += n

    def add5(self, n):
        # adds n into the variable that
        # stores 5-Baht coins
        self.coin5 += n

    def add10(self, n):
        # adds n into the variable that
        # stores 10 Baht coins
        self.coin10 += n

    def __int__(self):
        # returns the total value (the
        # amount of coins multiplied by
        # coins value)
        return 1 * self.coin1 + 2 * self.coin2 + 5 * self.coin5 + 10 * self.coin10

    def __lt__(self, rhs):
        # comparing the total money
        # between self and rhs
        return True if int(self) < int(rhs) else False

    def __str__(self):
        # return the strings that shows
        # the amount of each coin per
        # example
        return f"{{1:{self.coin1}, 2:{self.coin2}, 5:{self.coin5}, 10:{self.coin10}}}"

cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank() ; p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)


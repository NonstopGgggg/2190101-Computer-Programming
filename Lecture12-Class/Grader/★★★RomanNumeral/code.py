class roman:
    def __init__(self, r):
        self.roman = r
        
    def __lt__(self, rhs):
        return True if int(self) < int(rhs) else False
        
    def __str__(self):
        
        if isinstance(self.roman,int):
        
            num = self.roman
            table = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
            
            romanNum = ""
            for key in table:
                while num - key >= 0:
                    romanNum += table[key]
                    num -= key
                
            return romanNum
            
        return self.roman
        
    def __int__(self):
        table = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        r = self.roman
        total = sum([table[element] for element in r])
        
        # subtraction rule
        for i in range(len(r) - 1):
            if table[r[i]] < table[r[i+1]]:
                total -= table[r[i]] * 2
                
        return total
        
    def __add__(self, rhs):
        value1 = int(self)
        value2 = int(rhs)
        
        value = roman(value1 + value2)
        value = roman(str(value))
        
        return value

t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))



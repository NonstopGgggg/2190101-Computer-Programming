class Complex:
    """
    Class structure for a complex number (a + bi) implementation.
    """
    
    def __init__(self, a, b):
        """
        Initializes the complex number with real part 'a' and imaginary part 'b'.
        """
        self.real = a
        self.imagine = b

    def __str__(self):
        """
        Returns the string representation of the complex number.
        """
        # real part
        realPart = ""
        if self.real == 0:
            realPart = ""
            
        else:
            realPart = str(self.real)
           
        # imagine part
        imaginePart = "i"
        if self.imagine == 0 or self.imagine == 1:
            imaginePart *= self.imagine
            
        elif self.imagine == -1:
            imaginePart = "-i"
            
        else:
            imaginePart = str(self.imagine) + imaginePart

        # printing
        if realPart == "" and imaginePart == "":
            return "0"
        
        elif realPart == "":
            return imaginePart
        
        elif imaginePart == "":
            return realPart
        
        else:
            if imaginePart[0] == "-":
                return realPart + imaginePart
            
            else:
                return realPart + "+" + imaginePart

    def __add__(self, rhs):
        """
        Implements addition of two complex numbers (self + rhs).
        """
        realPart = self.real + rhs.real
        imaginePart = self.imagine + rhs.imagine
        
        return Complex(realPart,imaginePart)

    def __mul__(self, rhs):
        """
        Implements multiplication of two complex numbers (self * rhs).
        """
        # Placeholder for multiplication logic
        a = self.real
        b = self.imagine
        c = rhs.real
        d = rhs.imagine
        
        return Complex(a*c - b*d,a*d + b*c)

    def __truediv__(self, rhs):
        """
        Implements true division of two complex numbers (self / rhs).
        """
        # Placeholder for division logic
        a = self.real
        b = self.imagine
        c = rhs.real
        d = rhs.imagine
        
        realPart = (a*c + b*d) / (c*c + d*d)
        imaginePart = (-1*a*d + b*c) / (c*c + d*d)
        
        return Complex(realPart,imaginePart)
    
t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else : print(c1/c2)

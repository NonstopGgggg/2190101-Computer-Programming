# We are gievn a password and our task is to check if the password meets all the criteria
# If not print the unmet criteria in specific order as given:
# 1. less than 8 characters
# 2. no lowercase letter
# 3. no uppercase letter
# 4. no number
# 5. no symbol
# 6. character repetition
# 7. number sequence
# 8. letter sequence
# 9. keyboard sequence
# If all criteria are met print "OK"

def length(password):
    if len(password) < 8:
        return True
    return False

def noLowerCase(password):
    for char in password:
        if char.islower():
            return False
        
    return True

def noUpperCase(password):
    for char in password:
        if char.isupper():
            return False
        
    return True

def noNumber(password):
    for char in password:
        if char.isdigit():
            return False
    return True

def noSymbol(password):
    for char in password:
        if not char.isalnum():
            return False
    return True

def charRepetition(passw):
    password = passw.lower()

    for i in range(len(password) - 3):
        if password[i] == password[i + 1] == password[i + 2] == password[i + 3]:
            return True
        
# sequenceChecker checks if the given 4 character string is a sequence of numbers or letters or keyboard pattern.
def sequenceChecker(passw, keyword):
    password = passw.lower()

    if keyword == "num":
        # number sequences can be circular like 7890 or 8901
        num = ["0123456789","1234567890"]

        for number in num:
            if number.index(password[0]) + 1 == number.index(password[1]) and number.index(password[1]) + 1 == number.index(password[2]) and number.index(password[2]) + 1 == number.index(password[3]):
                return True
            
            elif number.index(password[0]) - 1 == number.index(password[1]) and number.index(password[1]) - 1 == number.index(password[2]) and number.index(password[2]) - 1 == number.index(password[3]):
                return True
        
    elif keyword == "letter":
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        if alphabet.index(password[0]) + 1 == alphabet.index(password[1]) and alphabet.index(password[1]) + 1 == alphabet.index(password[2]) and alphabet.index(password[2]) + 1 == alphabet.index(password[3]):
            return True
        
        elif alphabet.index(password[0]) - 1 == alphabet.index(password[1]) and alphabet.index(password[1]) - 1 == alphabet.index(password[2]) and alphabet.index(password[2]) - 1 == alphabet.index(password[3]):
            return True
        
    elif keyword == "keyboard":
        keyboard = ["!@#$%^&*()_+","qwertyuiop", "asdfghjkl", "zxcvbnm"]

        for row in keyboard:
            if password[0] in row and password[1] in row and password[2] in row and password[3] in row:
                if row.index(password[0]) + 1 == row.index(password[1]) and row.index(password[1]) + 1 == row.index(password[2]) and row.index(password[2]) + 1 == row.index(password[3]):
                    return True
                
                elif row.index(password[0]) - 1 == row.index(password[1]) and row.index(password[1]) - 1 == row.index(password[2]) and row.index(password[2]) - 1 == row.index(password[3]):
                    return True
                
    return False

    
def numSequence(password):
    for i in range(len(password) - 3):
        if password[i].isdigit() and password[i + 1].isdigit() and password[i + 2].isdigit() and password[i + 3].isdigit():
            if sequenceChecker(password[i:i+4], "num"):
                return True
        
    return False
            
def letterSequence(password):
    for i in range(len(password) - 3):
        if password[i].isalpha() and password[i + 1].isalpha() and password[i + 2].isalpha() and password[i + 3].isalpha():
            if sequenceChecker(password[i:i+4], "letter"):
                return True
            
    return False
            
def keyboardSequence(password):
    for i in range(len(password) - 3):
        if sequenceChecker(password[i:i+4], "keyboard"):
            return True
            
    return False
            
# input
password = input()
unmet = 0

# password validation
if length(password):
    print("Less than 8 characters")
    unmet += 1

if noLowerCase(password):
    print("No lowercase letters")
    unmet += 1

if noUpperCase(password):
    print("No uppercase letters")
    unmet += 1

if noNumber(password):
    print("No numbers")
    unmet += 1

if noSymbol(password):
    print("No symbols")
    unmet += 1

if charRepetition(password):
    print("Character repetition")
    unmet += 1

if numSequence(password):
    print("Number sequence")
    unmet += 1

if letterSequence(password):
    print("Letter sequence")
    unmet += 1

if keyboardSequence(password):
    print("Keyboard pattern")
    unmet += 1

if unmet == 0:
    print("OK")

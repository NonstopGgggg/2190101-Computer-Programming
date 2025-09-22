cipher = input()
n = len(cipher)

firstSet = ""
for i in range(3,n,7):
  firstSet += cipher[i]
  
secondSet = ""
for i in range(7,n,5):
  secondSet += cipher[i]

thirdSet = int(firstSet) +int(secondSet) + 10000

fourthSet = (thirdSet % 10000) // 10

fifthSet = fourthSet % 10 + (fourthSet // 10) % 10 + fourthSet // 100

digit = fifthSet % 10 + 1

sixthSet = chr(ord("A") + (digit-1))

print(fourthSet,end="")
print(sixthSet)

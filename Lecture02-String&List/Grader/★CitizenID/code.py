id = input()
checkDigit = 0

for i in range(12):
  checkDigit += (13-i) * int(id[i])
  
checkDigit = 11 - (checkDigit % 11)
checkDigit %= 10

print(id[0],id[1:5],id[5:10],id[10:13],checkDigit)

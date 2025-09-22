n = 0
sum = 0

while True:
  val = input()
  
  if val == 'q':
    break
  
  n += 1
  sum += float(val)
  
if n == 0:
  print("No Data")
  
else:
  print(f"{(sum / n):.2f}")

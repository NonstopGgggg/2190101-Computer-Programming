target = input()
start = 0
end = len(target)
mid = 0

target = float(target)

while end - start > 1E-10:
  mid = (end + start) / 2
  
  if 10 ** mid < target:
    start = mid
    
  else:
    end = mid
    
print(f"{mid:.6f}")

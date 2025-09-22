target = float(input())
start = 0
end = target
mid = 0

while end - start > 1E-10:
  mid = (start + end) / 2
  
  if 10 ** mid > target:
    end = mid
        
  else:
    start = mid
    
print(round(mid,6))

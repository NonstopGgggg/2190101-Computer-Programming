import numpy as np

def peak_indexes(x):
# x is an array containing values
# return an array listing indexes of “peaks”
  right = x[2:]
  left = x[:-2]
  mid = x[1:-1]
  
  index = (mid > left) & (mid > right)
  
  return np.arange(1,len(index)+1)[index]
    
def main():
  d = np.array([float(e) for e in input().split()])
  pos = peak_indexes(np.array(d))
  if len(pos) > 0:
      print(", ".join([str(e) for e in pos]))
  else:
      print("No peaks ")
        
exec(input().strip()) # Don't remove this line

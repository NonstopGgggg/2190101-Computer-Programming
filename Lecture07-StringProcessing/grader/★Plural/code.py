#A conditional code to turn singular to plural.

def transform_to_plural(s):
  new_s = ''
  # for s,x,ch
  if s[-1] == 's' or s[-1] == 'x' or s[-2:] == 'ch':
      new_s = s + 'es'
      
  # for y to ies
  elif s[-1] == 'y' and s[-2] not in "aeiou":
      new_s = s[:len(s)-1] + 'ies'
      
  # for general cases
  else:
      new_s = s + 's'
      
  return new_s

word = input()
print(transform_to_plural(word))

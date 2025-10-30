def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_coprime(a, b, c):
    # a, b, c are coprime if gcd(a, b, c) == 1
    return gcd(gcd(a, b), c) == 1

def primitive_Pythagorean_triples(max_len):
    triples = []
    m_limit = int(max_len**0.5) + 1
    
    for m in range(2,m_limit + 1):
      for n in range(1,m):
        if (m - n) % 2 == 0:
          continue
        if gcd(m,n) != 1:
          continue
        
        a = m*m - n*n
        b = 2*m*n
        c = m*m + n*n
        
        if c > max_len:
          break
        
        if a > b:
          a,b = b,a
          
        triples.append([a,b,c])
          
    return sorted(triples,key=lambda x: (x[2],x[0]))

exec(input().strip())  # required by grader


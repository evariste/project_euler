import math
import numpy


def isPrime_Eratosthenes(n):
  if (n < 2):
    return False
  elif (n == 2):
    return True
  elif (not n & 1): # n is even
    return False
  else:
    # Basic, test over possible odd divisors up to the approx square
    # root of n
    seq = [x for x in range(3, n/2, 2) if x*x < n+1]
    for d in seq:
      if n % d == 0:
        return False
  
  return True

def power_a_b_mod_n(a, index, n):
  # find a**b mod(n)
  if index < n:
    val = 1
    a = a % n # a mod(n)
    # The binary representation of the index can be used.
    # a**index can be expressed as a product of a subset of elements chosen from
    # a**1 a**2 a**4 a**8 ...
    # The subset corresponds to the ones in the binary representation of index
    if a == 0:
      return 0

    while (index > 0) & (val > 0):
      if index % 2 > 0:
        val = (val * a) % n
      a = (a * a) % n
      index = index / 2
    
    return val

  # If we got here then index >= n
  # Look for a cycle in the sequence of powers.
  storedPowers = numpy.zeros( (2*n) )
  storedPowers.dtype = 'int64'
  storedPowers[0] = a % n

  i = 1
  cycleFound = False
  while (i < 2*n) & (not cycleFound):
    curr = (a * storedPowers[i-1]) % n
    storedPowers[i] = curr
    if any(storedPowers[:i] == curr):
      start = numpy.where(storedPowers[:i] == curr)[0][0]
      cycleFound = True
      cycleLength = i - start
    i += 1

  if (i == 2*n) & (not cycleFound):
    print "Error : power_a_b_mod_n : no cycle found"
    exit()
  
  ind = start + (index -1 - start) % cycleLength
  return storedPowers[ind]



def isPrime_MillerRabin(n):
  if n < 1000:
    return isPrime_Eratosthenes(n)

  if (n > 4759123141):
    print 'isPrime_MillerRabin: number exceeds maximum testable with this version of algorithm (4759123141)'
    print 'result is not definite'

  if (not n & 1): # even.
    return False

  s = 0
  d = n - 1

  while (d % 2 == 0):
    s = s + 1
    d = d / 2

  a = [2, 7, 61]

  for i in range(3):
    aa = power_a_b_mod_n(a[i], d, n)

    isComposite = (aa != 1) and (aa != n-1) 

    if not isComposite:
      continue

    for r in range(1,s):
      isComposite = isComposite and ( power_a_b_mod_n(a[i], d*(2**r), n)  !=  (n-1) ) 

    if isComposite:
      return False

  return True

    



# Not great if numbers get very big.
def gen_primes():
  """ Generate an infinite sequence of prime numbers.
  """
  # Maps composites to primes witnessing their compositeness.
  # This is memory efficient, as the sieve is not "run forward"
  # indefinitely, but only as long as required by the current
  # number being tested.
  #
  D = {}  

  # The running integer that's checked for primeness
  q = 2  

  while True:
    if q not in D:
      # q is a new prime.
      # Yield it and mark its first multiple that isn't
      # already marked in previous iterations
      # 
      yield q        
      D[q * q] = [q]
    else:
      # q is composite. D[q] is the list of primes that
      # divide it. Since we've reached q, we no longer
      # need it in the map, but we'll mark the next 
      # multiples of its prime factors to prepare for larger
      # numbers
      # 
      for p in D[q]:
        D.setdefault(p + q, [ ]).append(p)
      del D[q]

    q += 1

# Not great if numbers get very big.
def gen_primesN(N):
  """ Generate a sequence of prime numbers up to and possibly including N.
  """
  # Maps composites to primes witnessing their compositeness.
  # This is memory efficient, as the sieve is not "run forward"
  # indefinitely, but only as long as required by the current
  # number being tested.
  #
  D = {}  

  # The running integer that's checked for primeness
  q = 2  

  while q < N:
    if q not in D:
      # q is a new prime.
      # Yield it and mark its first multiple that isn't
      # already marked in previous iterations
      # 
      yield q        
      D[q * q] = [q]
    else:
      # q is composite. D[q] is the list of primes that
      # divide it. Since we've reached q, we no longer
      # need it in the map, but we'll mark the next 
      # multiples of its prime factors to prepare for larger
      # numbers
      # 
      for p in D[q]:
        D.setdefault(p + q, [ ]).append(p)
      del D[q]

    q += 1


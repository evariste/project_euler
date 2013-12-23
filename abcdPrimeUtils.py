import math
import numpy
import itertools


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
  """ Generator object for an infinite sequence of prime numbers.
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
  """ Generator object a sequence of prime numbers up to and possibly including N.
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


def getNPrimes(N):
  """
  Create a list of primes up to or equal to N and return it.
  """
  g = gen_primesN(N)
  ps = []
  for p in g:
    ps = ps + [p]
  return ps



def primes_croft():
    """    from pyprimes.py
    Yield prime integers using the Croft Spiral sieve.

    This is a variant of wheel factorisation modulo 30.
    """
    # Implementation is based on erat3 from here:
    #   http://stackoverflow.com/q/2211990
    # and this website:
    #   http://www.primesdemystified.com/
    # Memory usage increases roughly linearly with the number of primes seen.
    # dict ``roots`` stores an entry x:p for every prime p.
    for p in (2, 3, 5):
        yield p
    roots = {9: 3, 25: 5}  # Map d**2 -> d.
    primeroots = frozenset((1, 7, 11, 13, 17, 19, 23, 29))
    selectors = (1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0)
    for q in itertools.compress(
            # Iterate over prime candidates 7, 9, 11, 13, ...
            itertools.islice(itertools.count(7), 0, None, 2),
            # Mask out those that can't possibly be prime.
            itertools.cycle(selectors)
            ):
        # Using dict membership testing instead of pop gives a
        # 5-10% speedup over the first three million primes.
        if q in roots:
            p = roots[q]
            del roots[q]
            x = q + 2*p
            while x in roots or (x % 30) not in primeroots:
                x += 2*p
            roots[x] = p
        else:
            roots[q*q] = q
            yield q



def factorise(n):
    """From pyprimes.py

    factorise(integer) -> yield factors of integer lazily

    >>> list(factorise(3*7*7*7*11))
    [(3, 1), (7, 3), (11, 1)]

    Yields tuples of (factor, count) where each factor is unique and usually
    prime, and count is an integer 1 or larger.

    The factors are prime, except under the following circumstances: if the
    argument n is negative, -1 is included as a factor; if n is 0 or 1, it
    is given as the only factor. For all other integer n, all of the factors
    returned are prime.
    """
    # TODO: check n is an integer , e.g.  if int(n + 0) != n

    if n in (0, 1, -1):
        yield (n, 1)
        return
    elif n < 0:
        yield (-1, 1)
        n = -n
    assert n >= 2
    for p in primes_croft():
        if p*p > n: break
        count = 0
        while n % p == 0:
            count += 1
            n //= p
        if count:
            yield (p, count)
    if n != 1:
#         if __debug__:
#             # The following test only occurs if assertions are on.
#             if _EXTRA_CHECKS:
#                 assert isprime(n), ('failed isprime test for %d' % n)
        yield (n, 1)

  

def allFactors(n):
  """
  generate all the factors of n (i.e. including composite factors).
  """
  pFacs = list(factorise(n))

  ps      = map(lambda (x,y): x, pFacs)
  indices = map(lambda (x,y): y, pFacs)

  nIndices = len(indices)

  indicesAddOne = map(lambda x: x+1, indices)

  nFactors = reduce(lambda x,y: x*y, indicesAddOne)

  # Each element is a cumulative product of preceding values
  cycleLengths = [1 for i in range(nIndices)]
  for i in range(1, nIndices):
    cycleLengths[i] = cycleLengths[i-1] * indicesAddOne[i-1]

  # Loop over all combinations of indices.
  for i in range(nFactors):
    fac = 1
    for j in range(nIndices):
      currInd = (i / cycleLengths[j]) % indicesAddOne[j]
      fac = fac * (ps[j] ** currInd)
    yield  fac

  # List comprehension, nicer but slower.
  #   y = map(lambda x: i / x, cycleLengths)
  #   y = zip(y, indicesAddOne)
  #   y = map(lambda (a,b): a % b, y)
  #   y = map(lambda (a,b): a ** b, zip(ps, y))
  #   y = reduce(lambda a,b: a*b, y)
  #   print y,


def allFactorisations(n):
  """
  Generate all factorisations (ordered).
  """
  store = []
  if isPrime_MillerRabin(n):
    store.append([n])
    yield [n]

  for f in allFactors(n):

    if f == 1 or f == n:
      if [n] in store:
        continue
      store.append([n])
      yield [n]
      continue

    for ff in allFactorisations(n / f):
      fact = [f] + ff
      fact.sort()
      if fact in store:
        continue
      store.append(fact)
      yield fact


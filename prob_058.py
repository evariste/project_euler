#!/usr/bin/env python

# Starting with 1 and spiralling anticlockwise in the following way, a
# square spiral with side length 7 is formed.

  # 37 36 35 34 33 32 31
  # 38 17 16 15 14 13 30
  # 39 18  5  4  3 12 29
  # 40 19  6  1  2 11 28 
  # 41 20  7  8  9 10 27
  # 42 21 22 23 24 25 26 
  # 43 44 45 46 47 48 49

# It is interesting to note that the odd squares lie along the bottom
# right diagonal, but what is more interesting is that 8 out of the 13
# numbers lying along both diagonals are prime; that is, a ratio of
# 8/13 \approx 62%.

# If one complete new layer is wrapped around the spiral above, a
# square spiral with side length 9 will be formed. If this process is
# continued, what is the side length of the square spiral for which
# the ratio of primes along both diagonals first falls below 10%?

# Solution: .

# Reading from the centre outwards, the numbers lying on the diagonals
# are:

# 1 3 13 31 : (2n)^2 - (2n-1) for n = 0, 1, 2, 3, .. 
# 1 5 17 37 : 1 + (2n)^2      for n = 0, 1, 2, 3, ..
# 1 7 21 43 : (2n)^2 + 2n + 1 for n = 0, 1, 2, 3, ..
# 1 9 25 49 : (2n+1)^2        for n = 0, 1, 2, 3, ..
#
# 0 2  4  6  : Differences reading downwards.
 
import sys
import math

# Using a generator object
def getCorners(n):
  # Give corners for square with edge length 1 + 2*num
  num  = 0
  a    = 1
  diff = 0
  while num < n:
    if num == 0:
      yield [1]
    else:
      a += 8*num-6
      yield [a, a+diff, a+2*diff, a+3*diff]
    num += 1
    diff += 2

# Version B:
# Only starts from num = 1, i.e. from a 3 by 3 square.
# I.e. it always returns a list of 4 values.
def getCornersB(n):
  # Give corners for square with edge length 1 + 2*num
  num  = 1
  a    = 1
  diff = 2
  while num < n:
    a += 8*num-6
    yield [a, a+diff, a+2*diff, a+3*diff]

    num += 1
    diff += 2


# Version C:
# As with version B but goes on for ever.
def getCornersC():
  # Give corners for square with edge length 1 + 2*num
  num  = 1
  a    = 1
  diff = 2
  while True:
    a += 8*num-6
    yield [a, a+diff, a+2*diff, a+3*diff]

    num += 1
    diff += 2


def isPrime(n):
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

# 1 3 13 31 : (2n)^2 - (2n-1) for n = 0, 1, 2, 3, .. 
# 1 5 17 37 : 1 + (2n)^2      for n = 0, 1, 2, 3, ..
# 1 7 21 43 : (2n)^2 + 2n + 1 for n = 0, 1, 2, 3, ..
# 1 9 25 49 : (2n+1)^2        for n = 0, 1, 2, 3, ..
#
# 0 2  4  6  : Differences reading downwards.


def firstn(g, n):
  for i in range(n):
    yield g.next()

def intsfrom(i):
  while 1:
    yield i
    i = i + 1

def exclude_multiples(n, ints):
  for i in ints:
    if (i % n > 0): yield i

def sieve(ints):
 while 1:
   prime = ints.next()
   yield prime
   ints = exclude_multiples(prime, ints)


def main(*args):
  x = 0
  currLen = 1
  primeCount = 0
  # Define each new square boundary as starting on the odd squares, 1,
  # 9, 25 ...
  squareStart = 1
  total = 1

  # 37 36 35 34 33 32 31
  # 38 17 16 15 14 13 30
  # 39 18  5  4  3 12 29
  # 40 19  6  1  2 11 28 
  # 41 20  7  8  9 10 27
  # 42 21 22 23 24 25 26 
  # 43 44 45 46 47 48 49


  for p in gen_primes():
    # which length square does current prime belong to?
    if p > squareStart:
      # Starting a new square
      currLen += 2
      #squareStart = currLen * currLen
      
      # 3 other corners apart from the square
      a = squareStart + currLen - 1
      b = a + currLen - 1
      c = b + currLen - 1
      
      percentPrime = float(primeCount)/total
      print '--- ' , currLen, primeCount, total, '%.3f' % percentPrime, squareStart

      if 10 * primeCount < 5 * total:
        percentPrime = float(primeCount)/total
        print
        print '--- ' , currLen-2, primeCount, total, '%.3f' % percentPrime, squareStart
        if primeCount > 0:
          break
# ---  3 0 1 0.000 1
# ---  26241 5248 52481 0.100 688590081

      total += 4
      squareStart += 4 * (currLen - 1)


    if (p == a) or (p == b) or (p == c):
      # Prime on a corner of square, i.e. on diagonal
      primeCount += 1


    

    
def mainSlowSlowSlow(*args):
  
  # List starts of with central 1, not prime
  primeCount = 0
  totalCount = 1
  sideLength = 1

  for s in getCornersC():
    primeCount += len(filter(isPrime, s))
    totalCount += 4
    sideLength += 2
    percentagePrime = 100.0 * primeCount / totalCount 
    print sideLength, '%.2f' % percentagePrime
    if percentagePrime < 33:
      print primeCount, totalCount, sideLength
      print '%.2f' % percentagePrime
      print
      break


if __name__ == '__main__':
  sys.exit(main(*sys.argv))



 


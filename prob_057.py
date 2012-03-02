#!/usr/bin/env python

# It is possible to show that the square root of two can be expressed
# as an infinite continued fraction.

# sqrt( 2 ) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

# By expanding this for the first four iterations, we get:

# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

# The next three expansions are 99/70, 239/169, and 577/408, but the
# eighth expansion, 1393/985, is the first example where the number of
# digits in the numerator exceeds the number of digits in the
# denominator.

# In the first one-thousand expansions, how many fractions contain a
# numerator with more digits than denominator?

# Solution: 153.


import sys

from fractions import Fraction

def expansion(n):
  if n < 1:
    return 0
  elif n == 1:
    return Fraction(1,2)
  else:
    return Fraction(1, 2 + expansion(n-1))

# Returns a fraction estimate
def estRoot2(n):
  return 1 + expansion(n)

# Expects a fraction
def testFraction(f):
  # numerator has more digits than denominator
  return len(repr(f.numerator)) > len(repr(f.denominator))

# Generate sequence of approximations to 1 + sqrt(2) 
# Modifies input argument by reference.
# [  The positive solution of x = 2 + (1/x) is 1+sqrt(2)  ]
def growListOfApproxs(seq):
  if seq == []:
    # Starting value.
    seq.append( 2 + Fraction(1,2) )
  else:
    seq.append(2 + Fraction(1, seq[-1]))

# Using a generator object
def approxSequence(n):
  num = 0
  val = 2
  while num < n:
    valNext = 2 + Fraction(1,val)
    yield valNext
    num += 1
    val = valNext

def main(*args):
  N = 1000

#   # Repeated applications of a recursive function - too much depth!
#   xs = map(estRoot2, range(1,N+1))
#   print len(filter(testFraction, xs))

  # Method 2
  # Grow a sequence with successive fractional approximations to
  # 1+sqrt(2) - much quicker.
  seq = [ ]
  for i in range(N):
    growListOfApproxs(seq)

  # Take one of the results.
  seq2 = map(lambda x:x-1, seq)

  # Find the fractions that have numerators with more digits than
  # their denominators
  print len(filter(testFraction, seq2))
  print "----"

  # Method 3: Use a purpose built generator, takes about the same time
  # as method 2
  seq3 = map(lambda x:x-1, approxSequence(N))
  print len(filter(testFraction, seq3))
  print "----"

if __name__ == '__main__':
  sys.exit(main(*sys.argv))






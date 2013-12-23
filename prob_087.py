


"""
The smallest number expressible as the sum of a prime square, prime
cube, and prime fourth power is 28. In fact, there are exactly four
numbers below fifty that can be expressed in such a way:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed as the sum of a
prime square, prime cube, and prime fourth power?
"""


from abcdPrimeUtils import *


maxVal = 50000000

print

p4s = []
p3s = []
p2s = []

pGen = primes_croft()

p = pGen.next()
p4 = p**4

while p4 < maxVal:
  p4s.append(p4)
  p3s.append(p4/p)
  p2s.append(p*p)
  p = pGen.next()
  p4 = p**4

p3 = p**3

while p3 < maxVal:
  p3s.append(p3)
  p2s.append(p*p)
  p = pGen.next()
  p3 = p**3

p2 = p*p

while p2 < maxVal:
  p2s.append(p2)
  p = pGen.next()
  p2 = p*p


l = [a+b+c for a in p2s for b in p3s for c in p4s if a+b+c < maxVal]

# This list contains duplicates as some numbers can be expressed as
# the sum of a square, cube and fourth power in more than one way.
print len(l)

# Fast way to find unique elements in a list
# See uniqifiers_benchmark.py

seen = set()
seen_add = seen.add
l2 = [ x for x in l if x not in seen and not seen_add(x)]

print len(l2)



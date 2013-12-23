
"""


A natural number, N, that can be written as the sum and product of a
given set of at least two natural numbers, {a1, a2, ... , ak} is
called a product-sum number: 

N = a1 + a2 + ... + ak = a1 x a2 x ... x ak.

For example, 6 = 1 + 2 + 3 = 1 x 2 x 3.

For a given set of size, k, we shall call the smallest N with this
property a minimal product-sum number. The minimal product-sum numbers
for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 x 2 = 2 + 2
k=3: 6 = 1 x 2 x 3 = 1 + 2 + 3
k=4: 8 = 1 x 1 x 2 x 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 x 1 x 2 x 2 x 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 x 1 x 1 x 1 x 2 x 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2 <= k <= 6, the sum of all the minimal product-sum numbers
is 4+6+8+12 = 30; note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for
2<=k<=12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for
2<=k<=12000?


"""



#import numpy
import abcdPrimeUtils

maxK = 12000

minPSnumber = [0 for i in range(maxK + 1)]

n = 3

# Bit of a slow method.
while any( map(lambda x: x<1, minPSnumber[2:]) ):
  n += 1

  # Loop over factorisations.
  for fac in abcdPrimeUtils.allFactorisations(n):
    if len(fac) < 2:
      continue

    k = len(fac) + n - sum(fac)

    if k > maxK:
      continue

    if minPSnumber[k] == 0:
      minPSnumber[k] = n
      # print n, k, sum(fac), fac


# for k in range(len(minPSnumber)):
#   print k , minPSnumber[k]


# Fast way to find unique elements in a list
# See uniqifiers_benchmark.py
l = minPSnumber[2:]

print 'uniquifying '
seen = set()
seen_add = seen.add
l2 = [ x for x in l if x not in seen and not seen_add(x)]

print l2, sum(l2)

print minPSnumber[maxK]


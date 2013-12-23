

"""

It is well known that if the square root of a natural number is not an
integer, then it is irrational. The decimal expansion of such square
roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital
sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the
digital sums of the first one hundred decimal digits for all the
irrational square roots.

Ans: 40886

"""

import math
from abcdNumericUtils import *


requiredDigits = 100

maxVal = 100

squares = [k*k for k in range(maxVal) if k*k <= maxVal]

totalSum = 0


for n in range(1 + maxVal):
  if n in squares:
    continue
  res, _, resStr = sqrtArbitraryPrecision(n, requiredDigits)
  print n, ' : ', resStr 
  totalSum += sum(res)


print totalSum




"""


# Fragment from http://apod.nasa.gov/htmltest/gifcity/sqrt2.1mil
s = '1.414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641572735013846230912297024924836055850737212644121497099935831'

print s[:101]

print sum( map(lambda x: int(x), s[0] + s[2:101]) )

"""

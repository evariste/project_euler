


# Consider the fraction, n/d, where n and d are positive integers. If
# n<d and HCF(n,d)=1, it is called a reduced proper fraction.

# If we list the set of reduced proper fractions for d <= 8 in
# ascending order of size, we get:

# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

# It can be seen that there are 21 elements in this set.

# How many elements would be contained in the set of reduced proper
# fractions for d <= 1,000,000?



# Note that they are not counting 0/1 and 1/1

# Answer: 303963552391

import math

# This function returns the length which _includes_ 0/1 and 1/1 ,
# i.e. two more than the length defined in the question.

# Uses formula

# | F( n ) | = (1/2) n (n+3) - sum_2^n  | F ( floor(n/d) ) |

def fareySequenceLength(n, cache = {}):

  if n < 1:
    return 0

  if n == 1:
    return 2

  if n == 2:
    return 3

  if cache.has_key(n):
    # May have already calculated the currently needed value.
    return cache[n]

  fLen  = n * (n + 3) / 2

  dEnd   = n
  dStart = n
  k = 1

  # Sum is calculated backwards.
  while dStart > 2:
    dStart = 1 + (n / k)
    k = k + 1
  
    if dStart > dEnd:
      continue

    # Now we should have floor(n/dEnd) = floor(n/dStart) and for every
    # value of d between dStart and dEnd. So we only need to make one
    # recursive call and multiply the result by the number of elements
    # between dStart and dEnd inclusive.

    floorNOverD = n / dStart
    val = fareySequenceLength(floorNOverD, cache)
    cache[floorNOverD] = val

    fLen = fLen - (1 + dEnd - dStart) * val

    dEnd = dStart - 1;

  return fLen



i = 1000000

l = fareySequenceLength(i) - 2

print i, l




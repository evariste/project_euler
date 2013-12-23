# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the
# 9-digit number, 134217728=8^9, is a ninth power.

# How many n-digit positive integers exist which are also an nth
# power?


# writing lg for log base 10, the number of digits in a number x is 

# 1 + floor(lg(x))

# if x = a^n, we want n = 1 + floor(lg(a^n)) = 1 + floor( n lg(a) )

# if lg(a) >= 1, then 

# 1 + floor( n lg(a) ) >= 1 + n

# so we need lg(a) < 1, i.e. 1 <= a < 10

# Clearly 1^n has n digits for n = 1 only


# The number of digits in a^(n+1) is

# 1 + floor( (n+1) lg(a) ) = 1 + floor( n lg(a) + lg(a) )

# Because lg(a) < 1, we either have

# floor( n lg(a) + lg(a) ) = floor( n lg(a) ) 

# or

# floor( n lg(a) + lg(a) ) = floor( n lg(a) ) + 1

# so, for 0 < a < 9, the number of digits in a^(n+1) either equals the
# number of digits in a^n or exceeds it by 1

# So we can check for each a in the range, incrementing n until it
# exceeds the number of digits in a^n and stopping there. We check
# along the way if n equals the number of digits.


import sys
from math import *

def noOfDigits(x):
  return int( 1 + floor(log10(x)))

###################################################################

def main(*args):
  count = 0
  for a in range(1, 10):
    n = 1

    while noOfDigits(a**n) >= n:
      if noOfDigits(a**n) == n:
        print '%d^%d = %d (%d digits)' % (a, n, a**n, noOfDigits(a**n))
        count += 1
      n += 1

  print
  print 'count = %d' % (count)
 
if __name__ == '__main__':
  sys.exit(main(*sys.argv))


###################################################################





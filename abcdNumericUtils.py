
from math import *
import fractions as fr

# function extended_gcd(a, b)
def gcd_ext(a,b):
  """
  Extended Euclidean algorithm.
  If r is the gcd of a and b then we can solve the equation
  x a + y b = r
  for integers x and y
  This function returns (x, y, r)
  """
  x, old_x = 0, 1
  y, old_y = 1, 0
  r, old_r = b, a
  while not r == 0:
    q = old_r / r
    old_r, r = r, old_r - q * r
    old_x, x = x, old_x - q * x
    old_y, y = y, old_y - q * y
  return (old_x, old_y, old_r)



def sqrtToContinuedFraction(n):
  """
  A square root can be written as a continued fraction

  sqrt(n) = a0 +  1
                 ---
                  a1 +  1
                       ---
                        a2 + ...

  The values a1, a2, ... eventually repeat so a compact representation
  is [a0 [a1, a2, ..., ak] ] where k is the end of the first cycle
  starting at a1.

  The a_i's can be found through a series of terms of the form
  x / (sqrt(n) - y).

  for example, writing r7 for sqrt(7), we have 2 < r7 < 3 so

  r7 = 2 + (r7 - 2) = 2 + ( (r7 - 2) / 1 )
     = 2 + 1 / (  1 / (r7 - 2) )

  here x = 1 and y = 2

  starting from 1 / (r7 - 2) , we can take the integer part to form
  then next a_i and subtract it away to get the next x and y

   1 / (r7 - 2)  =  [ 1 / (r7 - 2) ] * [ (r7 + 2) / (r7 + 2) ]
                 = ( r7 + 2 ) / (7 - 4)
                 = ( r7 + 2 ) / 3
                 = 1 + [ ( r7 + 2 - 3 ) / 3 ]
                 = 1 + [ ( r7 - 1 ) / 3 ]

  The next iteration then starts with the reciprocal of the last
  fraction:

  3 / (r7 - 1)

  i.e. x = 3 and y = 1 , etc.

  not described above are some steps to remove greatest common
  divisors to simplify the fractions as we go along.

  """
  rootN = sqrt(n)
  a0 = int(floor(rootN))

  if a0 * a0 == n:
    return [a0 , []]


  # term = x / (sqrt(n) - y)
  xy = [ (1, a0) ]
  a_rest = []

  while True:
    xPrev, yPrev = xy[-1]

    xCurr = n - yPrev * yPrev
    yCurr = xPrev * yPrev

    d = fr.gcd(xPrev, yCurr)
    xCurr /= d
    yCurr /= d

    aCurr = int(floor(rootN + yCurr)/xCurr)
    yCurr = - yCurr + xCurr * aCurr

    xy.append( (xCurr, yCurr) )
    a_rest.append( aCurr )

    # See if we're about to repeat the sequence
    if xy[-1] == xy[0]: break

  return [a0, a_rest]



#####################################################################

def getConvergent(contFrac, steps):
  """
  Get the convergent for the repeating continued fraction for a square
  root obtained after a certain number of steps using a recursive
  formula.  Does not actually make recursive calls, just uses a
  recursive formula within a single call.

  It can be assumed that the numerators in the continued fraction are
  all 1 and that, after the first term, the sequence repeats.  I.e has
  the form:

  b0 + 1 / (b1 + 1 / ( b2 + 1 / (b3 + ... 1 / (bk) ) )

  or

  [b0, [b1, b2, ..., bk] ]

  where the list [b1, b2, ..., bk] repeats.

  contFrac = [ b, list ] where b represents the first term and the
  list is repeated infinitely.

  E.g. the 5th convergent for [ b0, [b1, b2, b3, b4, b5, ...] ] is

    b0 + 1 / (b1 + 1 / ( b2 + 1 / (b3 + 1 / (b4) ) )

    steps  convergent:               Return
     1       b0                      (b0, 1)
     2       b0 + 1 / b1             (1 + b0 b1, b1)
     3       b0 + 1 / (b1 + 1 / b2)  (Use recursion, see below)

  """

  b0, b_rest = contFrac

  if steps == 1:
    return (b0, 1)

  if steps == 2:
    return (1 + b0 * b_rest[0], b_rest[0])

  index = steps - 2

  # index >= 3.

  # Let the nth convergent be A_n / B_n
  #
  # John Wallis's recurrence (see
  # http://en.wikipedia.org/wiki/Fundamental_recurrence_formulas )
  #
  # A_n = b_n A_{n-1} + a_n A_{n-2}
  #
  # B_n = b_n B_{n-1} + a_n B_{n-2}
  #
  # in our case, a_n = 1 always

  repeatLen = len(b_rest)
  index = 1
  stepsDone = 2

  # Terms just behind the current one (A_{n-1}, B_{n-1})
  A1,B1 = (1 + b0 * b_rest[0], b_rest[0])
  # Terms before that (A_{n-2}, B_{n-2})
  A2,B2 = (b0, 1)

  while stepsDone < steps:
    index = index % repeatLen

    An,Bn = (b_rest[index] * A1 + A2, b_rest[index] * B1 + B2)

    A2,B2 = (A1,B1)
    A1,B1 = (An,Bn)

    stepsDone += 1
    index += 1

  return (An, Bn)



"""
   Based on getConvergent above

"""
def approximateSqrtWithContFrac(contFrac, tol):
  if tol < 0:
    return 0

  b0, b_rest = contFrac

  numPrev   = b0
  denomPrev = 1

  numCurr   = 1 + b0*b_rest[0]
  denomCurr = b_rest[0]

  repeatLen = len(b_rest)

  # Terms just before the current one (A_{n-1}, B_{n-1})
  A1,B1 = (1 + b0 * b_rest[0], b_rest[0])
  # Terms before that (A_{n-2}, B_{n-2})
  A2,B2 = (b0, 1)

  index = 1

  An, Bn = 0, 0

  steps = 2

  while abs(A2 * B1 - A1 * B2) > tol * B1 * B2:
    index = index % repeatLen

    # A_n = b_n A_{n-1} + a_n A_{n-2}
    # B_n = b_n B_{n-1} + a_n B_{n-2}
    An,Bn = (b_rest[index] * A1 + A2, b_rest[index] * B1 + B2)

    A2,B2 = (A1,B1)
    A1,B1 = (An,Bn)

    index += 1
    steps += 1

  if An > 0:
    return (An, Bn, steps)

  return (A2, B2)

#########################################

# Return a list of digits of the square root of n to the required
# number of digits.  Also return the number of digits to the left of
# the point and a string representation.

# See method below and see also papers/squareRootsByBasicOps.pdf

def sqrtArbitraryPrecision(n, requiredDigits):

  if n < 0:
    return (0, 0, '0')

  k = 0
  while k*k <= n:
    k += 1

  k -= 1

  # How many digits to left of point in result?
  ansDigitsBeforePoint = len(str(k))

  # Space for result.
  result = [0 for i in range(requiredDigits)]

  if k * k == n:
    # Number is a square
    return (k, 0, str(k))


  # Don't have an exact square root.

  # Check if input number has a decimal point
  if '.' in str(n):
    nDigitsBeforePoint = str(n).index('.')
    nDigitsAfterPoint  = len(str(n)) - nDigitsBeforePoint - 1
    dotIndex = str(n).index('.')
  else:
    nDigitsBeforePoint = len(str(n))
    nDigitsAfterPoint  = 0
    dotIndex = len(str(n))

  # How many slots are needed for paired digits?
  nSlots  = (1 + nDigitsBeforePoint) / 2
  nSlots += (1 + nDigitsAfterPoint ) / 2

  # Pad string with zeros if necessary.
  padNStr = str(n)
  padNStr = padNStr[:dotIndex] + padNStr[1+dotIndex:]

  if nDigitsBeforePoint % 2 > 0:
    padNStr = '0' + padNStr

  if nDigitsAfterPoint % 2 > 0:
    padNStr = padNStr + '0'

  nPairs = len(padNStr) / 2

  # Finally make the pairs we will use.
  pairs  = [int(padNStr[2*i]+padNStr[2*i+1]) for i in range(nPairs)]

  # Start of with left most pair.
  k = 0
  while k*k <= pairs[0]:
    k += 1
  k -= 1

  # The first difference
  d = pairs[0] - k*k

  # First digit in answer.
  resultInd = 0
  result[resultInd] = k
  resultInd += 1

  """
  Rough layout: See method below function for details

           k  u  u ...
        +-------------
  k     |  n  ...
        | u*k
        +---------------
  k ... |  d
        |
  """
  nextPair = 1

  for i in range(requiredDigits - 1):

    d = d * 100

    if nextPair < nPairs:
      d += pairs[nextPair]
      nextPair += 1

    # double the unit digit with carry and multiply by ten
    k =  10 * ( k + (k % 10) )

    # Estimate for new unit digit.
    u = (d / k) % 10

    while u * (k + u) <= d:
      u += 1
    u -= 1

    k += u

    d -= u * k

    result[resultInd] = int(u)
    resultInd += 1


  resStr = ''.join(map(str, result))
  resStr = resStr[:ansDigitsBeforePoint] + '.' + resStr[ansDigitsBeforePoint:]

  return (result, ansDigitsBeforePoint, resStr)




"""http://johnkerl.org/doc/square-root.html

====================


How to manually find a square root

Here is an almost-forgotten art: one that, with the advent of
electronic calculators, will likely survive to the twenty-first
century only on paper and in the memories of oldsters.

What is the number you want to find the square root of? Here's one
we'll use:

46656

First, divide the number to be square-rooted into pairs of digits,
starting at the decimal point. That is, no digit pair should straddle
a decimal point. (For example, split 1225 into "12 25" rather than "1
22 5"; 6.5536 into "6. 55 36" rather than"6.5 53 6".)

Then you can put some lines over each digit pair, and a bar to the
left, somewhat as in long division.

     +--- ---- ----
     | 4   66   56

Find the largest number whose square is less than or equal to the
leading digit pair. In this case, the leading digit pair is 4; the
largest number whose square is less than or equal to 4 is 2.

Put that number on the left side, and above the first digit pair.

       2
     +--- ---- ----
  2  | 4   66   56

Now square that number, and subtract from the leading digit pair.

       2
     +--- ---- ----
  2  | 4   66   56
     |-4
     +----
       0

Extend the left bracket; multiply the last (and only) digit of the
left-hand number by 2, put it to the left of the difference you just
calculated, and leave an empty decimal place next to it.

       2
     +--- ---- ----
  2  | 4   66   56
     |-4
     +----
 4_  | 0

Then bring down the next digit pair and put it to the right of the
difference.

       2
     +--- ---- ----
  2  | 4   66   56
     |-4
     +----
 4_  | 0   66

Find the largest number to put in this blank decimal place such that
that number, times the number already there plus the decimal place,
will be less than the current difference. For example, see if 1 * 41
is <= 66, then 2*42 <= 66, etc. In this case it's a 1. Put this number
in the blank you left, and in the next decimal place on the result row
on the top.

       2    1
     +--- ---- ----
  2  | 4   66   56
     |-4
     +----
 41  | 0   66

Now subtract the product you just found.

       2    1
     +--- ---- ----
  2  | 4   66   56
     |-4
     +----
 41  | 0   66
     |-    41
     +--------
           25

Now, repeat as before: Take the number in the left column (here, 41)
and double its last digit (giving you 42). Copy this below in the left
column, and leave a blank space next to it. (Double the last digit
with carry: for example, if you had not 41 but 49, which is 40+9, you
should copy down 40+18 which is 58.) Also, bring down the next digit
pair on the right.

       2    1
     +--- ---- ----
  2  | 4   66   56
     |-4
     +----
 41  | 0   66
     |-    41
     +--------
42_        25   56

Now, find the largest digit (call it #) such that 42# * # <=
2556. Here, it turns out that 426 * 6 = 2556 exactly.

       2    1    6
     +--- ---- ----
  2  | 4   66   56
     |-4
     +----
 41  | 0   66
     |-    41
     +--------
426  |     25   56
     |-    25   56
     +-------------
                 0

When the difference is zero, you have an exact square root and you're
done. Otherwise, you can keep finding more decimal places for as long
as you want.

Here is another example, with less annotation.


          7 .  2  8  0  1 ...
       +----------------------
7      | 53 . 00 00 00 00 00
       | 49
       +----------------------
142    |  4   00
       |  2   84
       +----------------------
1448   |  1   16 00
       |  1   15 84
       +----------------------
14560  |         16 00
       |             0
       +----------------------
145601 |         16 00 00
       |         14 56 01
       +----------------------
       |          1 43 99 00
                         ...

John Kerl
john dot r dot kerl at lmco dot com
July, 1998

Current address (as of 2005):
kerl.john.r@gmail.com

       1   0
1      3  37  40
       1

2u     2  37

"""

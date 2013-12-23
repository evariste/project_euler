# Consider quadratic Diophantine equations of the form:

# x^2 - D y^2 = 1

# For example, when D=13, the minimal solution in x is 

#    649^2 - 13 x 180^2 = 1.

# It can be assumed that there are no solutions in positive integers
# when D is square.

# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain
# the following:

# 3^2 - 2 x 2^2 = 1
# 2^2 - 3 x 1^2 = 1
# 9^2 - 5 x 4^2 = 1
# 5^2 - 6 x 2^2 = 1
# 8^2 - 7 x 3^2 = 1

# Hence, by considering minimal solutions in x for D <= 7, the largest
# x is obtained when D=5.

# Find the value of D <= 1000 in minimal solutions of x for which the
# largest value of x is obtained.



# This is Pell's equation and it's solutions can be obtained by
# running through the convergents of sqrt(D) and checking the
# difference above.

from abcdNumericUtils import *


def seekTarget(contFrac, D, target):
  """" 
  Find successive convergents of a continued fraction in order to find
  a solution to Pell's equation.

  Uses the recursive formula used in abcdNumericUtils.getConvergent.

  This avoids multiple calls by running one set of evaluations for the
  convergents until a solution to the Pell equation

       x^2 - D y^2 = target

  is found.
  """

  b0, b_rest = contFrac

  # first step
  x = b0
  y = 1
  if x*x - D*y*y == target:
    return (x, y)

  # second step
  b1 = b_rest[0]
  x = 1 + b0 * b_rest[0]
  y = b_rest[0]
  if x*x - D*y*y == target:
    return (x, y)

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

  # Terms just behind the current one (A_{n-1}, B_{n-1})
  A1,B1 = (1 + b0 * b_rest[0], b_rest[0])
  # Terms before that (A_{n-2}, B_{n-2})
  A2,B2 = (b0, 1)

  x,y = (A2,B2)

  while x*x - D*y*y != target:
    index = index % repeatLen

    # Nth convergent terms
    x,y = (b_rest[index] * A1 + A2, b_rest[index] * B1 + B2)

    A2,B2 = (A1, B1)
    A1,B1 = (x, y)

    index += 1

  return (x, y)



maxD = 1000

allX = {}
allY = {}
for D in xrange(1, 1+maxD):
  rD = int(sqrt(D))
  if rD*rD == D: continue
  a, a_s = sqrtToContinuedFraction(D)
  x,y = seekTarget([a, a_s], D, 1)
  #print '%02d %+d %d, %d, %f' % (D, x*x - y*y*D , x, y, float(x)*x/y/y)
  allX[D] = x
  allY[D] = y


# for D in allX:
#   print D, allX[D], allY[D]

x, maxD = max([ (allX[D], D) for D in allX ])

print 'max x is %d, obtained by D = %d ' % (x, maxD)


x = allX[maxD]
y = allY[maxD]
print x
print y

print x*x - maxD * y * y


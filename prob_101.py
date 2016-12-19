'''If we are presented with the first k terms of a sequence it is
impossible to say with certainty the value of the next term, as there
are infinitely many polynomial functions that can model the sequence.

As an example, let us consider the sequence of cube numbers. This is
defined by the generating function,

u_n = n^3: 1, 8, 27, 64, 125, 216, ...

Suppose we were only given the first two terms of this
sequence. Working on the principle that "simple is best" we should
assume a linear relationship and predict the next term to be 15
(common difference 7). Even if we were presented with the first three
terms, by the same principle of simplicity, a quadratic relationship
should be assumed.

We shall define OP(k, n) to be the nth term of the optimum polynomial
generating function for the first k terms of a sequence. It should be
clear that OP(k, n) will accurately generate the terms of the sequence
for n <= k, and potentially the first incorrect term (FIT) will be
OP(k, k+1); in which case we shall call it a bad OP (BOP).

As a basis, if we were only given the first term of sequence, it would
be most sensible to assume constancy; that is, for n >= 2, OP(1, n) =
u1.

Hence we obtain the following OPs for the cubic sequence:

OP(1, n) = 1 	1, 1, 1, 1, ...
OP(2, n) = 7n - 6 	1, 8, 15, ...
OP(3, n) = 6n2 - 11n+6      	1, 8, 27, 58, ...
OP(4, n) = n3 	1, 8, 27, 64, 125, ...

Clearly no BOPs exist for k >= 4.

By considering the sum of FITs generated by the BOPs (indicated in red
above), we obtain 1 + 15 + 58 = 74.

Consider the following tenth degree polynomial generating function:

u_n = 1 - n + n^2 - n^3 + n^4 - n^5 + n^6 - n^7 + n^8 - n^9 + n^10

Find the sum of FITs for the BOPs.


Ans: 37076114526

'''

from scipy.interpolate import lagrange

import numpy as np
import math
from fractions import Fraction as fr



def lagrangePolySpecialised(xs,ys):
  ''' Lagrange interpolating polynomial, restricted to points on the integers
  1,...,n.  I.e. the xs argument is assumed to represent the integers 1 to n and
  the ys are assumed to be integer values.
'''
  if len(xs) == 1:
    return [ fr(ys[0],1) ]
  
  a,b = 0, len(xs)-1
  aa, bb = math.factorial(a), math.factorial(b)
  denom = pow(-1L, len(xs)-1)*aa*bb
  
  # lagrange poly is a sum of products. Each one has a denominator of the form
  # m! n! (-1)^n where m+n+1 = no of points. (I think)
  
  # Accumulate the coefficients as fractions.
  fracSum = [ fr(0,1) ] * len(xs)

  for k in range(len(xs)):
    # Find numerator term, this is a polynomial whose roots are the x values
    # except for one (the k index one).
    xx = xs[:k] + xs[k+1:]
    p = np.poly1d(xx,True)
    
    
    pCoeffs = map(long, p.coeffs)
    coeffFracs = map(lambda u: fr(u*ys[k], denom) , pCoeffs)
    summands = zip(fracSum, coeffFracs)
    fracSum = [x + y for (x,y) in summands]
    
    a = a + 1
    denom = -1L * denom * a / b
    b = max(1, b - 1)
  return fracSum


##################################################

def polyValSpecialised(cs, x):
  '''
  Evaluate a polynomial given by coefficients cs at x locations x. Used here for
  the case where cs are given as Fraction types and x is long long so that we
  can retain numeric accuracy.
  '''
  # How many points?
  nx = len(x)
  # Start of list for returned values returned values
  val = [cs[0]] * nx
  # Iteratively calculate polynomial values
  for c in cs[1::]:
    for i in range(nx):
      val[i] = val[i] * x[i] + c
  return val

##################################################

  
coeffs = np.ones((1,11), dtype=np.longlong)[0]
coeffs[1::2] = -1L
p = np.poly1d(coeffs)

x = map(lambda x: fr(x), range(1,12))
y = p(x)
print 'degree 10 polynomial'
print p
print 'x locations (integers)'
print x
print 'Values of degree 10 polynomial '
print y


sumFITs = 0L

for n in range(1,len(x)):
  p2 = lagrangePolySpecialised(x[0:n],y[0:n])
  
  print 'degree :' , n-1
  print ' polynomial using first {:d} terms'.format(n)
  print  p2
  val = polyValSpecialised(p2, x[n:n+1])
  print 'obtained value ', val
  print 'sequence value ', y[n:n+1]
  sumFITs = sumFITs + val[0]
  print '---'


print 'sum of FITs', sumFITs












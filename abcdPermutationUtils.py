

import math


def  factoradic2perm(digits):

# Convert a factoradic number into a permutation of n elements where n
# is the size of the vector 'digits' being passed.

# Permutation is assumed to be of the n element set {1, .., n}

# See Lehmer code:
# http://www.mathe2.uni-bayreuth.de/frib/KERBER/h00/node30.html

  n = len(digits);
  vals = range(1,n+1)


  p = [0 for i in range(n)]

  for i in range(n-1):
    d = digits[i]
    p[i] = vals[d]
    vals = vals[:d] + vals[d+1:]

  p[-1] = vals[0]

  return p


def index2factoradic(ind, n):

#  Find factoradic representation of decimal number ind which indexes
#  the permutations of n elements. The permutatons are
#  lexicographically ordered and their indices start at zero.
# 
#  The elements that are permuted are assumed to be '1', '2', . . ., 'n'
# 

  f = math.factorial(n-1);

  if ind > n*f - 1 or ind < 0:
    print 'index2factoradic: error : no such index'


  digits = [0 for i in range(n)]

  k = 1;
  while ind > 0:
    digits[k-1] = int(math.floor(ind / float(f)))
    ind = ind % f
    f = f / (n - k)
    k = k + 1


  return digits



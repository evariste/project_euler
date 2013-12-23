
import itertools
from scipy.misc import *


#####################
## Function to give the number of partitions of a given number - very
## slow before the caching part was put in.

# Uses the recursive formula 
# http://en.wikipedia.org/wiki/Partition_%28number_theory%29#Exact_formula
# based on generalised pentagonal numbers.

# Need to initialize the kinda static variable nPartitions.cache = {}
# before calling for the first time.

def nPartitions(n):
  if n < 0:
    return 0
  if n < 2:
    return 1
  if n in nPartitions.cache:
    return nPartitions.cache[n]

  pOfn = 0
  n1 = 1
  n2 = 1
  k = 0
  signFactor = 1

  # Initialise offsets to lower values. The offsets from n differ from
  # it by the pentagonal numbers.
  n1 = n
  n2 = n

  while n1 > 0 or n2 > 0:
    n1 = n1 - 3*k - 1
    n2 = n2 - 3*k - 2
    pOfn = pOfn + signFactor * (nPartitions(n1) + nPartitions(n2))
    k = k + 1
    signFactor = -1 * signFactor

  nPartitions.cache[n] = pOfn
  return pOfn

#############################################


def comb_numeric_to_list(c):
  """
  The binary representation of the number given shows which numbers
  from the set {0, .., N} are in the combination.  The number given
  is sometimes called a 'combinadic' and is part of the
  'combinatorial number system.
  """
  n = 0
  ret = [ ]
  while c > 0:
    if c & 1:
      ret = [n] + ret
    c = c >> 1
    n += 1

  return ret

def comb_list_to_numeric(li):
  """
  Convert a combination represented as a list of distinct numbers
  taken from {0, ..., N-1} into the combinadic number form.
  """
  c = 0  
  for n in li:
    c = c + (1 << n)
  return c

def combinations_numeric(N, k, startAfter = None):
  """
  Enumerate the combinations of k elements chosen from N in the
  numeric (combinadic) format where the set bits of each yielded value
  denote which elements are chosen.
  """
  if k > N or k < 1:
    return

  curr = 1
  for i in range(k-1):
    curr = curr | (curr << 1)

  last = curr << (N - k)

  if startAfter == None:
    count = 0
  else:
    bitCount = 0
    temp = startAfter
    # Count bits the Kernighan way!
    while temp > 0:
      bitCount += 1
      temp &= (temp-1)
    if bitCount != k:
      print 'combinations_numeric: incorrect bit count,',
      print 'k = %d, pattern = %s' % (k, bin(startAfter))
      return
    curr = startAfter
    count = 1
    
  # Based on the method described in Wikipedia for getting one binary
  # combinadic from the previous
  # one. http://en.wikipedia.org/wiki/Combinatorial_number_system
  while curr < last:
    if count == 0:
      count += 1
      yield curr

    x = curr
    ind = 0
    ones = 1
    while not(x & 1):
      x = x >> 1
      ind += 1
      ones |= (ones << 1)

    d = 1
    while x & 1:
      x >>= 1
      ind += 1
      ones = ones | (ones << 1)
      d |= (d << 1)

    x <<= ind
    d >>= 2
    ones >>= 1

    curr = (1+ones) | x | d
    yield curr


def combinations_as_lists(N, k):
  """
  Enumerate the combinations of k elements chosen from N ( [0, .., N-1] ).
  Return them as lists.
  """
  for c in combinations_numeric(N, k):
    yield comb_numeric_to_list(c)



def comb_to_comb_with_reps(c):
  """
  Input: a combination represented in numeric form.  Output: a
  combination represented in list form with repeated elements allowed,
  also known as a multiset.
  
  If the input is a combination of size k chosen from N elements, then
  c is viewed as a multiset of size k chosen from among N-k+1
  elements.
  """
  combWithReps = []
  countUnchosen = 0
  while c > 0:
    if c & 1:
      combWithReps.append(countUnchosen)
    else:
      countUnchosen += 1
    c >>= 1
  return combWithReps




# N = 8
# S = range(N)
# k=3
# allCs = {}

# startAfter = 69
# gen = combinations_numeric(N, k, startAfter)

# for c in gen:
#   print '%07d %03d' % (int(bin(c)[2:]), c),

#   combWithReps = comb_to_comb_with_reps(c)
#   print combWithReps

# exit()

# ####################


# i = 0
# for c in combinations_as_lists(N, 3):
#   i += 1
#   print i, c

# exit()

# #########################


# for c in gen:
#   print '%07d %03d' % (int(bin(c)[2:]), c),
#   li = comb_numeric_to_list(c)
#   print li, '   ', comb_list_to_numeric(li)

# exit()  

# ###############




# exact = 1

# for c in itertools.combinations(S, k):
#   c = list(c)
#   c.sort()
  
#   print c
#   sum = 0
#   for i in range(len(c)):
#     print comb(c[i], i+1, exact),
#     sum += comb(c[i], i+1, exact)
#   print '   ', sum,
#   if int(sum) == 10: print '  *',
#   print
#   c.sort()
#   c.reverse()
#   allCs[int(sum)] = c

# x = 0

# MAX = 2**N-1
# totalCount = 0
# for k in sorted(allCs.keys()):
#   totalCount += 1
#   b = 0
#   for n in allCs[k]:
#     b = b | (2**n)

#   bStore = b

#   print '%02d - ' % k, 
#   print allCs[k], 
#   val = int(bin(b)[2:])
#   print '%07d' % val,
#   val = gen.next()
#   print bin(val), '(', b, val, ')',
#   print comb_numeric_to_list(val)

# i = 0
# for c in combinations_as_lists(N, 3):
#   i += 1
#   print i, c


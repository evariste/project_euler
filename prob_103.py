

'''
Let S(A) represent the sum of elements in set A of size n. We shall call it a
special sum set if for any two non-empty disjoint subsets, B and C, the
following properties are true:

    S(B) <> S(C); that is, sums of subsets cannot be equal.
    If B contains more elements than C then S(B) > S(C).

If S(A) is minimised for a given n, we shall call it an optimum special sum set.
The first five optimum special sum sets are given below.

n = 1: {1}
n = 2: {1, 2}
n = 3: {2, 3, 4}
n = 4: {3, 5, 6, 7}
n = 5: {6, 9, 11, 12, 13}

It seems that for a given optimum set, A = {a1, a2, ... , an}, the next optimum
set is of the form B = {b, a1+b, a2+b, ... ,an+b}, where b is the "middle"
element on the previous row.

By applying this "rule" we would expect the optimum set for n = 6 to be A = {11,
17, 20, 22, 23, 24}, with S(A) = 117. However, this is not the optimum set, as
we have merely applied an algorithm to provide a near optimum set. The optimum
set for n = 6 is A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 and corresponding
set string: 111819202225.

Given that A is an optimum special sum set for n = 7, find its set string.

[20, 31, 38, 39, 40, 42, 45] 255


'''

from abcdCombinatorialUtils import generate_subsets, combinations_numeric, comb_numeric_to_list, generate_subsets_given_size
import numpy
from numpy.core.numeric import dtype
import itertools



def conway_guy_sequence(M):
  '''
  OEIS A005318. This sequence can be used to generate Subset-Sum-Distinct (SSD)
  sets. See the function subset_sum_distinct_set below.
  '''
  # a(n + 1) = 2a(n) - a(n - floor( 1/2 + sqrt(2n) )). 
  a = numpy.zeros((M+1,), dtype=numpy.long)
  if M < 1:
    return None
  
  a[0] = 0
  a[1] = 1
  for n in range(1,M):
    r = int(numpy.round(numpy.sqrt(2*n), 0))
    a[n+1] = 2 * a[n] - a[n-r]

  return a
  
  
def subset_sum_distinct_set(N):  
  '''
  Use the Conway-Guy sequence up to term N to generate a SSD set.
  '''
  a = conway_guy_sequence(N)

  print a
  
  b = numpy.zeros((N,), dtype=numpy.long)
  for i in range(1,N+1):
    b[i-1] = a[N] - a[N-i]

  return b


def sumReachable(L, targetValue):
  '''
  Is there a subset of integers in the list L that sum to the given value s?
  '''
  
  minVal = numpy.min(L)
  maxVal = numpy.sum(L)
  
  if targetValue > maxVal or targetValue < minVal:
    return False
  
  if numpy.any(L == targetValue):
    return True
  
  L.sort()
  if targetValue == L[0]:
    return True
  
  N = len(L)
  # Array to store accumulated values. Q(i,v) stores True/False depending on
  # whether there is a subset of the values [L_1, L_2, L_3, ..., L_i] that sum
  # to value v.
  
  sRange = range(minVal, maxVal+1)
  
  pairs = [(i,s) for i in range(N) for s in sRange ]
  Q = {}
  Q = Q.fromkeys(pairs, False)
  
  Q[(0,L[0])] = True

  for i in range(1,N):
    for s in sRange:
      Q[(i,s)] = Q[(i-1,s)] or (L[i] == s)
      if (not Q[(i,s)]) and s-L[i] >= minVal:
        Q[(i,s)] = Q[(i-1, s-L[i])]
    if Q[(i, targetValue)]:
      return True
  
  return False


##########################################


  
s = subset_sum_distinct_set(7)
print s

bestSum = sum(s)

currMax = max(s)
minVal = min(s)

# Keep min and max fixed and loop over all possible intermediate numbers.
k = len(s) - 2

while currMax < 3 + max(s):
  print 'current max: ', currMax
  
  ns = range(1+minVal, currMax)
  
  for intermediates in generate_subsets_given_size(ns, k):
    
    if minVal + sum(intermediates) + currMax > bestSum:
      continue
    
    vals = []
    valid = True
    currSet = [minVal] + intermediates + [currMax]
    
    for subset in generate_subsets(currSet):
      if subset == [] or subset == currSet:
        continue
      
      total = sum(subset)      
      if total in vals:
        valid = False
        break
      else:
        vals.append(total)
    if valid:
      print currSet, sum(currSet)
  
  currMax = currMax + 1
  
print 'done'

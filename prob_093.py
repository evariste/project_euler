"""By using each of the digits from the set, {1, 2, 3, 4}, exactly once,
and making use of the four arithmetic operations (+, −, *, /) and
brackets/parentheses, it is possible to form different positive
integer targets.

For example,

    8 = (4 * (1 + 3)) / 2
    14 = 4 * (3 + 1 / 2)
    19 = 4 * (2 + 3) − 1
    36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one
different target numbers of which 36 is the maximum, and each of the
numbers 1 to 28 can be obtained before encountering the first
non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the
longest set of consecutive positive integers, 1 to n, can be obtained,
giving your answer as a string: abcd.

Ans: 1258
"""


# Need to ensure division is treated as floating point division
from __future__ import division
import itertools
import sys



f1 = lambda x,y: x + y
f2 = lambda x,y: x - y
f3 = lambda x,y: x * y
f4 = lambda x,y: x / y
allF = [f1, f2, f3, f4]

allFStr = '+-*/'


funcPermutations = []
funcPermStrs = []



def getFuncPerms():
  ns = range(4)
  # Use global keyword so that we can write to the following variables.
  global funcPermutations
  global funcPermStrs

  for p in [ [a,b,c] for a in ns for b in ns for c in ns ]:
    currComb = (allF[p[0]], allF[p[1]], allF[p[2]] )
    funcPermutations = funcPermutations + [currComb] 
    currCombStr = (allFStr[p[0]], allFStr[p[1]], allFStr[p[2]] )
    funcPermStrs = funcPermStrs + [currCombStr]


def getCounts():
  noOfFuncPerms = len(funcPermutations)

  maxContiguousReached = 0

  # Take each combination of four numbers
  for c in itertools.combinations('123456789',4):
    # zero array to check what we can reach.
    # Largest value possible is 9*8*7*6 so need one more element in the zero-indexed array.
    reached = [0] * (9*8*7*6 + 1)

    # Take all permutations of the current set of four numbers.
    for p in itertools.permutations(c):
      a = map(int, p)

      # Loop over all choices of functions
      for fs in funcPermutations:

        # Case A: Functions applied from the left, i.e. if the
        # function set is f,g,h and numbers are a,b,c,d then we
        # calculate h( g( f(a,b), c), d)
        # 
        #         h
        #       /  \
        #      g    d
        #    /  \
        #   f    c
        #  / \
        # a   b

        val = a[0]
        for j in [0,1,2]:
          val = fs[j](val, a[j+1])

        if (val > 0) and (val == round(val)):
          reached[int(val)] = 1

        # Case B: Functions applied as in the following tree:
        #
        #      h
        #    /   \
        #   f     g
        #  / \   / \ 
        # a   b  c   d

        val1 = fs[0](a[0],a[1])
        val2 = fs[1](a[2],a[3])
        val  = fs[2](val1,val2)

        if (val > 0) and (val == round(val)):
          reached[int(val)] = 1


    # What is the longest contiguous set of reached numbers for the current combination?
    k = 1
    while k+1 < len(reached) and reached[k+1] > 0:
      k = k + 1

    # Have we hit a record?
    if k > maxContiguousReached:
      maxContiguousReached = k
      maxContiguousSet = c

  return(maxContiguousReached, maxContiguousSet)


################################

def listForSpecificCombination(c):
  noOfFuncPerms = len(funcPermutations)

  temp = {}

  #c = ('1', '2', '5', '8')

  reached = [0] * (9*8*7*6 + 1)

  for p in itertools.permutations(c):

    a = map(int, p)

    for i in range(noOfFuncPerms):
      fs = funcPermutations[i]
      val = a[0]
      for j in [0,1,2]:
        val = fs[j](val, a[j+1])

      iVal = int(val)
      if (val > 0) and (val == round(val)):
        reached[iVal] = 1
        temp[iVal] = ( a, funcPermStrs[i], 'A')

      val1 = fs[0](a[0],a[1])
      val2 = fs[1](a[2],a[3])
      val  = fs[2](val1,val2)

      iVal = int(val)
      if (val > 0) and (val == round(val)):
        reached[iVal] = 1
        temp[iVal] = ( a, funcPermStrs[i], 'B')


  # Print out the set, marker x indicates contiguity.
  # A or B indicates which tree structure is used for the evaluation (see above).
  ks = sorted(temp.keys())
  print ks[0], temp[ks[0]], 'x'
  for i in range(1, len(ks)):
    marker = ''
    if ks[i] == 1 + ks[i-1]:
      marker = 'x'
    print ks[i], temp[ks[i]], marker

    

###################################################################

def main(*args):
  # Figure out all the ways of permuting three basic functions
  getFuncPerms()
  # Apply to all combinations of numbers in all possible ways.
  (bestCount, bestSet) = getCounts()
  print bestCount, bestSet
  print ''

  # Show the results for the best.
  listForSpecificCombination(bestSet)


if __name__ == '__main__':
  sys.exit(main(*sys.argv))

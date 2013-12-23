
# The cube, 41063625 (345^3), can be permuted to produce two other
# cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the
# smallest cube which has exactly three permutations of its digits
# which are also cube.

# Find the smallest cube for which exactly five permutations of its
# digits are cube.

# 127035954683

import sys
from math import *

###################################################################

def main(*args):
  for noOfDigits in range(2,13):
    start = int( ceil( pow(10**(noOfDigits-1), (1/3.0)) ) )
    end   = int( ceil( pow(10**noOfDigits,     (1/3.0)) ) )

    cubes = [x**3 for x in range(start, end)]

    sortStrs = map( lambda x: ''.join(sorted(str(x))), cubes)

    digitsDict = {}
    for c in cubes:
      d = ''.join(sorted(str(c)))
      digitsDict.setdefault(d, []).append(c)

    listFound = []
    for d in digitsDict:
      if len(digitsDict[d]) == 5:
        print d, digitsDict[d]
        listFound = listFound + digitsDict[d]

    if any(listFound):
      val = min(listFound)
      print val, pow(val, (1/3.0))

if __name__ == '__main__':
  sys.exit(main(*sys.argv))


###################################################################


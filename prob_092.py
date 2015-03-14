
"""
A number chain is created by continuously adding the square of the
digits in a number to form a new number until it has been seen
before.

For example,

44 -> 32 -> 13 -> 10 -> 1 -> 1
85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89


Therefore any chain that arrives at 1 or 89 will become stuck in an
endless loop. What is most amazing is that EVERY starting number
will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

Ans: 8581146


To make it a bit faster:

Compile this code first in another script by calling 

import py_compile
py_compile.compile('prob_092.py')

then calling 

% time python prob_092.pyc
8581146

real	2m24.701s
user	2m23.031s
sys	0m0.601s

OR!

A starting number for which the sequence reaches 1 is called a HAPPY
number.

Take the list consisting of the number of happy numbers <= 10^n.
OEIS: A068571. For 10^7 this is 1418854 so the number required by
the question (the number that don't reach 1) is

10000000 - 1418854 = 8581146

"""

import numpy as np
import sys
import time


def main(*args):

    maxVal = 10000000

    # Storage for the ultimate destination from each starting number.
    endPoint = np.zeros( (maxVal,), dtype=np.uint8)

    endPoint[1] = 1
    endPoint[89] = 89

    for nStart in range(1,maxVal):
        n = nStart
        currList = []
        done = False

        while endPoint[n] == 0:
            # Append current number to list and find the next.
            currList = currList + [n]
            n = sum(int(x)**2 for x in str(n))


        endVal = endPoint[n]

        # Fill in the end points for each number in the list. Fill in
        # all its multiples by 10^k while we are at it. Seems to lead
        # to a bit of reduction in run time.
        for i in currList:
            while i < maxVal:
                endPoint[i] = endVal
                i = i * 10

    print np.count_nonzero( endPoint == 89 )


 
if __name__ == '__main__':
  sys.exit(main(*sys.argv))


#!/usr/bin/env python

# A googol (10^100) is a massive number: one followed by one-hundred
# zeros; 100^100 is almost unimaginably large: one followed by
# two-hundred zeros. Despite their size, the sum of the digits in each
# number is only 1.

# Considering natural numbers of the form, ab, where a, b < 100, what
# is the maximum digital sum?

# Solution 972 = digitSum( 99 ^ 95 )

import sys

def digitSum(n):
  # get string
  strN = filter (lambda x: x.isdigit(), repr(n))
  # get list
  n = map(int, strN) 
  return int( reduce(lambda a,b: a+b, n) )

def main(*args):
  N = 100
  ds = [(digitSum(a**b),a,b) for a in range(1,N) for b in range(1,N)]
  print
  print max(ds)
  m = 99**95
  print m
  print repr(m)
  print len(repr(m)) - 1 # 190 digits , excluding the python 'L'


if __name__ == '__main__':
  sys.exit(main(*sys.argv))






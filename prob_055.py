#!/usr/bin/env python


# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

# Not all numbers produce palindromes so quickly. For example,

# 349 + 943 = 1292,
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337

# That is, 349 took three iterations to arrive at a palindrome.

# Although no one has proved it yet, it is thought that some numbers,
# like 196, never produce a palindrome. A number that never forms a
# palindrome through the reverse and add process is called a Lychrel
# number. Due to the theoretical nature of these numbers, and for the
# purpose of this problem, we shall assume that a number is Lychrel
# until proven otherwise. 

# In addition you are given that for every number below ten-thousand,
# it will either 

#   (i) become a palindrome in less than fifty iterations, or, 

#   (ii) no one, with all the computing power that exists, has managed
#   so far to map it to a palindrome.

# In fact, 10677 is the first number to be shown to require over fifty
# iterations before producing a palindrome:

# 4668731596684224866951378664 (53 iterations, 28-digits).

# Surprisingly, there are palindromic numbers that are themselves
# Lychrel numbers; the first example is 4994.

# How many Lychrel numbers are there below ten-thousand?

# NOTE: Wording was modified slightly on 24 April 2007 to emphasise
# the theoretical nature of Lychrel numbers.

import sys

def flip(n):
  s = repr(n)
  if s[-1] == 'L':
    # Ignore the trailing 'L' in the long number. Flip only up to
    # penultimate character.
    return  int( s[-2::-1] )
  else:
    # Flip whole thing.
    return  int( s[::-1])

def isPalindrome(n):
  return n == flip(n)

# If a number n is a Lychrel number given k allowed iterations.
def isLychrel(n, k):
  if k == 0:
    return True
  else:
    next = n + flip(n)
    # print n , next, k
    return not isPalindrome(next) and isLychrel(next, k-1)

# For purposes of question
def isLychrelWrapper(n):
  return isLychrel(n, 50)

def main(*args):
  N = 10000
  #ly = filter(lambda x: isLychrel(x,50) , range(1,N))
  ly = filter(isLychrelWrapper, range(1,N))
  print ly
  print len(ly)

if __name__ == '__main__':
  sys.exit(main(*sys.argv))

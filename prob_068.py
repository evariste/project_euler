# Consider the following "magic" 3-gon ring, filled with the numbers 1
# to 6, and each line adding to nine.

#     4
#      \
#       3
#      / \
#     1 - 2 - 6
#    / 
#   5

# Working clockwise, and starting from the group of three with the
# numerically lowest external node (4,3,2 in this example), each
# solution can be described uniquely. For example, the above solution
# can be described by the set: 4,3,2; 6,2,1; 5,1,3.

# It is possible to complete the ring with four different totals: 9,
# 10, 11, and 12. There are eight solutions in total.

# Total	Solution Set

# 9	4,2,3; 5,3,1; 6,1,2
# 9	4,3,2; 6,2,1; 5,1,3
# 10	2,3,5; 4,5,1; 6,1,3
# 10	2,5,3; 6,3,1; 4,1,5
# 11	1,4,6; 3,6,2; 5,2,4
# 11	1,6,4; 5,4,2; 3,2,6
# 12	1,5,6; 2,6,4; 3,4,5
# 12	1,6,5; 3,5,4; 2,4,6

# By concatenating each group it is possible to form 9-digit strings;
# the maximum string for a 3-gon ring is 432621513.

# Using the numbers 1 to 10, and depending on arrangements, it is
# possible to form 16- and 17-digit strings. What is the maximum
# 16-digit string for a "magic" 5-gon ring?


import math
from abcdPermutationUtils import *
 
# Tri-gon : Place indices on outside 0,2,4 and inside 1,3,5

#     0 
#      \
#       1
#      / \
#     5 - 3 - 2
#    / 
#   4

x = [0 for i in range(6)]

# w.l.o.g we can try starting with 4 and work around

# smallest possible total is 6 + 1 + 2 = 9

# Assume 4 is in the first position.
x[0] = 4

bag = [0, 1, 2, 3, 5, 6]

n = len(bag) - 1

# for i in range(math.factorial(n)):
#   f = index2factoradic(i, n) 
#   p = factoradic2perm(f)
#   x[1:] = [bag[i] for i in p]
#   s0 = x[0] + x[1] + x[3]
#   if s0 < 9:
#     continue
#   s1 = x[2] + x[3] + x[5]
#   if not s0 == s1:
#     continue
#   s2 = x[1] + x[4] + x[5]
#   if not s0 == s2:
#     continue
#   print x[0] , x[1] , x[3]
#   print x[2] , x[3] , x[5]
#   print x[4] , x[5] , x[1]
#   print


      
# x0 + x1      + x3 
#           x2 + x3      + x5  
#      x1           + x4 + x5





#       0
#        \ 
#        1    2
#     /    \  /
#    9      3
#   /  \    /
#  8   7- 5 - 4
#       \
#        6
#

# Repeat above for 1 .. 10

x = [0 for i in range(10)]

# 10 can only appear once for the string to have 16 digits. I.e. 10
# must be on a leaf node (even index). WLOG set:
x[0] = 10

# Assume the largest string begins with a 6, i.e. 6 is also placed in
# a leaf node. This makes 4 choices of index for placing digit 6:
# 2,4,6 or 8

# Choose each one in turn, biggest answer given by 8
indForSix = 8

x[indForSix] = 6

takenInds = [0, indForSix]

leftInds = [i for i in range(len(x)) if i not in takenInds]

bag = range(10)

bag = filter(lambda x : not x == 6, bag)

n = len(bag) - 1

#       0
#        \ 
#        1    2
#     /    \  /
#    9      3
#   /  \    /
#  8   7- 5 - 4
#       \
#        6
#


for i in range(math.factorial(n)):
  f = index2factoradic(i, n) 
  p = factoradic2perm(f)
  currPerm = [bag[i] for i in p]

  j = 0
  for i in leftInds:
    x[i] = currPerm[j]
    j = j + 1

  s0 = x[0] + x[1] + x[3]

  sCurr = x[2] + x[3] + x[5]
  if not s0 == sCurr:
    continue

  sCurr = x[4] + x[5] + x[7]
  if not s0 == sCurr:
    continue

  sCurr = x[6] + x[7] + x[9]
  if not s0 == sCurr:
    continue

  sCurr = x[8] + x[9] + x[1]
  if not s0 == sCurr:
    continue


  print x[0] , x[1] , x[3]
  print x[2] , x[3] , x[5]
  print x[4] , x[5] , x[7]
  print x[6] , x[7] , x[9]
  print x[8] , x[9] , x[1]
  print


# Answer in 3s:

# 10 3 1
# 9 1 4
# 8 4 2
# 7 2 5
# 6 5 3

# 6531031914842725

#       10
#        \ 
#        3     9
#      /   \ /
#     5     1
#   /  \   /
#  6    2-4-8
#        \
#         7
#


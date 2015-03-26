'''If a box contains twenty-one coloured discs, composed of fifteen blue
discs and six red discs, and two discs were taken at random, it can be
seen that the probability of taking two blue discs, P(BB) =
(15/21)x(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of
taking two blue discs at random, is a box containing eighty-five blue
discs and thirty-five red discs.

By finding the first arrangement to contain over 10^12 =
1,000,000,000,000 discs in total, determine the number of blue discs
that the box would contain.

Ans: 756872327473


if b is the number of blue counters and t is the total number of
counters

the probability of blue in the first go is b/t and in the second it is
(b-1)/(t-1)

the probability of two blues in these goes is therefore b(b-1) / (
t(t-1) )

Setting this equal to 1/2 and rearranging gives

(2t-1)^2 - 2 (2b-1)^2 = 1

which can be viewed as a Pell type equation x^2 - n y^2 = -1 with n =
-2

'''
 

import numpy as np

# Seek solutions to x^2 - n y^2 = -1
#
# Can use the convergents to sqrt(2) in its continued fraction
# representation.
#
# AFAIK, the convergents xk,yk alternate between solving the two
# equations
#
# x^2 - n y^2 = -1   and    x^2 - n y^2 = 1
#
# We want the convergents for odd numbers of steps.

n = 2

# Get the convergent to sqrt(2) for step 2
x,y = 3L,2L

# Use to construct matrix that will iteratively generate convergents
# in steps that are two apart, e.g. starting at 1 and finding
# 3,5,7,... or starting at 2 and getting 4,6,8,...
M = np.asarray( [[x, n*y],[y, x]] , dtype=np.longlong)

# The convergent to sqrt(2) for step 1, note that here we have 1^2 -
# 2*1^2 = -1
xk,yk = 1L,1L
blue,total = (yk+1)/2, (xk+1)/2

while total < 1000000000000L:
  
  print xk, yk, pow(long(xk),2L) - 2L*pow(long(yk),2L)
  new = np.asarray( [xk, yk] , dtype=np.longlong ).T
  new = M.dot( new )
  xk,yk = new
  blue,total = (yk+1)/2, (xk+1)/2
  print '{:d} blue, {:d} in total'.format(blue, total)
  numerator = pow(long(blue),2L) - blue
  denom = pow(long(total),2L) - total
  print 2*numerator - denom
  
# 1 1 -1
# 3 blue, 4 in total
# 0
# 7 5 -1
# 15 blue, 21 in total
# 0
# 41 29 -1
# 85 blue, 120 in total
# 0
# 239 169 -1
# 493 blue, 697 in total
# 0
# 1393 985 -1
# 2871 blue, 4060 in total
# 0
# 8119 5741 -1
# 16731 blue, 23661 in total
# 0
# 47321 33461 -1
# 97513 blue, 137904 in total
# 0
# 275807 195025 -1
# 568345 blue, 803761 in total
# 0
# 1607521 1136689 -1
# 3312555 blue, 4684660 in total
# 0
# 9369319 6625109 -1
# 19306983 blue, 27304197 in total
# 0
# 54608393 38613965 -1
# 112529341 blue, 159140520 in total
# 0
# 318281039 225058681 -1
# 655869061 blue, 927538921 in total
# 0
# 1855077841 1311738121 -1
# 3822685023 blue, 5406093004 in total
# 0
# 10812186007 7645370045 -1
# 22280241075 blue, 31509019101 in total
# 0
# 63018038201 44560482149 -1
# 129858761425 blue, 183648021600 in total
# 0
# 367296043199 259717522849 -1
# 756872327473 blue, 1070379110497 in total
# 0

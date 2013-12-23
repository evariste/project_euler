# The square root of 2 can be written as an infinite continued
# fraction.

# The infinite continued fraction can be written, sqrt(2) = [1;(2)],
# (2) indicates that 2 repeats ad infinitum. In a similar way,
# sqrt(23) = [4;(1,3,1,8)].

# It turns out that the sequence of partial values of continued
# fractions for square roots provide the best rational
# approximations. Let us consider the convergents for sqrt(2).

# Hence the sequence of the first ten convergents for sqrt(2) are: 

# 1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

# What is most surprising is that the important mathematical constant,
# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

# The first ten terms in the sequence of convergents for e are: 2, 3,
# 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

# The sum of digits in the numerator of the 10th convergent is
# 1+4+5+7=17.

# Find the sum of digits in the numerator of the 100th convergent of
# the continued fraction for e.

# Solution 272

from abcdNumericUtils import *


cf = [1, [2]]
for n in range(1, 10): 
  (a,b) = getConvergent(cf, n)
  print '%d / %d : %.5f' % (a, b, float(a)*a/b/b  )

print


sz = 200
lst = [1 for i in range(sz)]
l = len(lst[1::3])
lst[1::3] = range(2, 2+2*l, 2)

cf = [2 , lst]
print cf
print

for n in range(1,10):
  (a,b) = getConvergent(cf, n)
  print '%d %d / %d : %.5f  %.5f' % (n, a, b, float(a)/b , log(float(a)/b) )


print

# Can't really call the recursive function for too many steps.
(a,b) = getConvergent(cf, 100)

print '%d / %d : %.5f  %.5f' % (a, b, float(a)/b , log(float(a)/b) )
print
sa = str(a)
print a
print sa
print sum( map(int, list(sa)) )

sm = 0
while a > 0:
  sm += a % 10
  a = a / 10

print sm



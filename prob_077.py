

# It is possible to write ten as the sum of primes in exactly five
# different ways:

# 7 + 3
# 5 + 5
# 5 + 3 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 2 + 2 + 2

# What is the first value which can be written as the sum of primes in
# over five thousand different ways?



import math

from abcdPrimeUtils import *

# Guess from online integer sequences on how far to go with checking.

maxN = 250

ps = getNPrimes(1 + maxN)


# Sum of distinct prime factors of n in the range 1, .., maxN
# http://oeis.org/A008472

sopf = [0 for i in range(1 + maxN)]

sopf[2] = 2

for n in range(3, 1+maxN):

  if n in ps:
    sopf[n] = n
  else:
    i = 0
    while n % ps[i] > 0:
      i = i + 1

    m = n 
    while m % ps[i] == 0:
      m = m / ps[i]

    sopf[n] = ps[i] + sopf[m]
    
##############

# See 
# http://programmingpraxis.com/2012/10/19/prime-partitions/
# http://oeis.org/A000607

 	

# T. D. Noe, Table of n, a(n) for n = 0..1000
# http://oeis.org/A000607/b000607.txt

# P. Flajolet and R. Sedgewick, Analytic Combinatorics, 2009; see page 580 


# kappa(n) = (1/n) * Sum_{j=1..n}  sopf(j) * kappa(n-j)

kappa = [0 for i in range(1 + maxN)]

kappa[0] = 1
kappa[1] = 0

for n in range(2, 1 + maxN):

  for j in range(1, n+1):
    kappa[n] = kappa[n] + sopf[j] * kappa[n - j]

  kappa[n] = kappa[n] / n

##############


temp = [i for i in range(len(kappa)) if kappa[i] <= 5000]

temp = temp[-1] + 1
print temp, kappa[temp] # 71, 5007




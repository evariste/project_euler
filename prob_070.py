


# Euler's Totient function, phi(n) [sometimes called the phi
# function], is used to determine the number of positive numbers less
# than or equal to n which are relatively prime to n. For example, as
# 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to
# nine, phi(9)=6.

# The number 1 is considered to be relatively prime to every positive
# number, so phi(1)=1.

# Interestingly, phi(87109)=79180, and it can be seen that 87109 is a
# permutation of 79180.

# Find the value of n, 1 < n < 10^7, for which phi(n) is a permutation
# of n and the ratio n/phi(n) produces a minimum.



# n / phi(n) at a minimum 

# subject to

# n and phi(n) being permuations of each other.


# phi(n) is always less than n 

# so n / phi(n) > 1

# want phi(n) as large as possible relative to n


# Prime numbers are an example of numbers with relatively large phi(n)

# for a prime p, phi(p) = p - 1

# As p grows p / phi(p) tends to one from above. I.e. we can make n /
# phi(n) as small as we like by choosing a sufficiently larger prime.


# But can this satisfy the permutation constraint?


# if a and b are decimal numbers whose digits are permutations of each
# other, then the digits of one can be re-arranged to obtain the
# digits of the other by a series of transpositions.

# A transposition of a decimal number written as 

# x_n ... x_i ... x_j ... x_0

# of digits x_i and x_j gives

# x_n ... x_j ... x_i ... x_0

# and the difference between the two is

# (x_i - x_j) (10^i - 10^j)

# which is a multiple of 9

# In other words, permuting the digits of a number preserves its
# modulo 9 value.


# So for a prime p with phi(p) = p - 1, we cannot have p and phi(p)
# being permutations of each other.


# What if n = p_1 p_2 , a product of two primes.

# In that case, phi(n) = (p1 - 1) (p2 - 1)
# = p1 p2 - p1 - p2 + 1 = n - (p1 + p2 - 1)

# So if p1 + p2 - 1 is a multiple of 9, we have a chance that n and
# phi(n) are permutations of each other.

# for p1 + p2 = 1 mod(9)



ps = []

count = 0

maxVal = 10**7

# Get the list of primes for which the product of any pair pq is less
# than the maximum.

f = open('firstMillionPrimes.txt')
for line in f:
  curr = int(line[:-1])
  if  curr > (maxVal/2):
    break
  ps.append(curr)

minRatio = 1000
bestN = 0
bestPhi = 0

for p in reversed(ps):
  for q in ps:

    n = p * q

    if n > maxVal:
      break

    r = (p + q) % 9
    if not r == 1:
      continue

    phi_n = n - p - q + 1

    if not sorted(str(n)) == sorted(str(phi_n)):
      continue

    rat = n / float(phi_n)
    if rat < minRatio:
      minRatio = rat
      bestN = n
      bestPhi = phi_n
      print n, phi_n, rat

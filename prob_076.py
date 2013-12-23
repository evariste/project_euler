# It is possible to write five as a sum in exactly six different ways:

# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1

# How many different ways can one hundred be written as a sum of at
# least two positive integers?


import abcdCombinatorialUtils




#Attempt Number 1:

# Number of partitions of n with parts of size k or less.
def F(n, k):
  if k == 0:
    return 0

  if n == 0:
    return 1

  if n < 0:
    return 0

  # First term: Partitions of n with all parts size k-1 or less

  # Second term: Partitions of n with at least one part having size k
  # - which is same as partitions of n-k with at least one part having
  # size k.

  # First and second terms count up two sets of partitions that have
  # no elements in common.
  return F(n, k-1) + F(n-k, k)


## Too slow!
# n = 100
# print F(n, n) - 1


#Attempt Number 2:

# Generalized pentagonal numbers
# 1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42

# Take pentagonal numbers until we are sure we have a value over 100, 20 will do.
n = 20

a = [x / 2 for x in range(2, n)]
b = [(-1)**(x) for x in range(len(a))]
k = map(lambda (x,y) : x*y, zip(a, b))
pents = map(lambda n : n * (3*n-1) / 2, k)


factors = map(lambda x: int( (-1)**(x-1) ) , k)


maxN = 100
p_n = [0 for i in range(1+maxN)]

p_n[0] = 1
p_n[1] = 1

for n in range(2, 1+maxN):
  i = 0
  while pents[i] <= n:
    p_n[n] = p_n[n] + factors[i] * p_n[ n - pents[i] ]
    i = i + 1



N = 100

# Exclude the single partition of size n (question asks for 'sums' only)
print  p_n[N] - 1 


# Attempt number 3, about the same speed as 2.
abcdCombinatorialUtils.nPartitions.cache = {}

print abcdCombinatorialUtils.nPartitions(N) - 1






# Let p(n) represent the number of different ways in which n coins can
# be separated into piles. For example, five coins can separated into
# piles in exactly seven different ways, so p(5)=7.

# OOOOO
# OOOO   O
# OOO   OO
# OOO   O   O
# OO   OO   O
# OO   O   O   O
# O   O   O   O   O

# Find the least value of n for which p(n) is divisible by one
# million.


from abcdCombinatorialUtils import nPartitions
 

nPartitions.cache = {}

n = 1

while nPartitions(n) % 1000000 > 0:
  n += 1

print n, nPartitions(n)
# 55374    and a very big number

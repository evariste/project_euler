# Consider the fraction, n/d, where n and d are positive integers. If
# n<d and HCF(n,d)=1, it is called a reduced proper fraction.

# If we list the set of reduced proper fractions for d <= 8 in
# ascending order of size, we get:

# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5,
# 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

# It can be seen that 2/5 is the fraction immediately to the left of
# 3/7.

# By listing the set of reduced proper fractions for d <= 1,000,000 in
# ascending order of size, find the numerator of the fraction
# immediately to the left of 3/7.


# Answer 428570

# Based on the Farey sequence: See 

# http://en.wikipedia.org/wiki/Farey_sequence

# In particular:


# If p/q has neighbours a/b and c/d in some Farey sequence, with

#     a/b < p/q < c/d

# then p/q is the mediant of a/b and c/d - in other words,

#     \frac{p}{q} = \frac{a + c}{b + d}.

# This follows easily from the previous property, since 
# if bp-aq = qc-pd = 1, 
# then bp+pd = qc+aq, p(b+d)=q(a+c), p/q = (a+c)/(b+d)

# It follows that if a/b and c/d are neighbours in a Farey sequence
# then the first term that appears between them as the order of the
# Farey sequence is increased is

#     \frac{a+c}{b+d},

# which first appears in the Farey sequence of order b + d.


### Alternatively!

# 3/7 == 428571/999999 ---> subtract one from numerator.
# Won't always work.

a = [2, 5]

b = [3, 7]

denomLimit = 10**6

while a[1] < denomLimit:
  aPrev = a
  a = map(lambda x,y: x+y, a, b)

a = aPrev
print a, a[0]/float(a[1])


print a[1] * b[0] - a[0] * b[1]




###################

## Graveyard

# represent fractions as pairs e.g. 3/7 -> (3, 7)

# The fractions equivalent to (3, 7) lie on a straight line : (3k,7k)

# For k = 1, 2, ...

# Two adjacent points on the line are (3k,7k) and (3k+3,7k+7)

# The sequence of fractions :

# From:
# 3k   7k

# 3k   7k+1
# 3k   7k+2
# 3k   7k+3

# 3k+1 7k+3
# 3k+1 7k+4
# 3k+1 7k+5

# 3k+2 7k+5
# 3k+2 7k+6
# 3k+2 7k+7

# To:
# 3k+3 7k+7

# Are all less than 3/7 

# Are all greater than the set of other fractions below 3/7 with
# numerators between 3k and 3k+3 and denominators between 7k and 7k+7

# The sequence is arranged in groups of three such that within each
# group, the first fraction is greater than the other two.

# This means that we only need to check fractions of the form

# Fraction     Denoted by
# 3k   7k+1     a_k
# 3k+1 7k+3     b_k
# 3k+2 7k+5     c_k

# k > 0 implies
# c_k > b_k > a_k 
#
# a_{k+1} = 3k+3 7k+8

# c_k - a_{k+1}
#   = 
#   = (38k+16-36k-15, ***) > 0

# c_k - b_{k+1}
#   = (3k+2, 7k+5) - (3k+4, 7k+10)
#   = (44k+20-43k-20, ***) > 0
#
# So far we have c_{k+1} > c_k > b_{k+1} > a_{k+1} 
#
# compare a_{k+1} and b_k
# a_{k+1} - b_k
#   = (3k+3, 7k+8) - (3k+1, 7k+3)
#   = (30k+9-31k-8, ***) = (-k+1, ***) < 0 for k > 1

# So far we have

# c_{k+1} > c_k > b_{k+1} > b_k > a_{k+1} > a_k

# Setting k to k+1
# c_{k+2} > c_{k+1} > b_{k+2} > b_{k+1} > a_{k+2} > a_{k+1}

# Need to compare c_k and b_{k+2} 
# Need to compare a_{k+2} and b_k
#
# to reconcile these two sequences
#
# b_{k+2} - c_k
#  = (3k+7, 7k+17) - (3k+2, 7k+5)
#  = (64k+35-65k-34, ***) = (-k+1, ***)
#  < 0 for k > 1
#
# so c_k > b_{k+2} for k > 1
#
# a_{k+2} - b_k
#  = (3k+6, 7k+15) - (3k+1, 7k+3)
#  = (51k+18-52k-15, ***)
#  = (-k+3, ***)
#
# so b_k > 
# Fraction     Denoted by
# 3k   7k+1     a_k
# 3k+1 7k+3     b_k
# 3k+2 7k+5     c_k
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

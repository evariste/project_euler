

# Consider the fraction, n/d, where n and d are positive integers. If
# n<d and HCF(n,d)=1, it is called a reduced proper fraction.

# If we list the set of reduced proper fractions for d <= 8 in
# ascending order of size, we get:

# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5,
# 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

# It can be seen that there are 3 fractions between 1/3 and 1/2.

# How many fractions lie between 1/3 and 1/2 in the sorted set of
# reduced proper fractions for d <= 12,000?

# Answer:
# 	7295372


# Use recursion formula for next term in sequence after two consecutive terms:

# http://en.wikipedia.org/wiki/Farey_sequence#Next_term

# Farey sequence order n:
# Given a/b c/d , two adjacent terms
# Pseudo code
# k = floor( (n + b) / d )
# next term will be (kc-a) / (kd-b)

# Modify the following from wikipedia:

def farey( n, asc=True ):
    """Python function to print the nth Farey sequence, either ascending or descending."""
    if asc: 
        a, b, c, d = 0, 1,  1  , n     # (*)
    else:
        a, b, c, d = 1, 1, n-1 , n     # (*)
    print "%d/%d" % (a,b)
    while (asc and c <= n) or (not asc and a > 0):
        k = int( (n + b) / d )
        a, b, c, d = c, d, k*c - a, k*d - b


# Start counting when you go past 1/3 and stop when you get to 1/2

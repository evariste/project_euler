'''
The first known prime found to exceed one million digits was discovered in 1999,
and is a Mersenne prime of the form 2^6972593-1; it contains exactly 2,098,960
digits. Subsequently other Mersenne primes, of the form 2p-1, have been found
which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains
2,357,207 digits: 2843 x 2**7830457 + 1.

Find the last ten digits of this prime number.

Ans : 9700303872


The cycle length of 2^k mod 10^m is 4*(5^(m-1)) and it starts at 2^m

See, e.g.

http://www.exploringbinary.com/cycle-length-of-powers-of-two-mod-powers-of-ten/

We can use this to avoid calculations involving numbers that are too large but
python seems to support arbitrary precision integers anyway.
'''


######################################

# Example. powers of 2 mod 100 (m=2) will start cycling at 2^2 = 4
# The length of the cycle is 4 * 5^1 = 20.

m = 2
powTen = 10**m

formatStr = '{:0' + str(m) +'d},'

# the powers before the cycle starts.
val = 1
for i in range(m-1):
  print formatStr.format(val)
  val = (val * 2) % powTen


cycleLen = 4 * (5 ** (m-1))

# Show a couple of cycles
for j in range(2):
  s = ''
  for i in range(cycleLen):
    val = (val * 2) % powTen
    s = s + formatStr.format(val)
  print s


######################################

# How about mod 1000?

m = 3
powTen = 10**m
cycleLen = 4 * (5 ** (m-1))

# If we want to find the modulus of 2^k directly we can do the following.
k = 2343
print (2**k) % powTen

# We know the cycle length is 4*5^2 = 100, so we don't need to evaluate 2^k directly.
# We can work out its position in the cycle (kk) and evaluate 2^kk instead, the result
# mod 10^m will be the same.

kk = m + (k - m) % cycleLen
print k, kk, (2**kk) % powTen

######################################

# The problem requires the last ten digits of the big prime so we are looking at
# mod 10^10

m = 10L
powTen = 10**m
cycleLen = 4 * (5 ** (m-1))

print 'cycle length is ', cycleLen

# The given power of two.
k = 7830457

# The position in the cycle
kk = m + (k - m) % cycleLen

# evaluate the power of two mod 10^m
# don't need to evaluate the whole power, keep finding the modulus each time.
val = 1L
for i in range(kk):
  val = (val * 2) % powTen

print kk
print val

# apply the multiplier and the addition given in the problem.
val = (val * 28433) % powTen
val = (val + 1) % powTen
print val


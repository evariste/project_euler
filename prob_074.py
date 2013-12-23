


# The number 145 is well known for the property that the sum of the
# factorial of its digits is equal to 145:

# 1! + 4! + 5! = 1 + 24 + 120 = 145

# Perhaps less well known is 169, in that it produces the longest
# chain of numbers that link back to 169; it turns out that there are
# only three such loops that exist:

# 169 -> 363601 -> 1454 -> 169
# 871 -> 45361 -> 871
# 872 -> 45362 -> 872

# It is not difficult to prove that EVERY starting number will
# eventually get stuck in a loop. For example,

# 69 -> 363600 -> 1454 -> 169 -> 363601 (-> 1454)
# 78 -> 45360 -> 871 -> 45361 (-> 871)
# 540 -> 145 (-> 145)

# Starting with 69 produces a chain of five non-repeating terms, but
# the longest non-repeating chain with a starting number below one
# million is sixty terms.

# How many chains, with a starting number below one million, contain
# exactly sixty non-repeating terms?


# Pre-calculate all the factorials for the digits 0 to 9

factorialsList = [1 for i in range(10)]

factorialsList[0] = 1
i = 1

while i < 10:
  factorialsList[i] = i * factorialsList[i-1]
  i = i + 1

##

def nextVal(curr):
  n = 0
  while curr > 0:
    unitDigit = curr % 10
    n = n + factorialsList[unitDigit]
    curr = curr / 10
    
  return n

len60Count = 0

# Starting numbers below 1 million.
for x in range(1, 1000000):
  count = 0
  intVals = []

  xx = x
  while not xx in intVals:
    intVals.append(xx)
    xx = nextVal(xx)
    count = count + 1
    if count > 60:
      break
  
  if count == 60:
    len60Count = len60Count + 1

print len60Count

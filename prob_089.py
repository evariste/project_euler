"""

The rules for writing Roman numerals allow for many ways of writing
each number (see About Roman Numerals...). However, there is always a
"best" way of writing a particular number.

For example, the following represent all of the legitimate ways of
writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

The last example being considered the most efficient, as it uses the
least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target
As...'), contains one thousand numbers written in valid, but not
necessarily minimal, Roman numerals; that is, they are arranged in
descending units and obey the subtractive pair rule (see About Roman
Numerals... for the definitive rules for this problem).

Find the number of characters saved by writing each of these in their
minimal form.

Note: You can assume that all the Roman numerals in the file contain
no more than four consecutive identical units


Ans: 743.

"""


digitLookup = { 'M':1000 , 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

# Pairs where a lower digit is allowed to be on the left of a higher one.
subPairs = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']

def roman2arabic(r):
  """
  Convert from a roman representation to an Arabic one. The Roman
  representation need not be the most efficient.
  """
  lenR = len(r)
  totalVal = 0
  prevVal  = 0
  prevDigit = ''

  # Read from right end backwards
  for i in range(len(r)-1, -1, -1):
    currDigit = r[i]
    val = digitLookup[currDigit]

    if val < prevVal:
      # Must be an allowed subtractive pair.
      if currDigit + prevDigit in subPairs:
        totalVal -= val
      else:
        print 'format error'
        return 0
    else:
      totalVal += val

    prevVal   = val
    prevDigit = currDigit

  return totalVal

def arabic2roman(a):
  """
  Convert from Arabic to Roman representation as efficiently as possible.
  """
  r = ''

  n = a / 1000
  r = r + 'M' * n

  a -= 1000 * n

  n = a / 100
  if n in [0, 1, 2, 3]:
    r = r + 'C' * n
  elif n == 4:
    r = r + 'CD'
  elif n in [5, 6, 7, 8]:
    r = r + 'D' + 'C' * (n - 5)
  else:
    r = r + 'CM'

  a -= 100 * n

  n = a / 10
  if n in [0, 1, 2, 3]:
    r = r + 'X' * n
  elif n == 4:
    r = r + 'XL'
  elif n in [5, 6, 7, 8]:
    r = r + 'L' + 'X' * (n - 5)
  else:
    r = r + 'XC'

  a -= 10 * n

  n = a
  if n in [0, 1, 2, 3]:
    r = r + 'I' * n
  elif n == 4:
    r = r + 'IV'
  elif n in [5, 6, 7, 8]:
    r = r + 'V' + 'I' * (n - 5)
  else:
    r = r + 'IX'


  return r






filename = 'prob_089.txt'

f = open(filename)

savedChars = 0

for line in f:
  curr = line[:-1]
  a = roman2arabic(curr)
  r = arabic2roman(a)
#   if len(curr) == len(r):
#     print curr, a, r,  len(curr), len(r)
  savedChars += len(curr) - len(r)
  print r

print 'Saved ' , savedChars, ' characters'


"""
Alternative: but this won't deal properly with lots of repeated X's say.

  cp prob_089.txt temp.txt 
  sed -i -e 's/VIIII/IX/g' temp.txt 
  sed -i -e 's/IIII/IV/g' temp.txt 
  sed -i -e 's//IV/g' temp.txt 
  sed -i -e 's/LXXXX/XC/g' temp.txt 
  sed -i -e 's/XXXX/XL/g' temp.txt 
  sed -i -e 's/DCCCC/CM/g' temp.txt 
  sed -i -e 's/CCCC/CD/g' temp.txt 
"""


"""

How do you read and write Roman numerals?

Traditional Roman numerals are made up of the following denominations:

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

You will read about many different rules concerning Roman numerals,
but the truth is that the Romans only had one simple rule:

Numerals must be arranged in descending order of size.

For example, three ways that sixteen could be written are XVI,
XIIIIII, VVVI; the first being the preferred form as it uses the least
number of numerals.

The 'descending size' rule was introduced to allow the use of
subtractive combinations. For example, four can be written IV because
it is one before five. As the rule requires that the numerals be
arranged in order of size it should be clear to a reader that the
presence of a smaller numeral out of place, so to speak, was
unambiguously to be subtracted from the following numeral. For
example, nineteen could be written XIX = X + IX (9). Note also how the
rule requires X (ten) be placed before IX (nine), and IXX would not be
an acceptable configuration.

Generally the Romans tried to use as few numerals as possible when
displaying numbers. For this reason, XIX would be the preferred form
of nineteen over other valid combinations, like XVIIII or
XVIV. However, this was NOT a rule and there still remain in Rome many
examples where economy of numerals has not been employed. For example,
in the famous Colesseum the the numerals above the forty-ninth
entrance is written XXXXVIIII and not IL nor XLIX (see rules below).

Despite this, over time we have continued to introduce new restrictive
rules. By mediaeval times it had become standard practice to avoid
more than three consecutive identical numerals. That is, IV would be
written instead of IIII, IX would be used instead of VIIII, and so
on. In addition, the subtractive combinations had the following rules
superimposed:

    Only I, X, and C can be used as the leading numeral in part of a
    subtractive pair.

    I can only be placed before V and X.
    X can only be placed before L and C.
    C can only be placed before D and M.

These last four rules are considered to be law, and generally it is
preferred, but not necessary, to display numbers using the minimum
number of numerals. Which means that IL is considered an invalid way
of writing forty-nine, and whereas XXXXVIIII, XXXXIX, XLVIIII, and
XLIX are all quite legitimate, the latter is the preferred (minimal)
form.

It is also expected that higher denominations should be used whenever
possible; for example, L should be used in place of XXXXX, or C should
be used in place of LL. However, even this 'rule' has been flaunted:
in the church of Sant'Agnese fuori le Mura (St Agnes' outside the
walls), found in Rome, the date, MCCCCCCVI (1606), is written on the
gilded and coffered wooden ceiling; I am sure that many would argue
that it should have been written MDCVI.

However, if we believe the adage, 'when in Rome do as the Romans do,'
and we see how the Romans write numerals, then it clearly gives us
much more freedom than many would care to admit.

"""

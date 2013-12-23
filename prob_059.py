#!/usr/bin/env python

# Each character on a computer is assigned a unique code and the
# preferred standard is ASCII (American Standard Code for Information
# Interchange). For example, uppercase A = 65, asterisk (*) = 42, and
# lowercase k = 107.

# A modern encryption method is to take a text file, convert the bytes
# to ASCII, then XOR each byte with a given value, taken from a secret
# key. The advantage with the XOR function is that using the same
# encryption key on the cipher text, restores the plain text; for
# example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

# For unbreakable encryption, the key is the same length as the plain
# text message, and the key is made up of random bytes. The user would
# keep the encrypted message and the encryption key in different
# locations, and without both "halves", it is impossible to decrypt
# the message.

# Unfortunately, this method is impractical for most users, so the
# modified method is to use a password as a key. If the password is
# shorter than the message, which is likely, the key is repeated
# cyclically throughout the message. The balance for this method is
# using a sufficiently long password key for security, but short
# enough to be memorable.

# Your task has been made easy, as the encryption key consists of
# three lower case characters. Using cipher1.txt (right click and
# 'Save Link/Target As...'), a file containing the encrypted ASCII
# codes, and the knowledge that the plain text must contain common
# English words, decrypt the message and find the sum of the ASCII
# values in the original text.


# Python uses the caret ^ operator to represent XOR !

import re

def xor_on_list(val, ns):
  return map(lambda x: val^x, ns)

f = file('prob_059-data.txt')
raw = f.read()
f.close()

# Get rid of trailing newline
raw = raw[:-1]

rawList = raw.split(',')

rawInts = map(int, rawList)

print 'Length of list is %u' % len(rawInts)
print

# Range of lower case characters
testLetters = range(ord('a'), 1 + ord('z'))

maxHits = [0, 0, 0]
achievedBy = [0, 0, 0]

for i in range(len(testLetters)):

  xorInts = xor_on_list(testLetters[i], rawInts) #  map(lambda x: x^testLetters[i], rawInts)

  s = "".join( map(chr, xorInts) )

  for j in range(3):
    s2 = re.findall(r'[a-zA-Z;., ]', s[j::3])
    if maxHits[j] < len(s2):
      maxHits[j] = len(s2)
      achievedBy[j] = i

candidate = ''
for ind in achievedBy:
  candidate = candidate + chr( testLetters[ind] )


print 'Candidate key is %s' % candidate    # 'god'
print 'with these hits %u %u %u' % tuple(maxHits)


for i in range(3):
  curr = testLetters[achievedBy[i]]
  rawInts[i::3] = xor_on_list(curr, rawInts[i::3])

ss = "".join( map(chr, rawInts) )

print ss

# ' (The Gospel of John, chapter 1) ...'

# Sum of the ascii values in the original list

print sum(rawInts)




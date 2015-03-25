
'''


By replacing each of the letters in the word CARE with 1, 2, 9, and 6
respectively, we form a square number: 1296 = 36^2. What is remarkable is that,
by using the same digital substitutions, the anagram, RACE, also forms a square
number: 9216 = 96^2. We shall call CARE (and RACE) a square anagram word pair and
specify further that leading zeroes are not permitted, neither may a different
letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, find all the square anagram
word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.


'''

#  18769 17689 (('BOARD', 'BROAD'), [0, 2, 3, 1, 4])
#  
#  9604 4096 (('RATE', 'TEAR'), [3, 2, 0, 1])
#  9604 4096 (('POST', 'STOP'), [3, 2, 0, 1])
#  9216 1296 (('CARE', 'RACE'), [2, 1, 0, 3])
#  9216 1296 (('NOTE', 'TONE'), [2, 1, 0, 3])
#  9216 1296 (('FILE', 'LIFE'), [2, 1, 0, 3])
#  4761 1764 (('DEAL', 'LEAD'), [3, 1, 2, 0])
#  4761 1764 (('SHUT', 'THUS'), [3, 1, 2, 0])
#  4096 9604 (('MEAN', 'NAME'), [2, 3, 1, 0])
#  2401 1024 (('RATE', 'TEAR'), [3, 2, 0, 1])
#  2401 1024 (('POST', 'STOP'), [3, 2, 0, 1])
#  1936 1369 (('HATE', 'HEAT'), [0, 2, 3, 1])
#  1936 1369 (('MALE', 'MEAL'), [0, 2, 3, 1])
#  1764 4761 (('DEAL', 'LEAD'), [3, 1, 2, 0])
#  1764 4761 (('SHUT', 'THUS'), [3, 1, 2, 0])
#  1296 9216 (('CARE', 'RACE'), [2, 1, 0, 3])
#  1296 2916 (('POST', 'SPOT'), [1, 2, 0, 3])
#  1296 9216 (('NOTE', 'TONE'), [2, 1, 0, 3])
#  1296 9216 (('FILE', 'LIFE'), [2, 1, 0, 3])
#  1296 2916 (('EAST', 'SEAT'), [1, 2, 0, 3])
#  1024 2401 (('MEAN', 'NAME'), [2, 3, 1, 0])
#  
#  961 169 (('DOG', 'GOD'), [2, 1, 0])
#  961 196 (('NOW', 'OWN'), [2, 0, 1])
#  625 256 (('ITS', 'SIT'), [1, 2, 0])
#  625 256 (('EAT', 'TEA'), [1, 2, 0])
#  625 256 (('HOW', 'WHO'), [1, 2, 0])
#  256 625 (('NOW', 'OWN'), [2, 0, 1])
#  196 961 (('ITS', 'SIT'), [1, 2, 0])
#  196 961 (('EAT', 'TEA'), [1, 2, 0])
#  196 961 (('HOW', 'WHO'), [1, 2, 0])
#  169 961 (('DOG', 'GOD'), [2, 1, 0])


import math
import itertools
import sys


def readData():
  f = file('prob_098_words.txt')
  data = list(f)
  words = data[0].split(',')
  words = map(lambda x: x.replace('"', ''), words)
  f.close()
  return words

def distinctCharCounts(aStr):
  '''
  Return a list of the character counts in a string.
  '''
  distinctChars = list(set(aStr))
  counts = [0] * len(distinctChars)
  
  for i in range(len(distinctChars)):
    c = distinctChars[i]
    counts[i] = sum(map(lambda x: x == c, aStr))
  return sorted(counts)
  
  
def getPermutationForAnagram(s1, s2):
  '''
  Two strings where one is an anagram of the other. Get the permutation that
  transforms one to the other. e.g. if s2 = DOG and s2 = GOD then we return 210
  because 0->2, 1->1, 2->0
  '''
  p = []
  unmarked = [True] * len(s2)
  for i in range(len(s1)):
    c = s1[i]
    
    charMatch = map(lambda x: x == c, s2)
    charMatch = [x and y for (x,y) in zip(charMatch, unmarked)]
    
    j = 0
    while not charMatch[j]:
      j = j + 1

    p.append( j )
    unmarked[j] = False

  return p

def checkLookup(number, word):
  ''' 
  Assuming digits/letters in the same position correspond, find the lookup
  between digits and letters. Check if it is one to one, i.e. there are no
  distinct digits that map to the same letter and no distinct letters that map
  to the same digit.

  This is to prevent situations such as the following:
  
  The square nubmers (209691, 992016) and the words ('FORMER', 'REFORM') are
  both related by the same permuation. One of each pair can be made into the
  other under the permuation given by [2, 3, 0, 5, 1, 4]. BUT, ..., there is no
  one-one correspondence.
  
  209691    992016
  FORMER    FORMER
  
  both give a mapping where digit 9 is mapped to different letters and letter R
  is mapped to different digits.

  The digit count and word count of word and number shoud be the same.
  '''
  lookup = zip(str(number), word)
  lookup = list(set(lookup))
  for pairing in itertools.combinations(lookup, 2):
    lookupA = pairing[0]
    lookupB = pairing[1]
    if lookupA[0] == lookupB[0] or lookupA[1] == lookupB[1]:
      return False 
  
  return True

def applyPerm(s, p):
  '''
  Apply the permutation represented by the index set p to the string s and
  return the resulting string
  '''
  return ''.join([s[n] for n in p])



def main(*args):

  words = readData()

  wordsSorted = map(lambda x : ''.join(sorted(x)), words)
  
  # Dictionary, key will be the sorted letters of each word, value is a list of all words with
  # the same letters as the key. Most entries have a list of one word only. If more than one
  # word is in the list for a particular key then we have an anagram.
  d = {}
  d = d.fromkeys(set(wordsSorted))
  
  for k in d.keys():
    d[k] = []
    
  
  for i in range(len(wordsSorted)):
    sw = wordsSorted[i]
    w = words[i]
    d[sw] = d[sw] + [w]
  longestAnag = 0

  for k in d.keys():
    ws = d[k]
    if len(ws) > 1:
      if len(k) > longestAnag:
        longestAnag = len(k)
  
  anags = {}
  anags = anags.fromkeys(range(1+longestAnag))
  for k in anags.keys():
    anags[k] = []
  
  for k in d.keys():
    noOfLetters = len(k)
    ws = d[k]
    if len(ws) > 1:
      anags[noOfLetters].append(ws)
    
  print 'The anagrams'
  for k in anags.keys():
    if len(anags[k]) > 0:
      print anags[k]
  
  print ''
  
  counts = [0] * (1+longestAnag)
  
  for k in anags.keys():
    counts[k] = len(anags[k])
  
  for nDigits in range(longestAnag, 1, -1):
    
    if counts[nDigits] < 1:
      continue
    
    suffix = ''
    if counts[nDigits] > 1:
      suffix = 's'
    print 'Checking for {:0d} digits, {:1d} anagram set{:s}.'.format( nDigits, counts[nDigits], suffix)
    
  
    # Get character patterns for current set.
    charCounts = []
    permsFound = []
    for anag in anags[nDigits]:
      w = anag[0]
      patt = distinctCharCounts(w)
      if not patt in charCounts:
        charCounts.append(patt)
        
      # Cannot always assume that anagrams are in exact pairs, may have triples.
      for ws in itertools.combinations(anag,2):
        perm = getPermutationForAnagram(ws[0], ws[1])
        permsFound.append((ws, perm))
    
    # Find all square numbers with current number of digits, work backwards from
    # the largest.
    maxPowTen = 10**nDigits
    minPowTen = 10**(nDigits-1)
    m = int( math.floor(math.sqrt(maxPowTen)) )
    sqNos = []
    m2 = m*m
  
    while m2 >= minPowTen:
      sqNoDigitCounts = distinctCharCounts(str(m2))
      checks = map(lambda x: x == sqNoDigitCounts, charCounts)
      # Only include a square number if its digits are a potential match to one
      # of the words in the anagram sets.
      if any(checks):
        sqNos.append(m2)
      m = m - 1
      m2 = m*m

    for sqA in sqNos:
      sqNoDigitCounts = distinctCharCounts(str(sqA))
      
      for p in permsFound:
        wordA = p[0][0]
        wordB = p[0][1]
        perm = p[1]

        letterCounts = distinctCharCounts(wordA)
        
        if not letterCounts == sqNoDigitCounts:
          continue

        sqB = int(applyPerm(str(sqA), perm))
        
        # Do we actually have a square number?
        if not sqB in sqNos:
          continue
        
        # Number is unaffected by the permutation
        if sqB == sqA:
          continue
        
        # Check if a sensible mapping between digits and letters is possible.
        if not checkLookup(sqA, wordA):
          continue
         
        if not checkLookup(sqB, wordA):
          continue

        # Success:
        print sqA, sqB, p
        
        
        
if __name__ == '__main__':
  sys.exit(main(*sys.argv))

# n the card game poker, a hand consists of five cards and are ranked,
# from lowest to highest, in the following way:

#     High Card: Highest value card.
#     One Pair: Two cards of the same value.
#     Two Pairs: Two different pairs.
#     Three of a Kind: Three cards of the same value.
#     Straight: All cards are consecutive values.
#     Flush: All cards of the same suit.
#     Full House: Three of a kind and a pair.
#     Four of a Kind: Four cards of the same value.
#     Straight Flush: All cards are consecutive values of same suit.
#     Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of
# the highest value wins; for example, a pair of eights beats a pair
# of fives (see example 1 below). But if two ranks tie, for example,
# both players have a pair of queens, then highest cards in each hand
# are compared (see example 4 below); if the highest cards tie then
# the next highest cards are compared, and so on.

# Consider the following five hands dealt to two players:

# Hand            Player 1                Player 2                Winner

# 1               5H 5C 6S 7S KD          2C 3S 8S 8D TD
#                 Pair of Fives           Pair of Eights          Player 2

# 2               5D 8C 9S JS AC          2C 5C 7D 8S QH
#                 Highest card Ace        Highest card Queen      Player 1
 
# 3               2D 9C AS AH AC          3D 6D 7D TD QD
#                 Three Aces              Flush with Diamonds     Player 2

# 4               4D 6S 9H QH QC          3D 6D 7H QD QS
#                 Pair of Queens          Pair of Queens
#                 Highest card Nine       Highest card Seven      Player 1

# 5               2H 2D 4C 4D 4S          3C 3D 3S 9S 9D
#                 Full House              Full House
#                 With Three Fours        with Three Threes       Player 1


# The file, poker.txt, contains one-thousand random hands dealt to two
# players. Each line of the file contains ten cards (separated by a
# single space): the first five are Player 1's cards and the last five
# are Player 2's cards. You can assume that all hands are valid (no
# invalid characters or repeated cards), each player's hand is in no
# specific order, and in each hand there is a clear winner.

# How many hands does Player 1 win?

# Solution: 376


import sys
import re


filename = "prob_054_poker.txt"
#filename = "temp.txt"

pictureCards = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14} # or 1?

suitVal = {'C':1, 'D':2, 'H':3, 'S':4}

rankNames = ['High Card', 'One Pair', 'Two Pairs', 'Three of a Kind', 'Straight', 'Flush', 'Full House', 'Four of a Kind', 'Straight Flush', 'Royal Flush']

def getCardAndSuit(str):
  card = str[0];
  suit = str[1];
  if re.match("[TJQKA]", card):
      card = pictureCards[card];
  else:
      card = int(card)
  suit = suitVal[suit]
  return (card, suit)

def getCards(hand):
  return map (lambda (a,b): a,  hand)

def getSuits(hand):
  return map(lambda (a,b): b, hand)


# Rank functions: All of these assume the hand is sorted in decreasing
# order of cards

#     High Card: Highest value card.
def highCard(hand):

  return (True, hand)

#     One Pair: Two cards of the same value.
def onePair(hand):

  xs = getCards(hand)
  a = xs[0]
  b = xs[1]
  c = xs[2]
  d = xs[3]

  if xs[0:2] == [a,a]:
    return (True, [a] + xs)
  elif xs[1:3] == [b,b]:
    return (True, [b] + xs)
  elif xs[2:4] == [c,c]:
    return (True, [c] + xs)
  elif xs[3:5] == [d,d]:
    return (True, [d] + xs)
  else:
    return (False, None)

#     Two Pairs: Two different pairs.
def twoPairs(hand):

  xs = getCards(hand)
  a = xs[0]
  b = xs[2]
  c = xs[4]

  if xs == [a,a,b,c,c]:
    return (True, [c, a] + xs)
  elif xs == [a,b,b,c,c]:
    return (True, [c, b] + xs)
  elif xs == [a,a,b,b,c]:
    return (True, [b, a] + xs)
  else:
    return (False, None)

#     Three of a Kind: Three cards of the same value.
def threeOfAKind(hand):

  xs = getCards(hand)
  a = xs[0]
  b = xs[1]
  c = xs[2]

  if xs[0:3] == [a,a,a]:
    return (True, [a] + xs)
  if xs[1:4] == [b,b,b]:
    return (True, [b] + xs)
  if xs[2:5] == [c,c,c]:
    return (True, [c] + xs)
  else:
    return (False, None)

#     Straight: All cards are consecutive values.
def straight(hand):

  xs =  getCards(hand)
  consecutives = range( xs[0], xs[0] - len(xs), -1)
  
  if xs == consecutives: # | xs == [1,2,3,4,14] ?
    return (True, hand)
  else:
    return (False, None)

#     Flush: All cards of the same suit.
def flush(hand):

  suits = getSuits(hand)
  if all( map( lambda x : x == suits[0], suits) ):
    return (True, getCards(hand))
  else:
    return (False, None)

#     Full House: Three of a kind and a pair.
def fullHouse(hand):

  xs = getCards(hand)
  a = xs[0]
  b = xs[-1]

  if xs == [a,a,a,b,b]:
    return (True, [a, b] + xs)
  elif xs == [a,a,b,b,b]:
    return (True, [b, a] + xs)
  else:
    return (False, None)

#     Four of a Kind: Four cards of the same value.
# pre: hand is sorted
def fourOfAKind(hand):

  xs = getCards(hand)
  a = xs[0]
  b = xs[-1]

  if xs == [a,a,a,a,b]:
    return (True, [a] + xs)
  if xs == [a,b,b,b,b]:
    return (True, [b] + xs)
  else:
    return (False, None)

#     Straight Flush: All cards are consecutive values of same suit.
def straightFlush(hand):

  if (flush(hand)[0] & straight(hand)[0]):
    return (True, hand)
  else:
    return (False, None)

#     Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
def royalFlush(hand):
  if (straightFlush(hand)[0] & hand[0][0] == 10):
    return (True, hand)
  else:
    return (False, None) 

rankFuncs = [highCard, onePair, twoPairs, threeOfAKind, \
               straight, flush, fullHouse, fourOfAKind, \
               straightFlush, royalFlush]


def scoreHand(hand):
  curr = len(rankFuncs)
  matched = False
  while not matched:
    curr = curr - 1
    f = rankFuncs[curr]
    val = f(hand)
    matched = val[0]
  # Return a list with [rankNumber, top card, .., top card, hand]
  return [curr] + val[1]
      
def printScore(hand):
  sc = scoreHand(hand)

  print rankNames[ sc[0] ] , ' hi card ', sc[1]

def compareHands(h1, h2):
  #print h1, h2
  h1copy = h1[:]
  h2copy = h2[:]

  h1 = map(getCardAndSuit, h1);
  h2 = map(getCardAndSuit, h2);

  h1.sort()
  h2.sort()
  h1.reverse()
  h2.reverse()
  
  sc1 = scoreHand(h1)
  sc2 = scoreHand(h2)

#   if sc1 > sc2:
#     print '1: ', h1copy , rankNames[ sc1[0] ]
#     print '   beats'
#     print '2: ', h2copy , rankNames[ sc2[0] ]
#   elif sc2 > sc1:
#     print '2: ', h2copy , rankNames[ sc2[0] ]
#     print '   beats'
#     print '1: ', h1copy , rankNames[ sc1[0] ]
#   else:
#     print h1copy
#     print ' ties with '
#     print h2copy
#   print

  if sc1 > sc2:
    return 1
  elif sc2 > sc1:
    return 2
  else:
    return 0
  print
  
def main(*args):
  f = open(filename);
  n = 0
  scores = [0, 0, 0]
  
  for line in f:
    # The hands
    h = line.split()
    h1 = h[0:5]
    h2 = h[5:]

    winner = compareHands(h1, h2)
    scores[winner] += 1

  print scores



if __name__ == '__main__':
    sys.exit(main(*sys.argv))

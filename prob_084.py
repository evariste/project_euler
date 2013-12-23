"""


In the game, Monopoly, the standard board is set up in the following way:

GO A1 CC1 A2 T1 R1 B1 CH1 B2 B3 JAIL
H2                              C1
T2                              U1
H1                              C2
CH3                             C3
R4                              R2
G3                              D1
CC3                             CC2
G2                              D2
G1                              D3
G2J F3 U2 F2 F1 R3 E3 E2 CH2 E1 FP

A player starts on the GO square and adds the scores on two 6-sided
dice to determine the number of squares they advance in a clockwise
direction. 

Without any further rules we would expect to visit each square with
equal probability: 2.5%. However, landing on G2J (Go To Jail), CC
(community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders
the player to go directly to jail, if a player rolls three consecutive
doubles, they do not advance the result of their 3rd roll. Instead
they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a
player lands on CC or CH they take a card from the top of the
respective pile and, after following the instructions, it is returned
to the bottom of the pile. 

There are sixteen cards in each pile, but for the purpose of this
problem we are only concerned with cards that order a movement; any
instruction not concerned with movement will be ignored and the player
will remain on the CC/CH square.

    Community Chest (2/16 cards):
        Advance to GO
        Go to JAIL

    Chance (10/16 cards):
        Advance to GO
        Go to JAIL
        Go to C1
        Go to E3
        Go to H2
        Go to R1
        Go to next R (railway company)
        Go to next R
        Go to next U (utility company)
        Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a
particular square. That is, the probability of finishing at that
square after a roll. For this reason it should be clear that, with the
exception of G2J for which the probability of finishing on it is zero,
the CH squares will have the lowest probabilities, as 5/8 request a
movement to another square, and it is the final square that the player
finishes at on each roll that we are interested in. 

We shall make no distinction between "Just Visiting" and being sent to
JAIL, and we shall also ignore the rule about requiring a double to
"get out of jail", assuming that they pay to get out on their next
turn.

By starting at GO and numbering the squares sequentially from 00 to 39
we can concatenate these two-digit numbers to produce strings that
correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in
order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO
(3.09%) = Square 00. So these three most popular squares can be listed
with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find
the six-digit modal string.

Answer

Length 4:

10, 15, 24

"""

import numpy as np
import random as rnd

np.set_printoptions(precision=4)
np.set_printoptions(suppress=True)


diceLen = 4

rolls = range(2, 1+2*diceLen)
rollRelFreqs = range(1, diceLen) + range(diceLen, 0, -1)
rollProbs = np.array(rollRelFreqs) / float(diceLen * diceLen)


sqs = {
0  : 'GO',      1  : 'A1',      2  : 'CC1',     3  : 'A2',      4  : 'T1',
5  : 'R1',      6  : 'B1',      7  : 'CH1',     8  : 'B2',      9  : 'B3',
10 : 'JAIL',    11 : 'C1',      12 : 'U1',      13 : 'C2',      14 : 'C3',
15 : 'R2',      16 : 'D1',      17 : 'CC2',     18 : 'D2',      19 : 'D3',
20 : 'FP',      21 : 'E1',      22 : 'CH2',     23 : 'E2',      24 : 'E3',
25 : 'R3',      26 : 'F1',      27 : 'F2',      28 : 'U2',      29 : 'F3',
30 : 'G2J',     31 : 'G1',      32 : 'G2',      33 : 'CC3',     34 : 'G3',
35 : 'R4',      36 : 'CH3',     37 : 'H1',      38 : 'T2',      39 : 'H2',
}

nSqs = len(sqs)


# Important indices

allInds = range(len(sqs))

iGo       = [i for i in allInds if sqs[i]      == 'GO'  ][0]
iJail     = [i for i in allInds if sqs[i]      == 'JAIL'][0]
iG2J      = [i for i in allInds if sqs[i]      == 'G2J' ][0]

iC1       = [i for i in allInds if sqs[i]      == 'C1'  ][0]
iE3       = [i for i in allInds if sqs[i]      == 'E3'  ][0]
iH2       = [i for i in allInds if sqs[i]      == 'H2'  ][0]
iR1       = [i for i in allInds if sqs[i]      == 'R1'  ][0]

iCC_all   = [i for i in allInds if sqs[i][0:2] == 'CC'  ]
iCH_all   = [i for i in allInds if sqs[i][0:2] == 'CH'  ]
iRail_all = [i for i in allInds if sqs[i][0]   == 'R'   ]
iUtil_all = [i for i in allInds if sqs[i][0]   == 'U'   ]



nMoves = 10

currSq = 0

sqCounts = [0 for i in range(nSqs)]

threeDoubles = [False, False, False]

chCard = 0

ccCard = 0

# Started to do a full simulation but eventually got the markove approach to work in the end

# for i in range(nMoves):
#   dieA = rnd.randint(1, diceLen)
#   dieB = rnd.randint(1, diceLen)
#   threeDoubles[i % 3] = dieA == dieB

#   currSq += dieA + dieB

#   if currSq == iG2J:
#     currSq = iJail


#   if currSq in iCC_all:
#     if ccCard == 0:
#       currSq = iGO
#     if ccCard == 1:
#       currSq = iJail
#     ccCard = (ccCard + 1) % 16

# print
# exit()

# Transition matrix
"""
    Community Chest (2/16 cards involve moving):
"""
ccTrans = {}
for i in iCC_all:
  # Transition probabilities from current cc square
  ps = np.zeros(nSqs, float)
  ps[i]     = 14  # Stay on cc square
  ps[iGo]   = 1   # Advance to GO
  ps[iJail] = 1   # Go to JAIL
  ccTrans[i] = ps / 16.0



"""
    Chance (10/16 cards involve moving):
"""
chTrans = {}
for i in iCH_all:
  # Transition probabilities from current CHANCE square
  ps = np.zeros(nSqs, float)

  nextR = [n for n in range(len(iRail_all)) if iRail_all[n] > i]
  nextR = nextR[0] if len(nextR) > 0 else 0
  nextR = iRail_all[nextR]

  nextU = [n for n in range(len(iUtil_all)) if iUtil_all[n] > i]
  nextU = nextU[0] if len(nextU) > 0 else 0
  nextU = iUtil_all[nextU]

  ps[i]     = 6  # Stay on CHANCE square
  ps[iGo]   = 1  # Advance to GO
  ps[iJail] = 1  # Go to JAIL
  ps[iC1]   = 1  # Go to C1
  ps[iE3]   = 1  # Go to E3
  ps[iH2]   = 1  # Go to H2
  ps[iR1]   = 1  # Go to R1
  ps[nextR] += 2  # Go to next R (railway company) (two cards) - might be R1 so add
  ps[nextU] = 1  # Go to next U (utility company)

  ps[(i - 3) % len(sqs)] += 1  # Go back 3 squares, it might be one of the above so add!

  # Might have landed on go to jail?
  ps[iJail] += ps[iG2J]
  ps[iG2J] = 0

  chTrans[i] = ps / 16.0


P = np.zeros((nSqs, nSqs), float)

for i in range(nSqs):
  if i == iG2J:
    P[iG2J, i] = 1
    continue

  # Reachable squares from current square.
  inds = range(i + min(rolls), i + min(rolls) + len(rolls))
  # Wrap round.
  inds = map(lambda x: x % nSqs, inds)
  P[inds, i] = rollProbs

  # Is there a 'special' square in the reachable list?

  # Go to JAIL?
  P[iJail, i] += P[iG2J, i]
  P[iG2J, i] = 0

  # CH
  js = [j for j in inds if j in iCH_all]
  for j in js:
    ps = P[: , i].copy()
    temp = ps[j]
    ps = ps + ps[j] * chTrans[j]
    ps[j] -= temp
    P[:, i] = ps

  # CC?
  js = [j for j in inds if j in iCC_all]
  for j in js:
    ps = P[: , i].copy()
    temp = ps[j]
    ps = ps + ccTrans[j] * ps[j]
    ps[j] -= temp
    P[:, i] = ps


    

# 3 consecutive doubles

# Copy of P, will modify so that we can model going to jail after 3
# consecutive doubles.  I.e Q is used after two applications of P
Q = P.copy()


# 1/(diceLen ** 3) chance of going two jail on turns after the third.


for i in range(nSqs):
  if i == iG2J:
    continue

  ps = Q[:, i].copy()

  newPJail = ps[iJail] + (1.0 / (diceLen ** 3))

  ps[iJail] = 0.0

  ps = ps * 1.0 / (diceLen ** 3) / sum(ps)

  Q[  :  , i] -= ps
  Q[iJail, i]  = newPJail



# State vector

state = np.zeros((nSqs, ), float)
state[0] = 1

for i in range(2):
  state = np.dot(P, state)

for i in range(100):
  state = np.dot(Q, state)



print state.T

topCount = 6
n = [ ]
v = np.zeros((topCount,1), float)

for i in range(topCount):
  n.append( np.argmax(state) )
  v[i] = state[ n[i] ]
  state[n] = 0

np.set_printoptions(precision=6)

print n
print v


print state[iG2J]




######################



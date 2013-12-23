import sys


from abcdCombinatorialUtils import *


def getMajorities(a, b):
  # For each element in a, count the number of b elements that it
  # dominates.
  return map(lambda y: len(filter(lambda x: y>x, b)), a)

def main(*args):
  f = open('majorities-6.txt')
  for line in f:
    line = line.rstrip()
    v = map(int, line.split(','))
    m = [v[:6] , v[6:12], v[12:]]

    if m[1] <= m[0] and m[1] <= m[2]:
      m = [m[1] , m[2], m[0]]

    if m[2] <= m[0] and m[2] <= m[1]:
      m = [m[2] , m[0], m[1]]

    print m



def main1(*args):
  maxPip = 6

  diceFaces = 6

  greaterSetSize = maxPip + diceFaces - 1 # N + k - 1

  transitiveCount = 0

  for c1 in combinations_numeric(greaterSetSize, diceFaces):

    d1 = comb_to_comb_with_reps(c1)

    for c2 in combinations_numeric(greaterSetSize, diceFaces, c1):
      d2 = comb_to_comb_with_reps(c2)

      win1 = win2 = 0
      for diff in [ x-y for x in d1 for y in d2 ]:
        win1 += diff > 0
        win2 += diff < 0

      # Test if one dice has a more than 50% chance of winning
      flip = False
      if win1 > 18:
        a = d1
        b = d2
        flip = True
      elif win2 > 18:
        a = d2
        b = d1
      else:
        continue
      
      for c3 in combinations_numeric(greaterSetSize, diceFaces, c2):
        d3 = comb_to_comb_with_reps(c3)
        
        # have a > b, need b > d3 and d3 > a
        #if b[0] <= d3[-1]: # or d3[0] <= a[-1]:
        #  continue

        winb = 0
        for diff in [ x-y for x in b for y in d3 ]:
          winb += diff > 0

        if winb <= 18:
          continue

        wind3 = 0
        for diff in [ x-y for x in d3 for y in a]:
          wind3 += diff > 0

        if wind3 <= 18:
          continue
        ###################################
        print a, b, d3,
        if flip: 
          print '*'
        else:
          print

        print getMajorities(a,b), getMajorities(b,d3), getMajorities(d3,a), 'm'
        print 

        ###################################
        transitiveCount += 1

  print 'Transitive count %d' % transitiveCount

if __name__ == '__main__':
  sys.exit(main(*sys.argv))





# import networkx as nx
# import itertools
# from abcdPrimeUtils import *

# #import random

# G = nx.DiGraph()
 

# ###################################################################

# def main(*args):

#   maxPip = 7

#   pipSet = range(1, maxPip+1)
#   i = 0
#   allDice = {}
#   gen1 = itertools.combinations_with_replacement(pipSet, 6)
#   for cmb in gen1:
#     allDice[i] = cmb
#     i += 1

# #   # If itertools is old (python < 2.7, combinations with replacement
# #   # is not available.
# #   pipSet = sorted(range(1, maxPip+1) * 6)
# #   i = 0
# #   allDice = {}
# #   cache = {}
# #   gen1 = itertools.combinations(pipSet, 6)
# #   for cmb in gen1:
# #     st = '-'.join(map(str, list(cmb)))
# #     if st in cache: continue
# #     cache[st] = 1
# #     allDice[i] = cmb
# #     i += 1

#   count = i
#   print count , 'combinations found'

# #   i = 0
# #   primes = []
# #   for p in gen_primes():
# #     primes.append(p)
# #     i += 1
# #     if i == count:
# #       break

# #   print 'Got primes', len(primes)


#   for i in xrange(count-1):
#     for j in xrange(i+1, count):
#       diffs = [ x-y for x in allDice[i] for y in allDice[j] ]

#       iWins = len( filter(lambda p: p > 0, diffs) ) 
#       jWins = len( filter(lambda p: p < 0, diffs) ) 

#       # Test if one dice has a more than 50% chance of winning

#       if iWins > 18:
#         G.add_edge(i, j)
#       elif jWins > 18:
#         G.add_edge(j, i)

#   print 'Graph details: '
#   print G.order(), G.number_of_edges(), G.number_of_selfloops()


#   totalCount = 0
#   eCount = 0

#   cache = {}

#   for e in G.edges_iter():
#     pre_t  = G.predecessors(e[0])
#     succ_h = G.successors(e[1])
#     inter = set(pre_t) & set(succ_h)
#     totalCount += len( inter )

# #     for n in inter:
# #       cache[ primes[n] * primes[e[0]] * primes[e[1]] ] = 1


#   print len(cache.keys())
  
#   print totalCount, totalCount / 3
#   print eCount


# if __name__ == '__main__':
#   sys.exit(main(*sys.argv))


# ###################################################################


# #   size = 3

# #   cache = {}
# #   for n in G:
# #     if G.in_degree(n) == 0 or G.out_degree(n) == 0 : continue
# #     for tri in triangles(n):
# #       key = '-'.join(map(str, sorted(tri)))
# #       cache[ key ] = 1
# #   print len(cache.keys())





# # def triangles(node):
# #   ns = G.neighbors(node)
# #   for n in ns:
# #     ms = G.neighbors(n)
# #     for m in ms:
# #       if node in G.neighbors(m):
# #         yield [node, n, m]

# # def buildCycle(currentPath, stepsLeft):
# #   """
# #   currentPath : list of nodes so far, starting at some node or other.
# #   stepsLeft: How many more nodes needed to make the required cycle.
# #   """
# #   ns = G.neighbors(currentPath[-1])
# #   start = currentPath[0]

# #   if ns == []:
# #     # No successors to the current node, can't be in a cycle
# #     return []

# #   if stepsLeft == 0:
# #     # Can we connect with the starting point.
# #     if start in ns:
# #       return currentPath
# #     else:
# #       return []

# #   ps = []
# #   for n in ns:
# #     p = buildCycle(currentPath + [n], stepsLeft - 1)
# #     if p != []:
# #       ps = ps + p 

# #   return ps


# # def compareDice(a, b):
# #   pairs = [(x,y) for x in a for y in b]
# #   aWins = len( filter(lambda x: x[0] > x[1], pairs) ) 
# #   bWins = len( filter(lambda x: x[0] < x[1], pairs) ) 

# #   return aWins - bWins

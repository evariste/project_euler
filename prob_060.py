
# The primes 3, 7, 109, and 673, are quite remarkable. By taking any
# two primes and concatenating them in any order the result will
# always be prime. For example, taking 7 and 109, both 7109 and 1097
# are prime. The sum of these four primes, 792, represents the lowest
# sum for a set of four primes with this property.

# Find the lowest sum for a set of five primes for which any two
# primes concatenate to produce another prime.


# sum ( [13, 5701, 5197, 8389, 6733] )
# Solution : 26033


import sys
from abcdPrimeUtils import *
import networkx as nx

# Need to guess a range to look in
maxVal = 10000

primeList = getNPrimes(maxVal + 10)
# Drop 2 and 5 ...
primeList = [ primeList[1] ] + primeList[3:]

G = nx.Graph()

cacheTests = {}

def testPair(p, q):
  pq = p*q
  if pq in cacheTests:
    return cacheTests[pq]
      
  sP = str(p)
  sQ = str(q)
  if not isPrime_MillerRabin(int(sP + sQ)):
    cacheTests[pq] = False
    return False

  if not isPrime_MillerRabin(int(sQ + sP)):
    cacheTests[pq] = False
    return False

  cacheTests[pq] = True
  return True


def buildGraph():
  for i in xrange(len(primeList) - 1):
    for q in primeList[i+1:]:
      if testPair(primeList[i], q):
        G.add_edge(primeList[i], q)

###################################################################

def main(*args):

  buildGraph()

  cs = list( nx.find_cliques(G) )

  for c in cs:
    if len(c) > 4:
      print c, ' ' , sum(c)


if __name__ == '__main__':
  sys.exit(main(*sys.argv))


###################################################################

# from math import floor, log10
# import numpy
# import itertools

# Attempt 2

def getCliques1(size):
  visited = { p : False for p in primeList }
  countNeeded = (size * (size-1) / 2 ) - (size - 1)

  for p in G:
    if G.degree(p) < (size - 1):
      continue

    for grp in itertools.combinations(G.neighbors(p), size-1):
      count = 0
      for pair in itertools.combinations(grp, 2):
        q = pair[0]
        r = pair[1]
        if G.has_edge(q, r): count += 1
      if count == countNeeded:
        yield [p] + list(grp)
      
def getCliques(size, cands):
  visited = { p : False for p in primeList }
  countNeeded = (size * (size-1) / 2 ) - (size - 1)

  for p in cands:
    if G.degree(p) < (size - 1):
      continue

    for grp in itertools.combinations(G.neighbors(p), size-1):
      count = 0
      for pair in itertools.combinations(grp, 2):
        q = pair[0]
        r = pair[1]
        if G.has_edge(q, r): count += 1
      if count == countNeeded:
        yield [p] + list(grp)



#def mainOld(*args):
#   cands = []
#   for cl in getCliques(3, G.nodes()):
#     cands = cands + cl

#   cands2 = [k for k,v in itertools.groupby(sorted(cands))]
#   cands = []
#   for cl in getCliques(4, cands2):
#     cands = cands + cl

#   cands2 = [k for k,v in itertools.groupby(sorted(cands))]

#   print cands2

#   cands = []
#   for cl in getCliques(5, cands2):
#     print cl
#     cands = cands + cl

#   print cands2

#  for cl in getCliques(5):
#      print cl


###################################################################
# Attempt 1

def test(ps):
  for i in range(len(ps)):
    p = ps[i]
    qs = ps[:i] + ps[i+1:]
    for q in qs:
      if not testPair(p, q):
        return False
  return True




lookup = {}
def getLookup():
  i = 0
  for p in primeList:
    lookup[p] = i
    i += 1

degrees = [0 for p in primeList]

def getDegrees():
  for p in edges.keys():
    degrees[lookup[p]] += len(edges[p])
    for q in edges[p]:
      degrees[lookup[q]] += 1


def pruneEdges(count):
  modifiedCount = 1

  while modifiedCount > 0:
    modifiedCount = 0
    for p in edges.keys():
      if degrees[ lookup[p] ] <= count and edges[p] != []:
        for q in edges[p]:
          degrees[lookup[q]] -= 1
        edges[p] = []
        degrees[ lookup[p] ] = 0
        modifiedCount += 1



#   for k in edges.keys():
#     print '{ ', k, edges[k]
#   exit()

triples = {}

def getTriples():
  for p in edges.keys():
    qs = edges[p]
    for i in xrange(len(qs)):
      for r in qs[i+1:]:
        if qs[i] in edges and r in edges[qs[i]]:
          triples.setdefault(p, []).append( [qs[i], r] )

  ks = triples.keys()
  ks.sort()
  tripleCount = 0
  for p in ks:
    print '  ' , p, triples[p]
    tripleCount += len(triples[p])

  print len(ks), tripleCount


def getCliques(size):
  cliques = {}
  countNeeded = (size * (size-1) / 2 ) - (size - 1)
  print 'count needed : ', countNeeded
  for p in edges.keys():
    qs = edges[p]
    if len(qs) < size-1: continue
    for grp in itertools.combinations(qs, size-1):
      count = 0
      for pair in itertools.combinations(grp, 2):
        if pair[0] in edges and pair[1] in edges[ pair[0] ]:
          count += 1
      if count == countNeeded:
        cliques.setdefault(p, []).append(list(grp))

  ks = cliques.keys()
  ks.sort()
  for p in ks:
    print 'clique ', size, 's', p, cliques[p]
  print

  return cliques

# given candidates
def getCliques2(size, cands):
  cliques = {}
  countNeeded = (size * (size-1) / 2 ) - (size - 1)
  print 'count needed : ', countNeeded
  for p in cands:
    qs = edges[p]
    if len(qs) < size-1: continue
    for grp in itertools.combinations(qs, size-1):
      count = 0
      for pair in itertools.combinations(grp, 2):
        if pair[0] in edges and pair[1] in edges[ pair[0] ]:
          count += 1
      if count == countNeeded:
        cliques.setdefault(p, []).append(list(grp))

  ks = cliques.keys()
  ks.sort()
  for p in ks:
    print 'clique ', size, 's', p, cliques[p]
  print

  return cliques

def collapse(cliques):
  lst = []
  for k in cliques.keys():
    lst.append(k)
#     for kk in cliques[k]:
#       lst = lst + (kk)
#   lst2 = [k for k,v in itertools.groupby(sorted(lst))]
  return lst

quads = {}
def getQuads():
  for p in edges.keys():
    qs = edges[p]
    if len(qs) < 3: continue
    for grp in itertools.combinations(qs, 3):
      count = 0
      for pair in itertools.combinations(grp, 2):
        if pair[0] in edges and pair[1] in edges[pair[0]]:
          count += 1
      if count == 3: # (1/2) * (4*3) - 3 
        quads.setdefault(p, []).append(list(grp))
    
  ks = quads.keys()
  ks.sort()
  for p in ks:
    print ' c4 ', p, quads[p]

  print len(ks)


def printEdges():
  ks = edges.keys()
  ks.sort()
  for p in ks:
    print 'e ', p, degrees[ lookup[p] ], ' : ', edges[p]
  print

def mainOld(*args):

#   li = [3, 7, 109, 673]
#   val = sum(li)
#   size = 4

#   maxVal = 10000
#   ps = getNPrimes(maxVal)

  # Must have distinct primes as p concatenated with p is a composite.
  # cannot have 2 in the list of primes
#   ps = [ ps[1] ] + ps[3:]
#   print ps[:10]

#   # Graph structure

  getLookup()

  # The primes are at the nodes, an edge connects each pair of primes
  # p , q for which the concatenations pq qp are both prime.
  buildGraph()


  getDegrees()

  # Remove any node which has degree one, i.e. which
  # cannot form a triangle.
  #pruneEdges(1)
  getTriples()

  #pruneEdges(2)
  #printEdges()

  # getQuads()
  triples = getCliques(3)
  
  cands = collapse(triples)

  quads2 = getCliques2(4, cands)

  cands = collapse(quads2)
  quints = getCliques2(5, cands)

  exit()

  size = 4
  start = 2 + size % 2 
  print 'Testing from ', start

  val = start
  while val < maxVal:
    for part in f_distinct_v2(val, 0, size):
      if test(part):
        print '----------',  val, part
        exit()
    val += 2



#############################################


# ps = [3, 7, 109, 673]

# for p in ps:
#   qs = filter(lambda x: x != p, ps)
#   for q in qs:
#     m = int(1 + floor(log10(q)))
#     concat = (10**m)*p + q
#     print p, q, ' -> ', concat
#     if not isPrime_MillerRabin(concat):
#         print  ' not  prime'
 
#     m = int(1 + floor(log10(p)))
#     concat = (10**m)*q + p
#     print q, p, ' -> ', concat
#     if not isPrime_MillerRabin(concat):
#         print  ' not  prime'
 
    




# def testPair(p, q):

#   if (p,q) in cacheTests:
#     return cacheTests[ (p,q) ]
      
#   sP = str(p)
#   sQ = str(q)
#   if not isPrime_MillerRabin(int(sP + sQ)):
#     cacheTests[ (p,q) ] = False
#     return False

#   if not isPrime_MillerRabin(int(sQ + sP)):
#     cacheTests[ (p,q) ] = False
#     return False

#   cacheTests[ (p,q) ] = True
#   return True




# def f(n, ps, size, distinct):
#   """
#   Pre: assumes list ps is in ascending order.
#   """
#   if size == 1:
#     if n in ps :
#       yield [n]
#   elif (len(ps) == 0):
#     return
#   else:
#     i = 0
#     while ps[i] < n:
#       if distinct:
#         rest = ps[i+1:]
#       else:
#         rest = ps[i]

#       for part in f(n-ps[i] ,  rest, size-1, distinct):
#         yield [ ps[i] ] + part
#       i += 1



# def f_distinct(n, ps, size):
#   """
#   Pre: assumes list ps is in ascending order.
#   """
#   if size == 1:
#     if n in ps :
#       yield [n]
#   elif (len(ps) == 0):
#     return
#   else:
#     i = 0
#     while ps[i] < n:
#       for part in f_distinct(n-ps[i] ,  ps[i+1:], size-1):
#         yield [ ps[i] ] + part
#       i += 1




# def f_distinct_v2(n, ind, size):
#   """
#   Pre: assumes list ps is in ascending order.
#   """
# #   if primeList[ind] > n / size:
# #     # If we have reached a prime in the list that exceeds n/2 then all
# #     # following primes will be too big.
# #     return    
# #   el
#   if size == 1:
#     i = ind
#     while primeList[i] < n:
#       i += 1
#     if n == primeList[i]:
#       yield [n]
#   else:
#     i = ind
#     while primeList[i] < (n / size):
#       for part in f_distinct_v2(n - primeList[i] ,  i+1, size-1):
#         yield [ primeList[i] ] + part
#       i += 1


# def f_distinct_v3(n, size):
#   """
#   """
#   i = 0
#   # smallest possible sum taking from left
#   temp = sum(primeList[:(size - 1)])
#   while n - primeList[i] > temp:
#     i += 1

#   print n, size, primeList[i]
#   print primeList[:i+1]
  
#   partition = [0 for x in range(size+1)]
#   inds = [0 for x in range(size)]

# #   for j in range(size):
# #     part
# #   partition[0] = primeList[i]
# #   partition[1] = n - primeList[i]

# #   inds[0] = i



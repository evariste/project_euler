"""



NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any
cell in the left column and finishing in any cell in the right column,
and only moving up, down, and right, is indicated in red and bold; the
sum is equal to 994.

	
131	673	*234	*103	*18
*201	*96	*342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331
	

Find the minimal path sum, in matrix.txt (right click and 'Save
Link/Target As...'), a 31K text file containing a 80 by 80 matrix,
from the left column to the right column.


"""

import numpy, networkx as nx

filename = 'prob_081.txt'

f = open(filename)

lines = f.readlines()

vals = map(int, lines[0][:-1].split(','))
sz = len(vals)

vals = numpy.zeros(sz*sz).reshape(sz, sz)
i = 0

for line in lines:
  # Chop
  line = line[:-1]
  vals[i] = map(int, line.split(','))
  i += 1

ids = numpy.array( [i + sz * j for i in range(sz) for j in range(sz)] )

ids = ids.reshape(sz, sz)

G = nx.DiGraph()

for i in range(sz):
  for j in range(sz):

    cost = vals[i][j]
    idA = ids[i][j]

    if i > 0:
      idB = ids[i - 1][j]
      G.add_edge(idA, idB, weight=cost)
    if i < sz - 1:
      idB = ids[i + 1][j]
      G.add_edge(idA, idB, weight=cost)
    if j < sz - 1:
      idB = ids[i][j + 1]
      G.add_edge(idA, idB, weight=cost)



starts = ids[: , 0]

minVal = vals.max() * vals.size
minA   = 0
minB   = 0
minI   = 0

for a in starts:

  sp = nx.shortest_path_length(G, a, None, weight='weight')

  # Only want values on right of array
  lastColVals = [ sp[i] for i in ids[:, -1] ]
  # And only the smallest in the last column
  i = lastColVals.index(min(lastColVals))

  if lastColVals[i] < minVal:
    minVal = lastColVals[i]
    minA = a
    minB = ids[i, -1]
    minI = i
    print minA, minB, minVal

# Add final value
minVal += vals[minI, -1]
print minVal



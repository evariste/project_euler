"""

In the 5 by 5 matrix below, the minimal path sum from the top left to
the bottom right, by only moving to the right and down, is indicated
in bold red and is equal to 2427.

	
*131	 673	 234	 103	 18
*201	*96	*342	 965	 150
 630	 803	*746	*422	 111
 537	 699	 497	*121	 956
 805	 732	 524	*37	*331
	

Find the minimal path sum, in matrix.txt (right click and 'Save
Link/Target As...'), a 31K text file containing a 80 by 80 matrix,
from the top left to the bottom right by only moving right and down.

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

    if i < sz - 1:
      idB = ids[i + 1][j]
      G.add_edge(idA, idB, weight=cost)
    if j < sz - 1:
      idB = ids[i][j + 1]
      G.add_edge(idA, idB, weight=cost)


firstNode = ids[0][0]
lastNode  = ids[sz-1][sz-1]
sp = nx.shortest_path(G, firstNode, lastNode, weight='weight')

print sp
print len(sp)


spl = nx.shortest_path_length(G, firstNode, lastNode, weight='weight')
# Add last value in grid
spl += vals[-1][-1]
print ' : ' , spl


"""
# Long way! Before realising there was a function to give the length directly :
totalW = 0

for i in range(len(sp)-1):
  idA = sp[i]
  idB = sp[i+1]
  w = G.edge[idA][idB]['weight']
  totalW += w
  print idA, idB, w


# Add last value in grid
totalW += vals[-1][-1]
print totalW
"""



"""
# From Thread for problem , quite interesting

def minimal_path(mat):
    rows = len(mat)
    cols = len(mat[0])
    for c in xrange(1, cols):
        mat[0][c] += mat[0][c-1]
    for r in xrange(1, rows):
        mat[r][0] += mat[r-1][0]
    for r in xrange(1, rows):
        for c in xrange(1, cols):
            mat[r][c] += min(mat[r-1][c], mat[r][c-1])
    return mat[rows-1][cols-1]

def read_matrix(filename):
    with file(filename, "r") as f:
        return [[int(x) for x in line.split(',')] for line in f.readlines()]

if __name__ == "__main__":
    print minimal_path(read_matrix("matrix.txt"))

"""


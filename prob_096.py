'''
Su Doku (Japanese meaning number place) is the name given to a popular puzzle
concept. Its origin is unclear, but credit must be attributed to Leonhard Euler
who invented a similar, and much more difficult, puzzle idea called Latin
Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or
zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains
each of the digits 1 to 9. Below is an example of a typical starting puzzle grid
and its solution grid.

003|020|600
900|305|001
001|806|400
-----------
008|102|900
700|000|008
006|708|200
-----------
002|609|500
800|203|009
005|010|300


483|921|657
967|345|821
251|876|493
-----------
548|132|976
729|564|138
136|798|245
-----------
372|689|514
814|253|769
695|417|382


A well constructed Su Doku puzzle has a unique solution and can be solved by
logic, although it may be necessary to employ "guess and test" methods in order
to eliminate options (there is much contested opinion over this). The complexity
of the search determines the difficulty of the puzzle; the example above is
considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'),
contains fifty different Su Doku puzzles ranging in difficulty, but all with
unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the
top left corner of each solution grid; for example, 483 is the 3-digit number
found in the top left corner of the solution grid above.

Ans: 24702

'''

import numpy as np
import itertools
import sys
import time

########################################
# Global variable to help out.

# Indices for cells, there are 9 3x3 cells in the grid. Store the i,j locations
# for each cell in a pair tuple of numpy arrays to use in indexing later.
cellInds = []

########################################
"""
Set up the global variable for cell indices.
"""
def setCellInds():
  ii = []
  jj = []
  for i,j in itertools.product([0,1,2], [0,1,2]):
      ii = ii + [i]
      jj = jj + [j]
  
  
  ii = np.asarray(ii)
  jj = np.asarray(jj)
  
  # Use global keyword so that we can write to the following variable.
  global cellInds
  
  for a,b in itertools.product([0,3,6], [0,3,6]):    
      cellInds = cellInds + [ (ii + a, jj + b) ]

########################################

""" 
Read the grids in the given text file into a numpy array 
"""
def getGrids():
    f = file('prob_096_sudoku.txt')
    
    allGrids = np.zeros( (9,9,50), dtype=np.int8 )
    
    lines = list(f)
    # Pesky new lines
    lines = map(lambda x: x.replace('\n', ''), lines)
    f.close()        
    
    i = 0
    while i < len(lines):
        currLine = lines[i]
        if currLine[:4] == 'Grid':
            # Format is, e.g. 'Grid 09'
            # grid index
            j = int( currLine[-3:] ) - 1
            # Next 9 lines are the grid entries.
            currGrid = lines[i+1:i+10]
            # Concatenate
            currGrid = reduce( lambda x,y: x+y , currGrid)
            # Make a numeric array
            currGrid = map(lambda x: int (x), currGrid)
            currGrid = np.asarray(currGrid, dtype=np.int16)
            currGrid = np.reshape( currGrid, (9,9))
    
            allGrids[:,:,j] = currGrid.copy()
            i = i + 10
    return allGrids
            

########################################
"""
See if a given configuration is ok. The grid can contain zero entries which are
ignored. Only the postive entries are checked.
"""
def checkGrid(g):
    # check 3x3 cells
    for i in range(9):
        temp = g[cellInds[i]]
        # only check positive entries
        temp = temp[temp > 0]
        if not len(temp) == len(set(temp)):
          return False

    # Check rows and columns
    for i in range(9):
        temp = g[i,:]
        temp = temp[temp > 0]
        if not len(temp) == len(set(temp)):
          return False
        
        temp = g[:,i]
        temp = temp[temp > 0]
        if not len(temp) == len(set(temp)):
          return False
        
    return True

########################################
'''
Pretty printing.
'''
def printGrid(g):
  r,c = g.shape
  print ''
  for i in range(r):
    if i == 3 or i == 6:
      print '-'*11
    rowStr =  ''.join(map(str, g[i,:]))
    print rowStr[0:3] + '|' + rowStr[3:6] + '|' + rowStr[6:]
  print ''

########################################
'''
Check if putting the value val into the grid g at cell location ij (a pair) is
okay under sudoku rules. Returns True/False.
'''
def checkGrid2(g, ij, val):
  valStore = g[ij]
  g[ij] = val
  result = checkGrid(g)
  g[ij] = valStore
  return result

########################################
'''
What values could go into the grid g at location i,j?
'''
def getHypotheses(g, i,j):
  return filter(lambda x: checkGrid2(g, (i,j), x), range(1,10))
  
########################################
'''
Identify any cells for which only one number can fit. Set these and iterate
until grid is no longer modified.
'''
def setSingletons(grid):

  g = grid.copy()
  modified = True
    
  while modified:
    modified = False
    
    # cells where there are no solutions
    ii,jj = np.where(g==0)
    
    for k in range(len(ii)):
      # How many possible numbers can fit it?
      hypotheses = getHypotheses(g, ii[k],jj[k])
                
      if len(hypotheses) == 1:
        g[ii[k], jj[k]] = hypotheses[0]
        modified = True
      
            
  return g
  

########################################
'''
The main function. It is called for cells with as few hypotheses as possible to
try to limit the combinations searched. For a given cell, loop over all possible
values that could be assigned to it (hypotheses) and assign them to the cell.
With the resulting grid, call recursively.

Still a bit slow for some grids but seems to work.
'''
def solve(grid):
  if np.all(grid > 0):
    # All slots have been filled in nothing to test.
    return grid

  g = grid.copy()
  # Fill in any cells that only have one option.
  g = setSingletons(g)
  shp = g.shape

  
  # Find the a zero entry in the grid, i.e. an unset cell, with as few options
  # as possible

  # Counts for how many hypotheses each cell has.
  hypCounts = 10*np.ones(shp)

  # cells where there are no solutions, cells that do have entries will have the
  # artifically high value of 10 associated with them so will be ignored.
  ii,jj = np.where(g==0)
  
  for k in range(len(ii)):
    # How many possible numbers could be assigned to the current cell?
    hypotheses = getHypotheses(g, ii[k],jj[k])
    hypCounts[ii[k], jj[k]] = len(hypotheses)
    
  if np.any(hypCounts == 0):
    # Stopping condition.
    # Under the current configuration, there is a cell somewhere that is
    # impossible to fill.
    return None

  # Find a cell with a low number of hypotheses.
  i,j = np.unravel_index(np.argmin(hypCounts) , shp )

      
  for val in getHypotheses(g, i, j) :
    g[i,j] = val
    g2 = solve(g)
    if not g2 == None:
      return g2

  return None
  

########################################

def main(*args):
  
  setCellInds()
  
  allGrids = getGrids()
  
  nGrids = allGrids.shape[2]

  t1 = time.clock()
  
  sum = 0
  
  for n in range(nGrids):
    print n
    currGrid = allGrids[:,:,n]
    solutionGrid = solve(currGrid)
    topLeft = np.dot(solutionGrid[0,0:3], [100, 10, 1])
    print ' ', topLeft
    sum = sum + topLeft
    
  print sum

  t2 = time.clock()
  print round(t2-t1, 3)
    
  
  
########################################


if __name__ == '__main__':
  sys.exit(main(*sys.argv))



'''Three distinct points are plotted at random on a Cartesian plane, for
which -1000 <= x, y <= 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas
triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K
text file containing the co-ordinates of one thousand "random"
triangles, find the number of triangles for which the interior
contains the origin.

NOTE: The first two examples in the file represent the triangles in
the example given above.

ANS 228

'''

import numpy as np


def getData():
  f = file('prob_102_triangles.txt')

  lines = list(f)
  # Pesky new lines
  lines = map(lambda x: x.replace('\n', ''), lines)
  lines = map(lambda x: x.split(','), lines)
  lines = map(lambda x: map(lambda y: int(y), x), lines )
  f.close()

  return lines



def signOfTheCross(x1, y1, x2, y2, x3, y3):
  '''Sign of the cross product of two vectors in the plane.  vectors are u
  and v where u is (x2,y2)-(x1,y1) and v is (x3,y3) - (x1,y1).

  The sign will correspond to whether the vector u needs to be turned
  clockwise or anti-clockwise to face in the direction of
  v. Alternatively, whether the point (x3,y3) is on the left or on the
  right as we move on a line in the direction from point (x1,y1) to
  point (x2,y2).

  '''

  ux = x2 - x1
  uy = y2 - y1
  vx = x3 - x1
  vy = y3 - y1
  return  np.sign( ux * vy - uy * vx )



lines = getData()

count = 0

for currLine in lines:
  x1,y1,x2,y2,x3,y3 = currLine

  sa = signOfTheCross(x1,y1,x2,y2,0,0)
  sb = signOfTheCross(x2,y2,x3,y3,0,0)
  sc = signOfTheCross(x3,y3,x1,y1,0,0)

  # Travelling around the triangle along each edge in a cyclic sense,
  # we need to the origin to be on the same side of each edge.
  if sa==sb and sb==sc:
    count = count + 1

print count





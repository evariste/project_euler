"""The points P (x1, y1) and Q (x2, y2) are plotted at integer
co-ordinates and are joined to the origin, O(0,0), to form triangle OPQ.

There are exactly fourteen triangles containing a right angle that can
be formed when each co-ordinate lies between 0 and 2 inclusive; that
is, 0 <= x1, y1, x2, y2 <= 2.

Given that 0 <= x1, y1, x2, y2 <= 50, how many right triangles can be formed?

Ans: 14234


The triangles where the right angle is on one of the coordinate axes
are treated separately.

Each coordinate is chosen from 1,...,N. If the right angle is at the
origin there are N^2 choices for the other two corners. If the right
angle is on the x-axis, there are N choices for the positon of the N
choices for the vertex above it, i.e. N^2 choices altogether.
Similarly there are N^2 choices where the right angle is on the
y-axis.

Now look at the triangles where the right angle is at a point (a,b)
where a>0 and b>0. We can move along the line from the origin to (a,b)
and, to form the right angle, we can turn 'left' or 'right'. The
vector (a,b)^T joins the origin to the point. Any vector parallel to
(b,-a)^T represents a right turn and any vector parallel to (-b,a)^T
is a left turn.

If we take a step of (-b,a)^T (or in the opposite direction, we will
hit grid points and just need to check that we stay inside the square
between (0,0) and (50,50). In fact, we can hit more grid points if
take a step of (-b',a')^T where b' = b / gcd(a,b) and a' = a / gcd(a,b).


"""

import itertools
import fractions as fr

N = 50

r = range(1,N+1)

total = 0
for ab in itertools.product(r,r):

  a,b = ab[0], ab[1]

  g = fr.gcd(a,b)
  aStep = a / g
  bStep = b / g

  # Points along a line turning right
  a2,b2 = a,b
  count = -1
  while a2 >= 0 and b2 >= 0 and a2 <= N and b2 <= N:
    count = count + 1
    a2 = a2 + bStep
    b2 = b2 - aStep
      
  total = total + count

  # Points along a line turning left
  a2,b2 = a,b
  count = -1
  while a2 >= 0 and b2 >= 0 and a2 <= N and b2 <= N:
    count = count + 1
    a2 = a2 - bStep
    b2 = b2 + aStep

  total = total + count



print 3*N*N
print total
print 3*N*N + total


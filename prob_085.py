
"""

By counting carefully it can be seen that a rectangular grid measuring
2 by 3 contains eighteen rectangles:

1x1 6  2 x 3
1x2 4  2 x 2
1x3 2  2 x 1
2x1 3  1 x 3
2x2 2  1 x 2
2x3 1  1 x 1

Although there exists no rectangular grid that contains exactly two
million rectangles, find the area of the grid with the nearest
solution.

Answer: 2772

My derivation here, easier one below.

Large rect size A x B
Sub rect with size m x n

contained in 
A - m + 1  rows
B - n + 1  cols

Want sum over all possible values of m, n from 1,1 to A,B

sum_n=1^B  sum_m=1^A  (A-m+1) (B-n+1)

sum_n=1^B  sum_m=1^A  (A+1) (B-n+1) - m (B-n+1)

sum_n=1^B  [  A (A+1) (B-n+1) - sum_m=1^A m (B-n+1) ]

sum_n=1^B  [ A (A+1) (B-n+1) - (B-n+1) sum_m=1^A m  ]

sum_n=1^B  [ A (A+1) (B-n+1) - (B-n+1) A (A+1)/2  ]

sum_n=1^B  (B-n+1) [ A (A+1)/2  ]

A (A+1)/2   sum_n=1^B  (B+1) - n 

A (A+1)/2   [ B (B+1) - sum_n=1^B n ] 

A (A+1)/2   [ B (B+1) / 2 ] 

A(A+1) B(B+1) / 4

i.e we seek integers which solve

2000000 = A(A+1) B(B+1) / 4
or
8000000 = A(A+1) B(B+1)

as closely as possible



For fixed B, we get a quadratic in A

A^2 + A - c = 0

where c = 8000000/ [ B(B+1) ]

Solving

A = [ -1 \pm sqrt( 1 + 4c ) ] / 2

If A has one or more real roots then the integers on either side can be checked for how well they solve (*)


Alternatively: From Thread

"It is just a simple combination question Let the width be a units and
the length be b units, the number of rectangles is

   (a+1) C 2 * (b+1) C 2 

where C is the combinatics (sic) function."

Of course, each rectangle is defined by its corners, the
'x-coordinates' of the corners are chosen as distinct pairs from 0, 1,
... , a+1 , etc.

"""

import math

rootsFound = 1



targetVal = 8000000.0

B = 1

c = targetVal / B / (B + 1)
fA = 0.5 * (math.sqrt(1 + 4 * c) - 1)

minDiff = 10000000
minAB = [1,1]

# As B increases, A goes down
while fA > 1.0:
  A = int(math.floor(fA))

  val = A * (A+1) * B * (B+1) / 4
  diff = abs(val - targetVal/4)
  if diff < minDiff:
    print A, B, val, diff
    minDiff = diff
    minAB = [A, B]
  
  A += 1

  val = A * (A+1) * B * (B+1) / 4
  diff = abs(val - targetVal/4)
  if diff < minDiff:
    print A, B, val, diff
    minDiff = diff
    minAB = [A, B]

  B += 1
  c = targetVal / B / (B + 1)
  fA = 0.5 * (math.sqrt(1 + 4 * c) - 1)

print 'AB = ' , minAB[0] * minAB[1]



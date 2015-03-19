

"""It is easily proved that no equilateral triangle exists with integral
length sides and integral area. However, the almost equilateral
triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for
which two sides are equal and the third differs by no more than one
unit.

Find the sum of the perimeters of all almost equilateral triangles
with integral side lengths and area and whose perimeters do not exceed
one billion (1,000,000,000).

Ans: 518408346

--------------------------

The triangles' sides are (n,n,n+1) or (n,n,n-1). Geometry can be
used to show that the area will be equal to

(n+1) sqrt( 3n^2 - 2n - 1) / 4   

or 

(n+1) sqrt( 3n^2 + 2n - 1) / 4 

So we need 3n^2 - 2n - 1 or 3n^2 + 2n - 1 to be a perfect square.

Focus on the first for now and write

3n^2 - 2n - 1 = k^2

This can be re-arranged to x^2 - 3 y^2 = 1 which is Pell's equation,
ie N = 3 in the general form x^2 - N y^2 = 1.

In this case we have

n = (2x + 1) / 3 and k = 2y

( for the other form with (n,n,n-1) we have n = (2x-1) / 3 and k = 2y)

Given a solution of (x,y) of x^2 - 3 y^2 = 1, we can find n and we can
find the corresponding area which is (n+1)y/2 ( or (n-1)y/2 ) and test
if they are integers.

The solutions of Pell's equation can be found by starting off with the
solution (x0, y0) = (2,1) and iteratively generating the rest, xk,yk
for k = 1,2, ... This can be done with the inductive formula

x_k+1 = x_0 x_k + N y_0 y_k
y_k+1 = y_0 x_k +   x_0 y_k

which in our case becomes

x_k+1 = 2 x_k + 3 y_k
y_k+1 =   x_k + 2 y_k


Checking the modulus of x and y mod 3 the solutions of Pell's equation
have xk = 2,1,2,1,... mod 3.

These alternately lead to solutions of the form (n,n,n+1) and (n,n,n-1).

"""



xk,yk = 2L,1L

perim = 0L
sumPerim = 0L
maxPerim = 1000000000

while perim < maxPerim:
    x = 2 * xk + 3 * yk
    y = xk + 2 * yk
    
    if x % 3 == 2:
        # (n,n,n-1) form
        n = (2*x-1)/3
        perim = long(3*n-1)
        area = (x-2)*y/3
    else: # if x % 3 == 1:
        # (n,n,n+1) form
        n = (2*x+1)/3
        perim = long(3*n+1)
        area = (x+2)*y/3

    if perim <= maxPerim:
        sumPerim = sumPerim + perim
        print (x,y), n, perim, area
    xk,yk = x,y


print sumPerim

# <codecell>



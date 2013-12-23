

"""
A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by
3, and a fly, F, sits in the opposite corner. By travelling on the
surfaces of the room the shortest "straight line" distance from S to F
is 10 and the path is shown on the diagram.

However, there are up to three "shortest" path candidates for any
given cuboid and the shortest route doesn't always have integer
length.

By considering all cuboid rooms with integer dimensions, up to a
maximum size of M by M by M, there are exactly 2060 cuboids for which
the shortest route has integer length when M=100, and this is the
least value of M for which the number of solutions first exceeds two
thousand; the number of solutions is 1975 when M=99.

Find the least value of M such that the number of solutions first
exceeds one million.



Approach

Find pythagorean triples (PTs) a, b, c

We have a^2 + b^2 = c^2

The dimensions of a cube d1 d2 d3 and the shortest path (SP) along the
surfaces can be related to a PT by setting

d1+d2 to be one of a or b
d3 to be the other (of a or b)

The shortest path will then be of length c

This is because the shortest path can be shown as the hypotenuse of a
right angled triangle with edge lengths equal to d1+d2 and d3. This
can be done by flattening out the two faces that the shortest path
runs along.

The three contenders for the shortest path are the hypotenuses of
right triangles with edge lengths

d1+d2 and d3
d1+d3 and d2
d2+d3 and d1

giving squared contenders for the shortest path of

(d1+d2)^2 + d3^2  A 
(d1+d3)^2 + d2^2  B
(d2+d3)^2 + d1^2  C


if d1 <= d2 <= d3

B - A = d1 d3 - d1 d2 = d1 (d3 - d2) >= 0
C - B = d2 d3 - d1 d3 = d3 (d2 - d1) >= 0

So the shortest path is obtained by setting d3 as b in the ordered PT
a, b, c



m^2 - n^2 - 2mn 
= (m-n)^2 - 2 n^2
= (m - n - n s2 ) (m - n + n s2)  where s2 = sqrt(2)
= (m - n (1 + s2)) (m + n (s2 - 1)) 
> 0  if m > n(1 + s2) 

ie. if


"""


from math import sqrt, floor


# Function not actually used, but helped during development.
def shortestDiag(dim):
  a = dim[0]
  b = dim[1]
  c = dim[2]
  minL2 = (a+b)**2 + c**2

  L2 = a**2 + (b+c)**2
  if minL2 > L2:
    minL2 = L2

  L2 = (a+c)**2 + b**2
  if minL2 > L2:
    minL2 = L2


  return sqrt(minL2)




# Basic traversal of the tree of primitive pythagorean triples.
#
# http://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples
#
# Within each call, check all the multiples of the current primitive.

def traverseTree(a, b, c, maxEdgeLen):
  if a > 2*maxEdgeLen or b > 2*maxEdgeLen:
    return

  minAB = min(a, b)
  maxAB = max(a, b)

  # Initialise the multiples.
  ka, kb = minAB, maxAB
  dim = [0,0,0]

  # Break up the smaller length
  while kb <= maxEdgeLen:
    # print ka, kb, '- '
    # Following should give us a list whose elements are sorted
    # triples of potential cube dimensions.
#     dims = [ [i , ka-i , kb] for i in range(1, 1 + ka/2)]
    traverseTree.count += ka/2
#     for dim in dims:

#       # found a new one
#       traverseTree.count += 1
#       # traverseTree.memo.append( dim )
#       # print dim

    ka += minAB
    kb += maxAB


  # Break up the larger length
  ka, kb, kc = minAB, maxAB, c

  while ka <= maxEdgeLen and kb <= 2*maxEdgeLen:
    # print ka, kb, '+ '
    
    dims = [ [i , kb-i , ka] for i in range(1, 1 + kb/2) ]
    
    for dim in dims:
      # Have we got a legal set of dimensions?
#       if any(map(lambda x: x > maxEdgeLen, dim)):
#         continue
      # If either of the broken lengths exceeds the unbroken one, ka,
      # then the hypotenuse of the PT will not be the shortest
      # length. In that case the shortest length is obtained by a
      # right triangle with sides that are either [i+ka, kb-i] or
      # [kb-i+ka, i] in other words, we no longer have the pythagorean
      # triple as the basis for our shortest length.
      if (any(map(lambda x: x > ka, dim))):
        continue


      # found a new one
      traverseTree.count += 1
#       traverseTree.memo.append( dim )
      # print dim


    ka += minAB
    kb += maxAB
    
  # The current primitive Pythagorean triple (a,b,c) is a node which
  # has 3 child nodes. Call recursively from each of them.
  traverseTree(a - 2*b + 2*c, 2*a - b + 2*c, 2*a - 2*b + 3*c, maxEdgeLen)
  traverseTree(a + 2*b + 2*c, 2*a + b + 2*c, 2*a + 2*b + 3*c, maxEdgeLen)
  traverseTree(2*b + 2*c - a, b + 2*c - 2*a, 2*b + 3*c - 2*a, maxEdgeLen)


####################################################

# The main bit


# Top level node in the tree.
a, b, c = 3, 4, 5

# Storage for the valid dimensions of cubes that have been found so
# far.
traverseTree.count = 0


# By trial and error!
i = 1818
traverseTree(a,b,c,i)
print i, traverseTree.count
print

# From forum
# sum = 0 
# loop 
# for j from 1 to M 
# loop for i from 2 to 2*j 
# if path_is_integral (i j) then 
# sum = sum + (combinations i j) where 
# combinations (i j) is the number of ways to choose x and y satisfying 1 <= x <= y <= j and x + y = i


exit()


traverseTree(a,b,c, 5)

# Copying a list correctly in python (avoid just getting a reference).
l1 = list(traverseTree.memo)

print l1

#a, b, c = 3, 4, 5
#traverseTree.memo = []

traverseTree(a,b,c, 20)

l2 = list(traverseTree.memo)

print l2


# ###################################
# def traverseTree(a, b, c, maxEdgeLen):
#   if a > 2*maxEdgeLen or b > 2*maxEdgeLen:
#     return

#   #print len(traverseTree.memo)

#   # Initialise the multiples.
#   ka, kb = min(a, b), max(a,b)
#   dim = [0,0,0]

#   # Break up the smaller length
#   while kb <= maxEdgeLen:
#     # print ka, kb, '- '
#     # Following should give us a list whose elements are sorted
#     # triples of potential cube dimensions.
#     dims = [ [i , ka-i , kb] for i in range(1, 1 + ka/2)]

#     for dim in dims:
# #       if (dim) in traverseTree.memo:
# #         # print ' found ' , dim
# #         continue

#       # found a new one
#       traverseTree.memo.append( dim )
#       # print dim

#     ka += min(a,b)
#     kb += max(a,b)


#   # Break up the larger length
#   ka, kb, kc = min(a,b), max(a,b), c

#   while ka <= maxEdgeLen and kb <= 2*maxEdgeLen:
#     # print ka, kb, '+ '
    
#     dims = [ [i , kb-i , ka] for i in range(1, 1 + kb/2) ]
    
#     for dim in dims:
#       # Have we got a legal set of dimensions?
#       if any(map(lambda x: x > maxEdgeLen, dim)):
#         continue
#       # If either of the broken lengths exceeds the unbroken one, ka,
#       # then the hypotenuse of the PT will not be the shortest
#       # length. In that case the shortest length is obtained by a
#       # right triangle with sides that are either [i+ka, kb-i] or
#       # [kb-i+ka, i] in other words, we no longer have the pythagorean
#       # triple as the basis for our shortest length.
#       if (any(map(lambda x: x > ka, dim))):
#         continue

#       # The dimensions may need sorting when breaking up kb
#       dim.sort()

# #       # Check if we've seen it before.
# #       if (dim) in traverseTree.memo:
# #         # print ' found ' , dim
# #         continue

#       # found a new one
#       traverseTree.memo.append( dim )
#       # print dim


#     ka += min(a,b)
#     kb += max(a,b)
    
#   # The current primitive Pythagorean triple (a,b,c) is a node which
#   # has 3 child nodes. Call recursively from each of them.
#   traverseTree(a - 2*b + 2*c, 2*a - b + 2*c, 2*a - 2*b + 3*c, maxEdgeLen)
#   traverseTree(a + 2*b + 2*c, 2*a + b + 2*c, 2*a + 2*b + 3*c, maxEdgeLen)
#   traverseTree(2*b + 2*c - a, b + 2*c - 2*a, 2*b + 3*c - 2*a, maxEdgeLen)


# ####################################################

# # The main bit


# # Top level node in the tree.
# a, b, c = 3, 4, 5

# # Storage for the valid dimensions of cubes that have been found so
# # far.
# traverseTree.memo = []


# i = 100
# traverseTree(a,b,c,i)
# print i, len(traverseTree.memo)
# print

# exit()


# traverseTree(a,b,c, 5)

# # Copying a list correctly in python (avoid just getting a reference).
# l1 = list(traverseTree.memo)

# print l1

# #a, b, c = 3, 4, 5
# #traverseTree.memo = []

# traverseTree(a,b,c, 20)

# l2 = list(traverseTree.memo)

# print l2



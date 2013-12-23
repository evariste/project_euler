
# It turns out that 12 cm is the smallest length of wire that can be
# bent to form an integer sided right angle triangle in exactly one
# way, but there are many more examples.

# 12 cm: (3,4,5)
# 24 cm: (6,8,10)
# 30 cm: (5,12,13)
# 36 cm: (9,12,15)
# 40 cm: (8,15,17)
# 48 cm: (12,16,20)

# In contrast, some lengths of wire, like 20 cm, cannot be bent to
# form an integer sided right angle triangle, and other lengths allow
# more than one solution to be found; 

# For example, using 120 cm it is possible to form exactly three
# different integer sided right angle triangles.

# 120 cm: (30,40,50), (20,48,52), (24,45,51)

# Given that L is the length of the wire, for how many values of L <=
# 1,500,000 can exactly one integer sided right angle triangle be
# formed?


maxPerimeter = 1500000

# Traverses the tree of primitive pythagorean triples.
#
# http://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples
#
# Until the perimeter length is exceeded.

def traverseTree(a, b, c):
  if a+b+c > maxPerimeter:
    return

  # Non-primitive multiples of the current primitive must also be
  # counted. Multiples below the maximimum lengths are all allowed.
  perim = a+b+c
  for p in range(perim, maxPerimeter, perim):

    if traverseTree.count.has_key(p):
      traverseTree.count[p] = traverseTree.count[p] + 1
    else:
      traverseTree.count[p] = 1

  # print a , b, c , traverseTree.count

  # The current node (a,b,c) has 3 child nodes. Call recursively from each of them.
  traverseTree(a - 2*b + 2*c, 2*a - b + 2*c, 2*a - 2*b + 3*c)
  traverseTree(a + 2*b + 2*c, 2*a + b + 2*c, 2*a + 2*b + 3*c)
  traverseTree(2*b + 2*c - a, b + 2*c - 2*a, 2*b + 3*c - 2*a)

  

# Top level node in the tree.
a, b, c = 3, 4, 5

traverseTree.count = {}

traverseTree(a,b,c)

countRequired = 0
for k in  traverseTree.count.keys():
  if traverseTree.count[k] > 1:
    continue
  countRequired = countRequired + 1

print countRequired


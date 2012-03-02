
data Tree a = Empty | Node a [ Tree a ]

-- binary version:
-- data Tree a = Empty | Node a ( Tree a ) ( Tree a )

treeSize :: Tree a -> Int 
treeSize Empty	        = 0 
treeSize ( Node x subtrees ) = 1 + sum ( map treeSize subtrees)

-- treeSize :: Tree a -> Int 
-- treeSize Empty	        = 0 
-- treeSize ( Node x l r ) = 1 + (treeSize l) + (treeSize r)


flatten :: Tree a -> [ a ]
flatten Empty = []
flatten ( Node x subtrees ) = x : concat(map flatten subtrees)

-- flatten :: Tree a -> [ a ] 
-- flatten Empty = []
-- flatten ( Node t1 x t2 ) = flatten t1 ++ (x:flatten t2)

headNode :: Tree a -> [a]
headNode Empty = []
headNode (Node x subtrees) = [x]

-- insert :: Int -> Tree Int -> Tree Int
-- insert n Empty = Node n []
-- insert n ( Node x subtrees ) | n <= x    = Node ( insert n t1 ) x t2 
--                           | otherwise = Node t1 x ( insert n t2 )


-- insert :: Int -> Tree Int -> Tree Int
-- insert n Empty = Node Empty n Empty
-- insert n ( Node t1 x t2 ) | n <= x    = Node ( insert n t1 ) x t2 
--                           | otherwise = Node t1 x ( insert n t2 )

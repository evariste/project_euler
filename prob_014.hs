-- The following iterative sequence is defined for the set of positive
-- integers:

-- n → n/2 (n is even)
-- n → 3n + 1 (n is odd)

-- Using the rule above and starting with 13, we generate the
-- following sequence: 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

-- It can be seen that this sequence (starting at 13 and finishing at
-- 1) contains 10 terms. Although it has not been proved yet (Collatz
-- Problem), it is thought that all starting numbers finish at 1.

-- Which starting number, under one million, produces the longest
-- chain?

-- NOTE: Once the chain starts the terms are allowed to go above one
-- million.


-- 837799
-- length 525 (524 steps to reach one)
-- But this solution is rubbish - should use a tree structure instead.

import List

main = do print (maxIndex)
          print (length (chain $ toInteger maxIndex))
          print (chain $ toInteger maxIndex)
          where maxIndex = (findIndices (== maxLen ) lens) !! 0
                lens = map length ( map chain [0..n] )
                maxLen = maximum (lens)
                n = 1000000


chain :: Integer -> [Integer]
chain 1 = [1]
chain n | (mod n 2) == 0 = n : (chain (div n 2))
        | otherwise      = n : (chain (3*n + 1))


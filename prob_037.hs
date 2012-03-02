-- The number 3797 has an interesting property. Being prime itself, it
-- is possible to continuously remove digits from left to right, and
-- remain prime at each stage: 3797, 797, 97, and 7. Similarly we can
-- work from right to left: 3797, 379, 37, and 3.

-- Find the sum of the only eleven primes that are both truncatable
-- from left to right and right to left.

-- NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


-- A: 748317

import MyFuncs

truncatable :: (Integral a, Ord a) => [a] -> a -> Bool
truncatable ps x
   | (x < 10) && (elem x ps) = True
   | otherwise               = and $ map (flip elem ps) ts
   where left  = takeWhile (<x) $ map (mod x) $ iterate (10*) 10
         right = takeWhile (>0) $ map (div x) $ iterate (10*) 10
         ts = left ++ right


main = do
     x <- readFile "firstMillionPrimes.txt" 
     let n = 100000
     let pstr = take n $ readWord x
     let pnum = take n $ readInteger x
     -- Remove primes with any of 024568 in any digit except the leading one.
     let temp = filter (\x -> and $ map (flip notElem "024685") $ tail x) pstr
     let cands = map toInteger $ map read temp
     let ts' = filter (truncatable pnum) cands
     let ts = dropWhile (<10) ts' -- Remove single digit primes.
     print $ length cands
     print $ last cands
     print ts
     print $ length ts -- We're told there are 11
     print $ sum ts
--      2734
--      1199999
--      [23,37,53,73,313,317,373,797,3137,3797,739397]
--      11
--      748317


-- A unit fraction contains 1 in the numerator. The decimal
-- representation of the unit fractions with denominators 2 to 10 are
-- given:

--     1/2	= 	0.5
--     1/3	= 	0.(3)
--     1/4	= 	0.25
--     1/5	= 	0.2
--     1/6	= 	0.1(6)
--     1/7	= 	0.(142857)
--     1/8	= 	0.125
--     1/9	= 	0.(1)
--     1/10	= 	0.1

-- Where 0.1(6) means 0.166666..., and has a 1-digit recurring
-- cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

-- Find the value of d < 1000 for which 1/d contains the longest
-- recurring cycle in its decimal fraction part.


import List

stripFactor :: Integer -> Integer -> Integer
stripFactor x f
  | rem x f > 0 = x
  | otherwise   = stripFactor x' f
  where x' = div x f


lenRec :: Integer -> Integer
-- Pre : n > 0
-- If the only prime factors are 2 and/or 5, the fraction terminates.
-- Otherwise the length is determined by the factor that remains after
-- stripping out 2 and 5 as much as possible (n').
-- In that case, find the first k s.t. 10^k == 1 mod n'
lenRec n 
 | n' == 1   = 0
 | otherwise = toInteger $ (+1) $ length $ takeWhile (>1) $ iterate ((flip mod n').(*10)) 10  
    where n' = foldl stripFactor n [2,5]


main = do
  let l = [1..1000]
  let ll = zip (map lenRec l) l
  print "d"
  print $ snd $ last $ sort ll
  print "length"
  print $ fst $ last $ sort ll


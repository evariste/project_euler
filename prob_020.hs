-- n! means n × (n − 1) × ... × 3 × 2 × 1

-- Find the sum of the digits in the number 100!

-- A: 648

import MyFuncs


main = do print $ digitSum $ foldl1 (*) [1..100]
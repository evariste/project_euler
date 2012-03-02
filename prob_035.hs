
-- The number, 197, is called a circular prime because all rotations
-- of the digits: 197, 971, and 719, are themselves prime.

-- There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17,
-- 31, 37, 71, 73, 79, and 97.

-- How many circular primes are there below one million?


-- A: 55 

-- They are:

--    2, 3, 5, 7, 11, 31, 71, 13, 73, 17, 37, 97, 79, 131, 311, 971,
--    991, 113, 373, 733, 197, 337, 199, 719, 919, 3119, 1193, 9311,
--    9377, 3779, 7793, 1931, 7937, 11939, 19391, 19937, 37199, 39119,
--    71993, 91193, 93719, 93911, 99371, 939391, 999331, 199933,
--    319993, 919393, 939193, 193939, 331999, 391939, 393919, 933199,
--    993319

import MyFuncs

rotateDigits :: (Integral a, Ord a, Num a) => a -> a
rotateDigits x
 | x < 10    = x
 | otherwise = u*(10^n) + rest
 where (rest, u) = quotRem x 10
       n = length $ takeWhile (>10) $ iterate (flip div 10) x

-- Second argument is a list of primes. Third is a number of repetitions.
-- First arg is the list of primes to check.
testSetOfPrimes :: [Integer] -> [Integer] -> Int -> [Integer]
testSetOfPrimes rotP p 0 = rotP
testSetOfPrimes rotP p n = testSetOfPrimes rotP2 p (n - 1)
                -- Which numbers remain prime after one cycle of the digits.
                where rotP2 = filter (flip elem p) $  map rotateDigits rotP

main = do
     x<- readFile "firstMillionPrimes.txt"
     let p = takeWhile (<1000000) $ readInteger x 
     let rotP = p
     -- Only need up to 5 cycles of the digits
     -- Could filter out any primes with a 2,5 or 0 in them first to speed things up.
     let final = testSetOfPrimes rotP p 5
     print $ length final
     print final



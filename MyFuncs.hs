module MyFuncs 
( splitDigits
, uniq
, primes
, digitSum
, fib
, isInt
, factorial
, readInteger
, readWord
) where

import Data.List
import Char

-- Extract integers from a string where they are separated by spaces
-- or returns.
readWord :: [Char] -> [[Char]]
readWord [] = []
readWord x  = [fst] ++ (readWord rest)
            where
              fst  = takeWhile (/=' ') $ dropWhile (flip elem " \r\n") x
              rest = dropWhile (/=' ') $ dropWhile (flip elem " \r\n") x

-- Extract integers from a string where they are separated by spaces
-- or returns.
readInteger :: [Char] -> [Integer]
readInteger [] = []
readInteger x = [fst] ++ (readInteger rest)
            where
              fst  = toInteger $ read $  takeWhile (/=' ') $ dropWhile (flip elem " \r\n") x
              rest = dropWhile (/=' ') $ dropWhile (flip elem " \r\n") x


factorial :: (Ord a, Num a) => a -> a
factorial n
  | n < 0     = 0
  | n == 0    = 1
  | otherwise = n * factorial (n-1)

-- Convert a number into a list of its digits.
splitDigits :: Int -> [Int]
splitDigits d =  map digitToInt $ show $ d

-- Remove duplicates from a list - can use 'nub' from Data.List instead.
uniq [] = []
uniq xs = x : map snd (filter (uncurry (/=)) (zip sxs (tail sxs)))
    where sxs = sort xs
          x   = head sxs

-- Infinite list of primes.
primes :: (Integral a) => [a]
primes    = 2: oddprimes
 where oddprimes = 3: sieve oddprimes 3 0
       sieve (p:ps) x k 
          = [n | n <- [x+2,x+4..p*p-2]
                 , and [rem n p/=0 | p <- take k oddprimes]]
            ++ sieve ps (p*p) (k+1)



isInt :: Float -> Bool
isInt x = x == (fromInteger $ round(x))

-- Fibonacci
fib :: Integer -> Integer
-- Pre: n in fib n is non-negative
fib 0 = 0
fib 1 = 1
-- fib n = ( fib (n-1) ) + ( fib (n-2) ) .... Slow for large n!
fib n = let phi = 0.5 * (1 + sqrt(5));
        in  floor $ 0.5 + ( phi^n / sqrt(5) ) 


digitCount :: Integer -> Integer
digitCount n
  | n < 0  = digitCount $ -1 * n 
  | n < 10 = 1
  | otherwise = 1 + digitCount m
    where (m, k) = divMod n 10


digitSum :: Integer -> Integer
digitSum n
  | n < 0     = digitSum $ negate n
  | n == 0    = 0
  | otherwise = final + digitSum rest
    where (rest, final) = divMod n 10



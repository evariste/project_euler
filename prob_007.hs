-- By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
-- see that the 6^(th) prime is 13.
 
-- What is the 10001^(st) prime number?


isPrime a = isPrimeHelper a primes

isPrimeHelper a (p:ps)
  | p*p > a        = True
  | a `mod` p == 0 = False
  | otherwise      = isPrimeHelper a ps

primes = 2 : filter isPrime [3..]

main = print $ primes !! 10000 


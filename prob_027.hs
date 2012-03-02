-- Mostly messing about, done with matlab.

primes    = 2: oddprimes
oddprimes = 3: sieve oddprimes 3 0
sieve (p:ps) x k 
          = [n | n <- [x+2,x+4..p*p-2]
                 , and [rem n p/=0 | p <- take k oddprimes]]
            ++ sieve ps (p*p) (k+1)
-- oddprimes:

-- 3: sieve [3,..] 3 0
-- 3: [n | n<- [5,7] and [rem n p/= 0 | p <-.take 0 [3,..]] ++ sieve ps p*p (k+1)
-- 3: [n | n<- [5,7] and [ ] ++ sieve ps p*p (k+1)
-- 3: [5,7] ++ sieve [5,7,..] 9 1

-- sieve [5,7,..] 9 1
-- sieve 5:[7,..] 9 1
-- [n | n <- [9,11,..,23] , and [rem n p/=0 | p <- take 1 oddprimes]] ++ sieve ps p*p (k+1)
-- [n | n <- [9,11,..,23] , and [rem n p/=0 | p <- take 1 oddprimes]] ++ sieve ps p*p (k+1)
-- [n | n <- [9,11,..,23] , and [rem n p/=0 | p <- [3]]] ++ sieve ps p*p (k+1)
-- [11,13,17,19,23] ++ sieve [7,11,13,17,19,23,..] 25 2

-- sieve [7,11,13,17,19,23,..] 25 2
-- seive 7:[11,..] 25 2
-- [n | n <- [27,29..47], and [rem n p/=0 | p <- take 2 oddprimes]] ++ sieve ps p*p k+1
-- [n | n <- [27,29..47], and [rem n p/=0 | [3,5]] ++ sieve ps p*p k+1



quad a b = \n -> n^2  + a * n + b

isPrime n = n == (last $ takeWhile (<=n) primes)


testQuad a b = takeWhile isPrime $ map (quad a b) [0..]


checkPrimeWithList :: [Integer] -> Integer -> Bool
checkPrimeWithList p n
  = not $ elem 0 $ map (mod n) p'
  where p' = takeWhile (<  limit) p
        limit = (+1) $ floor $ sqrt $ fromInteger n


growPrimeList :: [Integer] -> [Integer]
growPrimeList [2] = [2, 3]
growPrimeList x   = x ++ [next]
                 where next = (last x) + 2*k
                       k = toInteger $ (+1) $ length $ takeWhile (==False) $ map (checkPrimeWithList x) cands
                       cands = tail $ iterate (+2) $ last x
--   The fraction ^(49)/_(98) is a curious fraction, as an
--   inexperienced mathematician in attempting to simplify it may
--   incorrectly believe that ^(49)/_(98) = ^(4)/_(8), which is
--   correct, is obtained by cancelling the 9s.

--   We shall consider fractions like, ^(30)/_(50) = ^(3)/_(5), to be
--   trivial examples.

--   There are exactly four non-trivial examples of this type of
--   fraction, less than one in value, and containing two digits in
--   the numerator and denominator.

--   If the product of these four fractions is given in its lowest
--   common terms, find the value of the denominator.

--   A: 100
-- 
-- Excellent answer from forum:
-- Preamble:
--   'xy' / 'yz' = x/z
--   (10x + y) / (10y+z) = x/z
--   9xz + yz = 10xy 
-- 
-- So:
-- 
-- [(10*x+y,10*y+z) | x <- [1..9], y <- [1..9], z <- [1..9], x /= y , (9*x*z) + (y*z) == (10*x*y)]

import List

match :: (Ord a, Integral a) => a -> a -> Bool
match x y
  | x < 10 || y < 10         = False
  | x > 99 || y > 99         = False
  | x == y                   = False
  | ux==dx || uy==dy         = False
  | ux==0                    = False
  | ux == uy && x*dy == y*dx = True
  | ux == dy && x*uy == y*dx = True
  | dx == uy && x*dy == y*ux = True
  | dx == dy && x*uy == y*ux = True
  | otherwise                = False
    where (dx, ux) = quotRem x 10
          (dy, uy) = quotRem y 10

--     x   [dx ux]    dx
--     - = ------- == --
--     y   [dy uy]    dy

--     ux == uy && x*dy == y*dx

--     x   [dx ux]    dx
--     - = ------- == --
--     y   [dy uy]    uy

--     ux == dy && x*uy == y*dx

--     x   [dx ux]    ux
--     - = ------- == --
--     y   [dy uy]    dy

--     dx == uy && x*dy == y*ux

--     x   [dx ux]    ux
--     - = ------- == --
--     y   [dy uy]    uy

--     dx == dy && x*uy == y*ux



simplifyFrac :: (Integral a) => (a, a) -> (a, a)
simplifyFrac (x, y) = (div x d, div y d)
              where d = gcd x y


main = do
     let fracs = [(a,b) |  a<-[10..98] , b<-[a..99], b/=a]
     let l = nub $ map simplifyFrac $ filter (uncurry match) fracs
     let a = foldl1 (*) $ map fst l
     let b = foldl1 (*) $ map snd l
     print $ snd $ simplifyFrac (a, b)

-- *Main List> filter (uncurry match) [(a,b) |  a<-[10..98] , b<-[a..99], b/=a]

-- [(16,64),(19,95),(26,65),(49,98)]

--   An irrational decimal fraction is created by concatenating the
--   positive integers:

--   0.123456789101112131415161718192021...

--   It can be seen that the 12^(th) digit of the fractional part is
--   1.

--   If d_(n) represents the n^(th) digit of the fractional part, find
--   the value of the following expression.

--   d_(1) × d_(10) × d_(100) × d_(1000) × d_(10000) × d_(100000) × d_(1000000)


-- A: 



--
-- 0.123456789      1011121314151617181920..9899 100101102103...998999 100010011002
--    batch 1        batch 2                      batch 3               batch 4
--index starts at 1  starts at 10                 starts at 190         starts at 2890

-- no.  start index         end index                  digits
-- 10   1                .. 1+9*1-1                    0..9
-- 90   1+9*1            .. 1+9*1+90*2-1               10..99
-- 900  1+9*1+90*2       .. 1+9*1+90*2+900*3-1         100..999
-- 9000 1+9*1+90*2+900*3 .. 1+9*1+90*2+900*3+9000*4-1  1000..9999

-- 10^(n-1)..10^n-1

--      1+9*1+90*2+900*3+..+9*[10^(n-2)]*(n-1) ..
--              1+9*1+90*2+900*3+..+9*[10^(n-1)]*n - 1


-- 1 + 9 * (1 + 10*2 + 100*3 + 1000*4 + ...)

import MyFuncs

-- Return the batch number and the starting index of the batch for a
-- given index.
index2batch :: Int -> (Int, Int)
index2batch x = (length ll, last ll)
            where ll = takeWhile (<=x) l
                  l =  [1] ++ ( map (\x -> 1 + x*9) $ scanl1 (+) $ zipWith (*) [1..]  $ iterate (*10) 1 )


index2digit :: Int -> Int
index2digit x = (splitDigits no) !! posInNo
            where 
             (nDigits, batchStartInd) = index2batch x
             rangeStart = 10^(nDigits - 1)
             (offset, posInNo) = quotRem (x - batchStartInd) nDigits
             no = rangeStart + offset

main = do
     print $ product $ map index2digit $ take 7 $ iterate (*10) 1

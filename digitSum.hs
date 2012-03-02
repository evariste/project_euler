
digitSum :: Integer -> Integer
digitSum n
  | n < 0     = digitSum $ negate n
  | n == 0    = 0
  | otherwise = final + digitSum rest
    where (rest, final) = divMod n 10



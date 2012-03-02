-- Work out the first ten digits of the sum of the following
-- one-hundred 50-digit numbers.

-- A: 5537376230


main = do x <- readFile "prob_013.data"
          let rows = lines(x)
          let s = sum (map rInt rows)
          print s
          print (  map ((show s) !!) [0..9]  )
          -- Or ... didn't really need to re-implement 'take' on the
          -- previous line ...
          let sStr = show s
          print (take 10 sStr)
          
rInt :: String -> Integer
rInt = read

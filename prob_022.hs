
-- Using names.txt (right click and 'Save Link/Target As...'), a 46K
-- text file containing over five-thousand first names, begin by
-- sorting it into alphabetical order. Then working out the
-- alphabetical value for each name, multiply this value by its
-- alphabetical position in the list to obtain a name score.

-- For example, when the list is sorted into alphabetical order,
-- COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name
-- in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

-- What is the total of all the name scores in the file?

-- A: 871198282


import Char
import List

getNames :: [Char] -> [[Char]]
getNames [] = []
getNames x  = [fst] ++ (getNames rest) 
          where 
             fst  = takeWhile isAlpha  $ dropWhile (not . isAlpha) x 
             rest = dropWhile isAlpha  $ dropWhile (not . isAlpha) x

strToLower :: [Char] -> [Char]
strToLower str = map toLower str

-- Pre : x is lower case.
charValue :: Char -> Int
charValue x = ord x - ord 'a' + 1

strValues :: [Char] -> [Int]
strValues str = map charValue str

main = do 
       x <- readFile "prob_022.txt"
       -- there will be an empty string at the end of the list of
       -- names
       let names    = takeWhile (/= "") $ getNames x
       let lowNames = sort $ map strToLower names
       let lenNames = map strValues lowNames
       let totals   = map sum lenNames
       print $ sum $ zipWith (*) totals [1..]

--        print $ lowerNames !! 937
--        print $ length lowerNames
--        print $ last lowerNames
--        print $ take 5 lenNames 
--        print $ last lenNames 
--        print $ take 5 totals
--        print $ take 5 totalsWeighted
--        print $ last totals
--        print $ last totalsWeighted
--        print $ sum totalsWeighted

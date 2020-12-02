module Day02 where

import Text.Printf(printf)

-- Main zone--
main = do
  input <- readFile "../inputs/02.txt"
  printf "part 1: %d\n" $ part1 input
  printf "part 2: %d\n" $ part2 input

part1 input = length $ filter is_valid_1 $ makeLines input
part2 input = length $ filter is_valid_2 $ makeLines input

-- For part 1 --
count :: Char -> String -> Int
count c s = length $ filter (c==) s

is_valid_1 :: Line -> Bool
is_valid_1 (low, high, letter, password) = 
  letter_count >= low && letter_count <= high
  where letter_count = count letter password

-- For part 2 --
is_valid_2 :: Line -> Bool
is_valid_2 (low, high, letter, password) = 
  (password!!(low-1) == letter) /= (password!!(high-1) == letter) 

-- For both parts --
type Line = (Int, Int, Char, String)

replace :: Char -> Char -> String -> String
replace c1 c2 s = map (\c -> if c==c1 then c2 else c) s

parse :: String -> [String]
parse s = words $ replace '-' ' ' (filter (':'/=) s)

makeLine :: [String] -> Line
makeLine (a:b:c:d:_) = (read a, read b, head c, d)

makeLines :: String -> [Line]
makeLines input = map (makeLine . parse) $ lines input

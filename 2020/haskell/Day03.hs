module Day03 where

import Text.Printf(printf)

-- Main zone--
main = do
  input <- readFile "../inputs/03.txt"
  printf "part 1: %d\n" $ part1 input
  printf "part 2: %d\n" $ part2 input

part1 input = countTrees (lines input) (3,1)
part2 input = product $ map (countTrees (lines input)) [(1,1),(3,1),(5,1),(7,1),(1,2)]

-- For both parts --
visit :: [String] -> Int -> Int -> String
visit s dx dy = map (\t -> s!!(fst t)!!(snd t)) indices
  where 
    indices = [
        (mod y height, mod (floor (fromIntegral y*m)) width) | 
        y <- [dy,2*dy..height-1]
      ]
      where 
        height = length s
        width = length (s!!0)
        m = fdiv dx dy

countTrees :: [String] -> (Int, Int) -> Int
countTrees s slope = length $ filter ('#'==) $ visit s dx dy
  where 
    dx = fst slope
    dy = snd slope

fdiv :: Int -> Int -> Float
fdiv a b = (fromIntegral a) / (fromIntegral b)

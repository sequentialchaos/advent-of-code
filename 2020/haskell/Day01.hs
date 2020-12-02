module Day01 where

import Text.Printf(printf)

main = do
  input <- readFile "../inputs/01.txt"
  printf "part 1: %d\n" $ part1 $ linesToInts input
  printf "part 2: %d\n" $ part2 $ linesToInts input

part1 xs = [
    xs!!i * (2020 - xs!!i) | 
    i <- [0..(length xs - 1)], 
    elem (2020 - xs!!i) xs
  ]!!0

part2 xs = [
    xs!!i * xs!!j * (2020 - xs!!i - xs!!j)| 
    i <- [0..(length xs - 2)], 
    j <- [i+1..(length xs - 1)], 
    elem (2020 - xs!!i - xs!!j) xs
  ]!!0

-- For both parts --
linesToInts :: String -> [Int]
linesToInts a = map read (lines a)

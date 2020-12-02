module Day02 where

import Text.Printf(printf)

main = do
  input <- readFile "../inputs/02.txt"
  printf "part 1: %d\n" $ part1 input
  printf "part 2: %d\n" $ part2 input

part1 input = sum $ map (wrappingPaper . parseDimensions) $ lines input
part2 input = sum $ map (ribbon . parseDimensions) $ lines input

-- For both parts --
parseDimensions :: [Char] -> [Int]
parseDimensions s = map read $ lines $ map (\c -> if c=='x' then '\n' else c) s

-- For part 1 --
minSideArea :: [Int] -> Int
minSideArea xs = minimum [xs!!i * xs!!j | i <- [0..length xs - 2], j <- [i+1..length xs - 1]]

wrappingPaper :: [Int] -> Int
wrappingPaper (l:w:h:_) = 2*l*w + 2*l*h + 2*w*h + minSideArea [l,w,h]

-- For part 2 --
minSidePerimeter :: [Int] -> Int
minSidePerimeter xs = minimum [2*xs!!i + 2*xs!!j | i <- [0..length xs - 2], j <- [i+1..length xs - 1]]

volume :: Int -> Int -> Int -> Int
volume l w h = l*w*h

ribbon :: [Int] -> Int
ribbon (l:w:h:_) = volume l w h + minSidePerimeter [l,w,h]

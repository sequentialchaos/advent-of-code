module Day03 where

import Text.Printf(printf)
import Data.List

main = do
  input <- readFile "../inputs/03.txt"
  printf "part 1: %d\n" $ part1 input
  -- printf "part 2: %d\n" $ part2 input

part1 input = length $ nub $ positions input
part2 input = 0

-- For both parts --
direction :: Char -> [Int, Int]
direction c
  | c=='>' = [ 1,  0]
  | c=='<' = [-1,  0]
  | c=='^' = [ 0,  1]
  | c=='v' = [ 0, -1]

nextPosition :: [Int, Int] -> Char -> [Int, Int]
nextPosition position arrow = zipWith (+) position (direction arrow)

xFilter :: Char -> Int
xFilter c 
  | c=='>' = 1
  | c=='<' = -1
  | otherwise = 0

yFilter :: Char -> Int
yFilter c
  | c=='^' = 1
  | c=='v' = -1
  | otherwise = 0

xMovements :: String -> [Int]
xMovements s = map xFilter s

yMovements :: String -> [Int]
yMovements s = map yFilter s

xPositions :: String -> [Int]
xPositions s = [0] ++ (scanl1 (+) $ xMovements s)

yPositions :: String -> [Int]
yPositions s = [0] ++ (scanl1 (+) $ yMovements s)

positions :: String -> [(Int,Int)]
positions s = zip (xPositions s) (yPositions s)

-- For part 1 --

-- For part 2 --


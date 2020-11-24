import Data.List
import Text.Printf(printf)

main = do
  input <- readFile "01.txt"
  printf "part 1: %d\n" (whichFloor input)
  printf "part 2: %d\n" (basementPosition input)

whichFloor :: [Char] -> Int
whichFloor s = length [c | c <- s, c == '('] - length [c | c <- s, c == ')']

basementPosition :: String -> Int
basementPosition s = 
  case position of 
    Nothing -> (-1)
    Just p -> p + 1
  where 
    position = 
      elemIndex (-1) $ 
      scanl1 (+) $ 
      map (\c -> if c == '(' then 1 else -1) s

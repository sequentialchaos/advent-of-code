
def main():
  s = read_input()
  print(f'part 1: {part_1(s, (3,1))}')
  print(f'part 2: {part_2(s, [(1,1), (3,1), (5,1), (7,1), (1,2)])}')

def part_1(s, slope):
  return count_trees(s, slope)

def part_2(s, slopes):
  product = 1
  for slope in slopes:
    product *= count_trees(s, slope)
  return product

#####################################################################

def read_input():
  with open('../inputs/03.txt') as f:
    return [line.strip() for line in f.readlines()]

def traverse(s, slope):
  dx, dy = slope
  height, width = len(s), len(s[0])
  return (
    s[y][int(y*dx/dy) % width] 
    for y in range(dy, height, dy)
  ) 

def count_trees(s, slope):
  return sum(c == '#' for c in traverse(s, slope))

#####################################################################

if __name__ == "__main__":
  main()

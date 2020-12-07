import re

def main():
  s = read_input()
  print(f'part 1: {part_1(s)}')
  print(f'part 2: {part_2(s)}')

def part_1(s):
  grid = make_grid()
  for line in s:
    instruction, x1, y1, x2, y2 = line
    grid = update_1(grid, instruction, x1, y1, x2, y2)
  return sum(sum(row) for row in grid)

def part_2(s):
  grid = make_grid()
  for line in s:
    instruction, x1, y1, x2, y2 = line
    grid = update_2(grid, instruction, x1, y1, x2, y2)
  return sum(sum(row) for row in grid)

#####################################################################

def read_input():
  parse_instruction = lambda line: re.findall("(\w+)+ \d", line)[0]
  parse_position = lambda line: [int(n) for n in re.findall('(\d+)', line)]
  parse = lambda line: [parse_instruction(line)] + parse_position(line)
  with open('../inputs/06.txt') as f:
    return [parse(line) for line in f.readlines()]

def make_grid():
  return [[0 for i in range(1000)] for j in range(1000)]

def update_1(grid, instruction, x1, y1, x2, y2):
  for y in range(y1, y2+1):
    for x in range(x1, x2+1):
      if instruction == 'on':
        grid[y][x] = 1
      elif instruction == 'off':
        grid[y][x] = 0
      else:
        grid[y][x] = 1 if grid[y][x] == 0 else 0
  return grid

def update_2(grid, instruction, x1, y1, x2, y2):
  for y in range(y1, y2+1):
    for x in range(x1, x2+1):
      if instruction == 'on':
        grid[y][x] += 1
      elif instruction == 'off':
        grid[y][x] = grid[y][x] - 1 if grid[y][x] > 0 else 0
      else:
        grid[y][x] += 2
  return grid

#####################################################################

if __name__ == "__main__":
  main()

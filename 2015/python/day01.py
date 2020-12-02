
def read_input():
  with open('../inputs/01.txt') as f:
    return f.read()

def part1(s):
  return s.count('(') - s.count(')')

def part2(s):
  movements = [1 if c == '(' else -1 for c in s]
  positions = movements
  for i in range(1, len(positions)):
    positions[i] = positions[i-1] + positions[i]
  basement = xs.index(-1) + 1
  return basement

def main():
  s = read_input()
  print(f'part 1: {part1(s)}')
  print(f'part 2: {part2(s)}')

if __name__ == "__main__":
  main()

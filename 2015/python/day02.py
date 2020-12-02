
def read_input():
  with open('../inputs/02.txt') as f:
    return f.read()

def part1(s):
  return s.count('(') - s.count(')')

def part2(s):
  def movements(s):
    return [1 if c == '(' else -1 for c in s]
  def positions(xs):
    ys = xs
    for i in range(1, len(ys)):
      ys[i] = ys[i-1] + ys[i]
    return ys
  def find(value, xs):
    return xs.index(value) + 1
  return find(-1, positions(movements(s)))

def main():
  s = read_input()
  print(f'part 1: {part1(s)}')
  print(f'part 2: {part2(s)}')

if __name__ == "__main__":
  main()


def read_input():
  with open('../inputs/03.txt') as f:
    return f.read()

def part1(s):
  position = (0,0)
  a = [position]
  for c in s:
    x = position[0]
    y = position[1]
    if c == '^':
      y += 1
    elif c == '>':
      x += 1
    elif c == 'v':
      y -= 1
    elif c == '<':
      x -= 1
    position = (x,y)
    a.append(position)
  print(a)
  return len(set(a))

def part2(s):
  santa = (0,0)
  robo_santa = (0,0)
  a = [santa, robo_santa]
  for i,c in enumerate(s):
    if i % 2 == 0:
      x = santa[0]
      y = santa[1]
    else:
      x = robo_santa[0]
      y = robo_santa[1]
    if c == '^':
      y += 1
    elif c == '>':
      x += 1
    elif c == 'v':
      y -= 1
    elif c == '<':
      x -= 1
    if i % 2 == 0:
      santa = (x,y)
      a.append(santa)
    else:
      robo_santa = (x,y)
      a.append(robo_santa)
  return len(set(a))

def main():
  s = read_input()
  print(f'part 1: {part1(s)}')
  print(f'part 2: {part2(s)}')

if __name__ == "__main__":
  main()

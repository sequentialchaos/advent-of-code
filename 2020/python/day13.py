import math

def main():
  s = read_input()
  print(f'part 1: {part_1(s)}')
  print(f'part 2: {part_2(s)}')

def part_1(s):
  timestamp, bus_ids = s
  bus_ids = [t[0] for t in bus_ids]
  t = min([
    (n * math.ceil(timestamp / n) - timestamp, n) 
    for n in bus_ids
  ], key = lambda t: t[0])
  return t[0]

def part_2(s):
  timestamp, bus_ids = s
  first_bus = bus_ids[0][0]
  m = 1
  b = 0
  for j in range(2, len(bus_ids)+1):
    x = 1
    while True:
      c = first_bus * (m*x + b)
      if check(c, bus_ids[:j]):
        m *= bus_ids[j-1][0]
        b = c // first_bus
        break
      x += 1
  return c

#####################################################################
def read_input():
  def parse(line):
    s = line.split(',')
    return [(int(n), s.index(n)) for n in s if n != 'x']
  with open('../inputs/13.txt') as f:
    lines = f.readlines()
    return int(lines[0]), parse(lines[1])

def check(n, ids):
  return all((n+offset) % b == 0 for b,offset in ids)

#####################################################################
if __name__ == "__main__":
  main()

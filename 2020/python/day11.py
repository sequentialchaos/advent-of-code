def main():
  s = read_input()
  print(f'part 1: {part_1(s)}')
  print(f'part 2: {part_2(s)}')

def part_1(s):
  while True:
    s = next_layout(s, get_neighbors_1, 4)
    t = next_layout(s, get_neighbors_1, 4)
    if count(s, '#') == count(t, '#'):
      return count(s, '#')

def part_2(s):
  while True:
    s = next_layout(s, get_neighbors_2, 5)
    t = next_layout(s, get_neighbors_2, 5)
    if count(s, '#') == count(t, '#'):
      return count(s, '#')

#####################################################################
def read_input():
  with open('../inputs/11.txt') as f:
    return [[c for c in line.strip()] for line in f.readlines()]

def are_equal(a1, a2):
  return all(
    a1[i][j] == a2[i][j] 
    for i in range(len(a1)) 
    for j in range(len(a1[0]))
  )

def next_layout(layout, neighbors_function, max_occupied):
  return [
    [
      apply_rules(layout, i, j, neighbors_function, max_occupied) 
      for i in range(len(layout))
    ] 
    for j in range(len(layout[0]))
  ]

def apply_rules(layout, i, j, neighbors_function, max_occupied):
  if layout[i][j] == '.':
    return '.'
  if layout[i][j] == '#':
    if sum(c == '#' for c in neighbors_function(layout, i, j)) >= max_occupied:
      return 'L'
    else:
      return '#'
  if layout[i][j] == 'L':
    if sum(c == '#' for c in neighbors_function(layout, i, j)) == 0:
      return '#'
    else:
      return 'L'

def get_neighbors_1(layout, i, j):
  for m in range(i-1, i+2):
    for n in range(j-1, j+2):
      if m == i and n == j:
        continue
      if is_valid(layout, m, n):
        yield layout[m][n]

def get_neighbors_2(layout, i, j):
  directions = ['NE','E','SE','S','SW','W','NW','N']
  for direction in directions:
    yield search_direction(layout, i, j, direction)

def get_direction(direction):
  if direction == 'NE': return (-1, 1)
  if direction == 'E':  return (0, 1)
  if direction == 'SE': return (1, 1)
  if direction == 'S':  return (1, 0)
  if direction == 'SW': return (1, -1)
  if direction == 'W':  return (0, -1)
  if direction == 'NW': return (-1, -1)
  if direction == 'N':  return (-1, 0)

def search_direction(layout, i, j, direction):
  d = get_direction(direction)
  m, n = i + d[0], j + d[1]
  while True:
    if is_valid(layout, m, n):
      c = layout[m][n]
      if c != '.':
        return c
    else:
      break
    m += d[0]
    n += d[1]
  return '.'

def is_valid(layout, i, j):
  return 0 <= i <= len(layout)-1 and 0 <= j <= len(layout[0])-1

def count(layout, c):
  return sum(
    c == layout[i][j] 
    for i in range(len(layout)) 
    for j in range(len(layout[0]))
  )

def pretty_print(layout):
  s = ''
  for i in range(len(layout)):
    for j in range(len(layout[i])):
      s += layout[i][j]
    s += '\n'
  print(s)

#####################################################################
if __name__ == "__main__":
  main()

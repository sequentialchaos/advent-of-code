import re

def main():
  s = read_input()
  print(f'part 1: {part_1(s)}')
  print(f'part 2: {part_2(s)}')

def part_1(s):
  position = [0, 0]
  degrees = 0
  directions = ['E','S','W','N']
  for line in s:
    action, value = line
    if action in directions:
      position = move(position, action, value)
    else:
      if action == 'R':
        degrees = (degrees + value) % 360
      if action == 'L':
        degrees = (degrees - value) % 360
      if action == 'F':
        direction = directions[degrees // 90]
        position = move(position, direction, value)
  return sum(map(abs, position))

def part_2(s):
  position = [0, 0]
  waypoint = [10, 1]
  directions = ['E','S','W','N']
  for line in s:
    action, value = line
    if action in directions:
      waypoint = move(waypoint, action, value)
    else:
      if action in ['R', 'L']:
        degrees = value if action == 'R' else -value
        degrees = degrees % 360
        waypoint = rotate_waypoint(waypoint, degrees)
      if action == 'F':
        position[0] += value * waypoint[0]
        position[1] += value * waypoint[1]
  return sum(map(abs, position))

#####################################################################
def read_input():
  parse = lambda line: (line[0], int(line[1:]))
  with open('../inputs/12.txt') as f:
    return [parse(line.strip()) for line in f.readlines()]

def move(starting_position, direction, amount):
  x, y = starting_position
  if 'E' == direction:
    return [x + amount, y]
  if 'W' == direction:
    return [x - amount, y]
  if 'N' == direction:
    return [x, y + amount]
  if 'S' == direction:
    return [x, y - amount]

def rotate_waypoint(current, degrees):
  position = current * 1
  for _ in range(degrees // 90):
    position = [position[1], position[0] * -1]
  return position

#####################################################################
if __name__ == "__main__":
  main()

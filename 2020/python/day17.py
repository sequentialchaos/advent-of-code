from itertools import product

def main():
  grid = read_input()
  print(f'part 1: {part_1(grid, 6)}')
  print(f'part 2: {part_2(grid, 6)}')

def part_1(grid, num_cycles):
  coordinates = get_initial_coordinates(grid, 3)
  for _ in range(num_cycles):
    coordinates = execute_cycle(coordinates)
  return len(coordinates)

def part_2(grid, num_cycles):
  coordinates = get_initial_coordinates(grid, 4)
  for _ in range(num_cycles):
    coordinates = execute_cycle(coordinates)
  return len(coordinates)

#####################################################################

def read_input():
  with open('../inputs/17.txt') as f:
    return [[c for c in line.strip()] for line in f.readlines()]

def get_initial_coordinates(grid, num_dimensions):
  '''Returns the initial coordinates for each of the cubes in a grid.'''
  coordinates = set({})
  for y, row in enumerate(grid):
    for x, value in enumerate(row):
      if value == '#':
        zeroes = [0] * (num_dimensions - 2)
        coordinate = tuple([x, y] + zeroes)
        coordinates.add(coordinate)
  return coordinates


def get_neighbors(coordinate):
  '''Returns the coordinates for each of the neighbors of a given coordinate.'''
  num_dimensions = len(coordinate)
  return [
    tuple([coordinate[i] + distance[i] for i in range(num_dimensions)])
    for distance in product([-1, 0, 1], repeat=num_dimensions) 
    if not all(n == 0 for n in distance)
  ]

def execute_cycle(coordinates):
  '''Returns the new state of the coordinates after one cycle.'''
  new_coordinates = set({})
  num_neighbors = {}

  # add 1 to the neighbor count for each active coordinate's neighbor
  for coordinate in coordinates:
    for neighbor in get_neighbors(coordinate):
      num_neighbors.setdefault(neighbor, 0)
      num_neighbors[neighbor] += 1

  # process the counts of active neighbors for each coordinate
  for coordinate in num_neighbors.keys():
    if coordinate in coordinates:
      # coordinate is active => needs 2 or 3 active neighbors
      if num_neighbors[coordinate] in [2, 3]:
        new_coordinates.add(coordinate)
    else:
      # coordinate is inactive => needs exactly 3 active neighbors
      if num_neighbors[coordinate] == 3:
        new_coordinates.add(coordinate)

  return new_coordinates

#####################################################################

if __name__ == "__main__":
  main()

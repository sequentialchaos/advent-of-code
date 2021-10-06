from itertools import product

def main():
  s = read_input()
  print(f'part 1: {part_1(s)}')
  print(f'part 2: {part_2(s)}')

def part_1(s):
  pocket_dimension = Pocket_Dimension_3D(s)
  for n in range(6):
    pocket_dimension.get_next_state()
  return pocket_dimension.count_active_cubes()

def part_2(s):
  return 0

#####################################################################

def read_input():
  with open('../inputs/17.txt') as f:
    return [[c for c in line.strip()] for line in f.readlines()]

class Pocket_Dimension_3D:
  def __init__(self, initial_state):
    self.state = initial_state
    self.add_empty_layers()
    
  def add_empty_layers(self):
    empty_layer = self.make_empty_layer(len(self.state[0]), len(self.state))
    self.state = [empty_layer, self.state, empty_layer]

  def get_next_state(self):
    self.state = self.get_padded_state()
    layers = self.get_padded_state()
    for i in range(len(self.state)):
      for j in range(len(self.state[i])):
        for k in range(len(self.state[i][j])):
          layers[i][j][k] = self.apply_rules(self.state, i, j, k)
    self.state = layers

  def apply_rules(self, layers, i, j, k):
    neighbors = self.get_neighbors(layers, i, j, k)
    active_count = neighbors.count('#')
    if layers[i][j][k] == '#':
      if 2 <= active_count <= 3:
        return '#'
      else:
        return '.'
    else:
      if active_count == 3:
        return '#'
      else:
        return '.'

  def get_padded_state(self):
    min_j, min_k, max_j, max_k = self.minimum_frame()
    width = max_k - min_k + 3
    height = max_j - min_j + 3
    layers = []
    if not all(c == '.' for row in self.state[0] for c in row):
      layers.append(self.make_empty_layer(width, height))
    for i in range(len(self.state)):
      layer = [['.' for n in range(width)]]
      for j in range(min_j, max_j+1):
        row = ['.']
        for k in range(min_k, max_k+1):
          row.append(self.state[i][j][k])
        row.append('.')
        layer.append(row)
      layer.append(['.' for n in range(width)])
      layers.append(layer)
    if not all(c == '.' for row in self.state[-1] for c in row):
      layers.append(self.make_empty_layer(width, height))
    return layers

  def make_empty_layer(self, width,height):
    return [
      ['.' for k in range(width)]
      for j in range(height)
    ]

  def minimum_frame(self):
    min_j, max_j = 99999999, -99999999
    min_k, max_k = 99999999, -99999999
    for i, layer in enumerate(self.state):
      for j, row in enumerate(layer):
        for k, value in enumerate(row):
          if value == '#':
            if j < min_j:
              min_j = j
            if k < min_k:
              min_k = k
            if j > max_j:
              max_j = j
            if k > max_k:
              max_k = k
    return min_j, min_k, max_j, max_k

  def get_neighbors(self, layers, i, j, k):
    neighbors = []
    for x in range(i-1, i+2):
      if x < 0 or x >= len(layers):
        continue
      for y in range(j-1, j+2):
        if y < 0 or y >= len(layers[x]):
          continue
        for z in range(k-1, k+2):
          if z < 0 or z >= len(layers[x][y]):
            continue
          if not(x == i and y == j and z == k):
            neighbors.append(layers[x][y][z])
    return neighbors
    
  def count_active_cubes(self):
    return sum(sum(row.count('#') for row in layer) for layer in self.state)
  
  def pretty_print(self):
    for layer in self.state:
      print('\n'.join([''.join(row) for row in layer]))
      print()
    
#####################################################################

if __name__ == "__main__":
  main()

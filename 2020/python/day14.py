import re

def main():
  s = read_input()
  print(f'part 1: {part_1(s)}')
  print(f'part 2: {part_2(s)}')

def part_1(s):
  mem = {}
  for line in s:
    if line[0] == 'mask':
      mask = line[1]
    else:
      address, value = line[1], line[2]
      mem[address] = apply_mask_1(value, mask)
  return sum(mem.values())

def part_2(s):
  mem = {}
  for line in s:
    if line[0] == 'mask':
      mask = line[1]
    else:
      address, value = line[1], line[2]
      for masked_address in apply_mask_2(address, mask):
        mem[masked_address] = value
  return sum(mem.values())

#####################################################################
def read_input():
  def parse(line):
    if line[:4] == 'mask':
      return line.split(' = ')
    else:
      matches = re.match('(\w+)\[(\d+)\] = (\d+)', line).groups()
      return (matches[0], int(matches[1]), int(matches[2]))
  with open('../inputs/14.txt') as f:
    return [parse(line.strip()) for line in f.readlines()]

def apply_mask_1(number, mask):
  binary_str = str(bin(number))[2:].zfill(36)
  return int(''.join([
    c if mask[i] == 'X' else mask[i] 
    for i,c in enumerate(binary_str)
  ]), 2)

def apply_mask_2(number, mask):
  binary_str = str(bin(number))[2:].zfill(36)
  base = ''.join([
    c if mask[i] == '0' else mask[i] 
    for i,c in enumerate(binary_str)
  ])
  x_indices = [i for i in range(len(base)) if base[i] == 'X']
  for b in all_binary_numbers_of_length(len(x_indices)):
    yield int(''.join([
      c if c != 'X' else b[x_indices.index(i)]
      for i, c in enumerate(base)
    ]), 2)

def all_binary_numbers_of_length(length):
  for num in range(2**length):
    yield str(bin(num))[2:].zfill(length)

#####################################################################
if __name__ == "__main__":
  main()

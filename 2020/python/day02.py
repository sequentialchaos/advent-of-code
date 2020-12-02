import re

#####################################################################

def main():
  lines = read_input()
  print(f'part 1: {part_1(lines)}')
  print(f'part 2: {part_2(lines)}')

def part_1(lines):
  return sum(is_valid_1(line) for line in lines)

def part_2(lines):
  return sum(is_valid_2(line) for line in lines)

#####################################################################

def read_input():
  def parse_line(line):
    values = re.match('^(\d+)-(\d+) (\w): (\w+)$', line).groups()
    return (int(values[0]), int(values[1]), values[2], values[3])
  with open('../inputs/02.txt') as f:
    return [parse_line(line) for line in f.readlines()]

def is_valid_1(line):
  low, high, letter, password = line
  letter_count = password.count(letter) 
  return low <= letter_count <= high

def is_valid_2(line):
  low, high, letter, password = line
  return (password[low-1] == letter) ^ (password[high-1] == letter)

#####################################################################

if __name__ == "__main__":
  main()

def main():
  s = read_input()
  print(f'part 1: {part_1(s)}')
  print(f'part 2: {part_2(s)}')

def part_1(s):
  return sum(count_1(group) for group in s)

def part_2(s):
  return sum(count_2(group) for group in s)

#####################################################################

def read_input():
  with open('../inputs/06.txt') as f:
    return [line.split('\n') for line in f.read().split("\n\n")]

def count_1(group):
  sets = [set(g) for g in group]
  return len(set(sets[0]).union(*sets[1:]))

def count_2(group):
  sets = [set(g) for g in group]
  return len(set(sets[0]).intersection(*sets[1:]))

#####################################################################

if __name__ == "__main__":
  main()

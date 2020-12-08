def main():
  s = read_input()
  print(f'part 1: {part_1(s)}')
  print(f'part 2: {part_2(s)}')

def part_1(s):
  acc = 0
  i = 0
  visited_lines = set()
  while i < len(s):
    if i in visited_lines:
      return (1, acc)
    visited_lines.add(i)
    operation, argument = s[i]
    if operation == 'acc':
      acc = acc + argument
      i = i + 1
    elif operation == 'jmp':
      i = i + argument
    else:
      i = i + 1
  return (0, acc)

def part_2(s):
  for i in range(len(s)):
    if s[i][0] == 'jmp':
      s[i][0] = 'nop'
      value = part_1(s)
      if value[0] == 0:
        return value
      s[i][0] = 'jmp'

#####################################################################

def read_input():
  parse = lambda line: [line.split(" ")[0], int(line.split(" ")[1])]
  with open('../inputs/08.txt') as f:
    return [parse(line) for line in f.readlines()]

#####################################################################

if __name__ == "__main__":
  main()

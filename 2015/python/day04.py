import hashlib

#####################################################################

def main():
  s = read_input()
  print(f'part 1: {part_1(s)}')
  print(f'part 2: {part_2(s)}')

def part_1(s):
  n = 0
  while True:
    check = f'{s}{n}'
    if '00000' == hashlib.md5(check.encode()).hexdigest()[:5]:
      return n
    n += 1

def part_2(s):
  n = 0
  while True:
    check = f'{s}{n}'
    if '000000' == hashlib.md5(check.encode()).hexdigest()[:6]:
      return n
    n += 1

#####################################################################

def read_input():
  with open('../inputs/04.txt') as f:
    return f.read().strip()

#####################################################################

if __name__ == "__main__":
  main()

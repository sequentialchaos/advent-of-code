import re
import math
from operator import lshift, rshift, sub, and_, or_

def main():
  s = read_input()
  print(f'part 1: {part_1(s)}')
  print(f'part 2: {part_2(s)}')

def part_1(s):
  return sum(map(len, s)) - sum(map(count_1, s))

def part_2(s):
  return sum(map(count_2, s)) - sum(map(len, s))

#####################################################################
def read_input():
  with open('../inputs/08.txt') as f:
    return [line.strip() for line in f.readlines()]

def count_1(s):
  count = 0
  i = 1
  while i < len(s) - 1:
    if s[i] == '\\':
      if s[i+1] in ['\\', '\"']:
        count += 1
        i += 2
      elif s[i+1] == 'x':
        count += 1
        i += 4
    else:
      count += 1
      i += 1
  return count

def count_2(s):
  count = 6
  i = 1
  while i < len(s) - 1:
    if s[i] == '\\':
      if s[i+1] in ['\\', '\"']:
        count += 4
        i += 2
      elif s[i+1] == 'x':
        count += 5
        i += 4
    else:
      count += 1
      i += 1
  return count
#####################################################################

if __name__ == "__main__":
  main()

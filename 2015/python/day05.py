def main():
  s = read_input()
  print(f'part 1: {part_1(s)}')
  print(f'part 2: {part_2(s)}')

def part_1(s):
  return sum(is_valid_1(string) for string in s)

def part_2(s):
  return sum(is_valid_2(string) for string in s)

#####################################################################

def read_input():
  with open('../inputs/05.txt') as f:
    return f.readlines()

def is_valid_1(s):
  has_three_vowels = 3 <= sum(s.count(c) for c in 'aeiou')
  has_adjacent_duplicates = any(s[i] == s[i+1] for i in range(len(s)-1))
  excludes_certain_strings = all(t not in s for t in ['ab', 'cd', 'pq', 'xy'])
  return has_three_vowels and has_adjacent_duplicates and excludes_certain_strings

def is_valid_2(s):
  has_duplicate_pair = any(len(s.split(s[i]+s[i+1])) >= 3 for i in range(len(s)-1))
  has_separated_pair = any(s[i] == s[i+2] for i in range(len(s)-2))
  return has_duplicate_pair and has_separated_pair

#####################################################################

if __name__ == "__main__":
  main()

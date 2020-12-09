def main():
  s = read_input()
  print(f'part 1: {part_1(s)}')
  print(f'part 2: {part_2(s)}')

def part_1(s):
  for i in range(25, len(s)):
    if not is_valid(s, i):
      return(s[i])

def part_2(s):
  n = part_1(s)
  i = 0
  while i < len(s):
    total = s[i]
    j = i + 1
    while total < n:
      total += s[j]
      j += 1
    if total == n:
      return min(s[i:j]) + max(s[i:j])
    i += 1

#####################################################################
def read_input():
  with open('../inputs/09.txt') as f:
    return [int(line) for line in f.readlines()]

def is_valid(nums, i):
  for j in range(i-25, i-1):
    for k in range(j+1, i):
      if nums[j] + nums[k] == nums[i]:
        return True
  return False

#####################################################################
if __name__ == "__main__":
  main()

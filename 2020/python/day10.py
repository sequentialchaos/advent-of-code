def main():
  s = read_input()
  print(f'part 1: {part_1(s)}')
  print(f'part 2: {part_2(s)}')

def part_1(s):
  s.sort()
  s = [0] + s + [s[len(s)-1]+3]
  d = [s[i+1] - s[i] for i in range(len(s)-1)]
  return d.count(1) * d.count(3)

def part_2(s):
  s.sort()
  s = [0] + s + [s[len(s)-1]+3]
  return count_ways(s)

#####################################################################
def read_input():
  with open('../inputs/10.txt') as f:
    return [int(line) for line in f.readlines()]

def count_ways(s):
  ways = [1 if n in s else 0 for n in range(max(s)+1)]
  for i in range(1, len(s)):
    n = s[i]
    if n == 1:
      ways[n] = ways[n-1]
    elif n == 2:
      ways[n] = ways[n-1] + ways[n-2]
    elif n >= 3:
      ways[n] = ways[n-1] + ways[n-2] + ways[n-3]
  return ways[-1]

# def count(s, i=0):
#   # too slow :(
#   if i >= len(s)-1:
#     return 0
#   if s[i+1] == s[i] + 1:
#     if s[i+2] == s[i] + 2:
#       if s[i+3] == s[i] + 3:
#         return 2 + count(s, i+1) + count(s, i+2) + count(s, i+3)
#       else:
#         return 1 + count(s, i+1) + count(s, i+2)
#     elif s[i+2] == s[i] + 3:
#       return 1 + count(s, i+1) + count(s, i+2)
#     else:
#       return 0 + count(s, i+1)
#   elif s[i+1] == s[i] + 2:
#     if s[i+2] == s[i] + 3:
#       return 1 + count(s, i+1) + count(s, i+2)
#     else:
#       return 0 + count(s, i+1)
#   elif s[i+1] == s[i] + 3:
#     return 0 + count(s, i+1)


#####################################################################
if __name__ == "__main__":
  main()

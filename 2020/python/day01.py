
def main():
  xs = read_input()
  print(f'part 1: {part_1(xs)}')
  print(f'part 2: {part_2(xs)}')

def part_1(xs):
  return [
    xs[i] * (2020 - xs[i])
    for i in range(len(xs)-1)
    if 2020 - xs[i] in xs
  ][0]

def part_2(xs):
  return [
    xs[i] * xs[j] * (2020 - xs[i] - xs[j])
    for i in range(len(xs)-1)
    for j in range(i+1, len(xs))
    if 2020 - xs[i] - xs[j] in xs
  ][0]

#####################################################################

def read_input():
  with open('../inputs/01.txt') as f:
    return [int(line) for line in f.readlines()]

#####################################################################

if __name__ == "__main__":
  main()

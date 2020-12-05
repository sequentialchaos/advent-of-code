
def main():
  s = read_input()
  print(f'part 1: {part_1(s)}')
  print(f'part 2: {part_2(s)}')

def part_1(s):
  return max([get_seat_id(line) for line in s])

def part_2(s):
  seat_ids = [get_seat_id(line) for line in s]
  for seat_id in sorted(seat_ids):
    if (seat_id+1 not in seat_ids) and (seat_id+2 in seat_ids):
      return seat_id+1

#####################################################################

def read_input():
  with open('../inputs/05.txt') as f:
    return [line.strip() for line in f.readlines()]

def decode(s):
  lo, hi = 0, 2**len(s) - 1
  for c in s:
    avg = (lo + hi) // 2
    if c in ['F', 'L']:
      hi = avg
    elif c in ['B', 'R']:
      lo = avg + 1
  return lo
  
def decode_row(s):
  return decode(s[:-3])

def decode_column(s):
  return decode(s[-3:])

def get_seat_id(s):
  return 8 * decode_row(s) + decode_column(s)

#####################################################################

if __name__ == "__main__":
  main()

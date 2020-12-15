def main():
  s = read_input()
  print(f'part 1: {part_1(s)}')
  print(f'part 2: {part_2(s)}')

def part_1(s):
  return simulate_game(s, 2020)

def part_2(s):
  return simulate_game(s, 30_000_000)

def simulate_game(starting_numbers, num_turns):
  sequence = [n for n in starting_numbers]
  last_visited_turn = {n:i for i,n in enumerate(sequence)}
  sequence.append(0)
  starting_turn = len(sequence) - 1
  for turn in range(starting_turn, num_turns):
    spoken_number = sequence[turn]
    if spoken_number not in last_visited_turn:
      next_value = 0
    else:
      next_value = turn - last_visited_turn[spoken_number]
    last_visited_turn[spoken_number] = turn
    sequence.append(next_value)
  return spoken_number

#####################################################################
def read_input():
  with open('../inputs/15.txt') as f:
    return list(map(int, f.read().split(',')))

#####################################################################
if __name__ == "__main__":
  main()

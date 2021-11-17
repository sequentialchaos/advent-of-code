import re


##### MAIN FUNCTION #################################################

def main():
    sequence = parse_input()
    print(f'part 1: {part_1(sequence)}')
    print(f'part 2: {part_2(sequence)}')


##### PART 1 & PART 2 ###############################################

def part_1(sequence):
    sequence_copy = [n for n in sequence]
    for _ in range(40):
        sequence_copy = look_and_say(sequence_copy)
    return len(sequence_copy)


def part_2(sequence):
    sequence_copy = [n for n in sequence]
    for _ in range(50):
        sequence_copy = look_and_say(sequence_copy)
    return len(sequence_copy)

##### PARSE INPUT ###################################################


def parse_input():
    with open('../inputs/10.txt') as f:
        return [int(c) for c in f.read().strip()]


##### UTILITY FUNCTIONS #############################################

def look_and_say(sequence):
    result = []
    count = 1
    for i, n in enumerate(sequence):
        if i == len(sequence) - 1 or n != sequence[i+1]:
            result.extend([count, n])
            count = 1
        else:
            count += 1
    return result


##### CALL main() ###################################################

if __name__ == "__main__":
    main()

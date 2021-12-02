##### MAIN FUNCTION #################################################


def main():
    instructions = parse_input()
    print(f"part 1: {part_1(instructions)}")
    print(f"part 2: {part_2(instructions)}")


##### PART 1 & PART 2 ###############################################


def part_1(instructions):
    position = [0, 0]
    for instruction in instructions:
        position[0] += instruction[0]
        position[1] += instruction[1]
    return position[0] * position[1]


def part_2(instructions):
    aim = 0
    position = [0, 0]
    for instruction in instructions:
        position[0] += instruction[0]
        aim += instruction[1]
        if instruction[0] != 0:
            position[1] += aim * instruction[0]
    return position[0] * position[1]


##### PARSE INPUT ###################################################


def parse_input():
    with open("../inputs/02.txt") as f:
        instructions = []
        for line in f.readlines():
            amount = int(line.split(" ")[1])
            if line[0] == "f":
                instructions.append((amount, 0))
            if line[0] == "d":
                instructions.append((0, amount))
            if line[0] == "u":
                instructions.append((0, -amount))
        return instructions


##### UTILITY FUNCTIONS #############################################


##### CALL main() ###################################################


if __name__ == "__main__":
    main()

##### MAIN FUNCTION #################################################


def main():
    depths = parse_input()
    print(f"part 1: {part_1(depths)}")
    print(f"part 2: {part_2(depths)}")


##### PART 1 & PART 2 ###############################################


def part_1(depths):
    return count_increases(depths)


def part_2(depths):
    return count_increases(rolling_sums(depths, 3))


##### PARSE INPUT ###################################################


def parse_input():
    with open("../inputs/01.txt") as f:
        return list(map(int, f.readlines()))


##### UTILITY FUNCTIONS #############################################


def count_increases(a):
    return sum(a[i + 1] > a[i] for i in range(len(a) - 1))


def rolling_sums(a, length):
    return [sum(a[i : i + length]) for i in range(len(a) - length + 1)]


##### CALL main() ###################################################


if __name__ == "__main__":
    main()

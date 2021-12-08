##### MAIN FUNCTION #################################################


def main():
    ages = parse_input()
    print(f"part 1: {part_1(ages)}")
    print(f"part 2: {part_2(ages)}")


##### PART 1 & PART 2 ###############################################


def part_1(ages):
    return sum(simulate(ages, 80))


def part_2(ages):
    return sum(simulate(ages, 256))


##### PARSE INPUT ###################################################


def parse_input():
    with open("../inputs/06.txt") as f:
        return list(map(int, f.read().split(",")))


##### UTILITY FUNCTIONS #############################################


def simulate(ages, days):
    counts = [ages.count(i) for i in range(8 + 1)]
    for _ in range(days):
        new_counts = [0] * len(counts)
        for age, count in enumerate(counts):
            if age == 0:
                new_counts[6] += count
                new_counts[8] += count
            else:
                new_counts[age - 1] += count
        counts = new_counts
    return counts


##### CALL main() ###################################################


if __name__ == "__main__":
    main()

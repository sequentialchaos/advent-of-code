import re


##### MAIN FUNCTION #################################################


def main():
    lines = parse_input()
    print(f"part 1: {part_1(lines)}")
    print(f"part 2: {part_2(lines)}")


##### PART 1 & PART 2 ###############################################


def part_1(lines):
    return len(overlaps(lines))


def part_2(lines):
    return len(overlaps(lines, diagonal=True))


##### PARSE INPUT ###################################################


def parse_input():
    parse = lambda line: list(map(int, re.findall("\d+", line)))
    with open("../inputs/05.txt") as f:
        return list(map(parse, f.readlines()))


##### UTILITY FUNCTIONS #############################################


def overlaps(lines, diagonal=False):
    overlaps = {}
    for line in lines:
        if line[0] == line[2] or line[1] == line[3]:
            for point in points_in_line(line):
                overlaps.setdefault(point, 0)
                overlaps[point] += 1
        elif diagonal:
            for point in points_in_line(line):
                overlaps.setdefault(point, 0)
                overlaps[point] += 1
    return [p for p in overlaps if overlaps[p] >= 2]


def points_in_line(line):
    x = line[0], line[2]
    y = line[1], line[3]
    if x[0] == x[1]:
        return [(x[0], n) for n in between(y[0], y[1])]
    elif y[0] == y[1]:
        return [(n, y[0]) for n in between(x[0], x[1])]
    else:
        return list(zip(between(x[0], x[1]), between(y[0], y[1])))


def between(a, b):
    if a < b:
        return list(range(a, b + 1))
    else:
        return list(range(b, a + 1))[::-1]


##### CALL main() ###################################################


if __name__ == "__main__":
    main()

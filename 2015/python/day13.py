import re

##### MAIN FUNCTION #################################################


def main():
    names, connections = parse_input()
    print(f"part 1: {part_1(names, connections)}")
    print(f"part 2: {part_2(names, connections)}")


##### PART 1 & PART 2 ###############################################


def part_1(names, connections):
    maximum_happiness = 0
    for permutation in permutations(names):
        happiness = total_happiness(permutation, connections)
        if happiness > maximum_happiness:
            maximum_happiness = happiness
    return maximum_happiness


def part_2(names, connections):
    for name in names:
        connections[("me", name)] = 0
        connections[(name, "me")] = 0
    maximum_happiness = 0
    for permutation in permutations(names + ["me"]):
        happiness = total_happiness(permutation, connections)
        if happiness > maximum_happiness:
            maximum_happiness = happiness
    return maximum_happiness


##### PARSE INPUT ###################################################


def parse_input():
    def parse(line):
        g = re.match("^([A-Z][a-z]+).* (\d+) .*([A-Z][a-z]+)\.$", line).groups()
        if "gain" in line:
            return ((g[0], g[2]), int(g[1]))
        else:
            return ((g[0], g[2]), -int(g[1]))

    with open("../inputs/13.txt") as f:
        names = set()
        connections = {}
        for line in f.readlines():
            connection = parse(line)
            connections[connection[0]] = connection[1]
            names.add(connection[0][0])
            names.add(connection[0][1])
        return list(names), connections


##### UTILITY FUNCTIONS #############################################


def permutations(a):
    if len(a) == 0:
        yield []
        return
    for permutation in permutations(a[1:]):
        for i in range(len(permutation) + 1):
            yield permutation[:i] + a[:1] + permutation[i:]


def total_happiness(arrangement, connections):
    total = 0
    for i, person_a in enumerate(arrangement):
        j = (i + 1) % len(arrangement)
        person_b = arrangement[j]
        happiness_a = connections[(person_a, person_b)]
        happiness_b = connections[(person_b, person_a)]
        total += happiness_a + happiness_b
    return total


##### CALL main() ###################################################

if __name__ == "__main__":
    main()

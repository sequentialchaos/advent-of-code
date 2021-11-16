import re


##### MAIN FUNCTION #################################################

def main():
    distances, locations = parse_input()
    print(f'part 1: {part_1(distances, locations)}')
    print(f'part 2: {part_2(distances, locations)}')


##### PART 1 & PART 2 ###############################################

def part_1(distances, locations):
    routes = permutations(locations)
    shortest_distance, shortest_route = 10**9, []
    for route in routes:
        distance = calculate_distance(route, distances)
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_route = route
    return shortest_distance, shortest_route


def part_2(distances, locations):
    routes = permutations(locations)
    longest_distance, longest_route = 0, []
    for route in routes:
        distance = calculate_distance(route, distances)
        if distance > longest_distance:
            longest_distance = distance
            longest_route = route
    return longest_distance, longest_route


##### PARSE INPUT ###################################################

def parse_input():
    def parse(line):
        g = re.match('(\w+) to (\w+) = (\d+)', line).groups()
        return (g[0], g[1], int(g[2]))

    with open('../inputs/09.txt') as f:
        distances = {}
        locations = set()
        for line in f.readlines():
            start, end, distance = parse(line)
            distances[(start, end)] = distance
            distances[(end, start)] = distance
            locations.add(start)
            locations.add(end)
        return distances, list(locations)


##### UTILITY FUNCTIONS #############################################

def permutations(a):
    if len(a) == 0:
        yield []
        return
    for permutation in permutations(a[1:]):
        for i in range(len(permutation)+1):
            yield permutation[:i] + a[:1] + permutation[i:]


def calculate_distance(route, distances):
    total_distance = 0
    for i, location in enumerate(route[:-1]):
        next_location = route[i+1]
        distance = distances[(location, next_location)]
        total_distance += distance
    return total_distance


##### CALL main() ###################################################

if __name__ == "__main__":
    main()

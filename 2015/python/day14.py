import re

##### MAIN FUNCTION #################################################


def main():
    reindeer = parse_input()
    print(f"part 1: {part_1(reindeer)}")
    print(f"part 2: {part_2(reindeer)}")


##### PART 1 & PART 2 ###############################################


def part_1(reindeer):
    return find_leaders(simulate(reindeer, 2503))


def part_2(reindeer):
    return max(
        points for _, points in simulate(reindeer, 2503, concurrently=True).items()
    )


##### PARSE INPUT ###################################################


def parse_input():
    def parse(line):
        g = re.match("^([A-Z][a-z]+).* (\d+).* (\d+).* (\d+)", line).groups()
        return (g[0], int(g[1]), int(g[2]), int(g[3]))

    reindeer = {}
    with open("../inputs/14.txt") as f:
        for line in f.readlines():
            name, *stats = parse(line)
            reindeer[name] = stats
    return reindeer


##### UTILITY FUNCTIONS #############################################


def step(reindeer, distance, time, state):
    speed, fly_duration, rest_duration = reindeer
    time += 1
    if state == "flying":
        distance += speed
        if time == fly_duration:
            state = "resting"
            time = 0
    else:
        if time == rest_duration:
            state = "flying"
            time = 0
    return [distance, time, state]


def simulate(reindeer, num_seconds, concurrently=False):
    reindeer_states = {name: [0, 0, "flying"] for name in reindeer}
    reindeer_points = {name: 0 for name in reindeer}
    for _ in range(num_seconds):
        for name in reindeer:
            reindeer_states[name] = step(reindeer[name], *reindeer_states[name])
        if concurrently == True:
            leaders, _ = find_leaders(reindeer_states)
            for leader in leaders:
                reindeer_points[leader] += 1
    if concurrently:
        return reindeer_points
    return reindeer_states


def find_leaders(reindeer_states):
    tuples = list(reindeer_states.items())
    distance = max(tuples, key=lambda t: t[1][0])[1][0]
    leaders = [name for name, state in tuples if state[0] == distance]
    return leaders, distance


##### CALL main() ###################################################

if __name__ == "__main__":
    main()

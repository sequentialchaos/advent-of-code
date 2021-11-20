import re

##### MAIN FUNCTION #################################################


def main():
    ingredients = parse_input()
    print(f"part 1: {part_1(ingredients)}")
    print(f"part 2: {part_2(ingredients)}")


##### PART 1 & PART 2 ###############################################


def part_1(ingredients):
    max_score = 0
    for recipe in sums(100):
        score, _ = score_recipe(recipe, ingredients)
        if score > max_score:
            max_score = score
    return max_score


def part_2(ingredients):
    max_score = 0
    for recipe in sums(100):
        score, calories = score_recipe(recipe, ingredients)
        if calories == 500 and score > max_score:
            max_score = score
    return max_score


##### PARSE INPUT ###################################################


def parse_input():
    def parse(line):
        return list(map(int, re.findall("(\-*\d+)", line)))

    with open("../inputs/15.txt") as f:
        return [parse(line) for line in f.readlines()]


##### UTILITY FUNCTIONS #############################################


def score_recipe(recipe, ingredients):
    score = 1
    calories = 0
    for i in range(len(ingredients[0])):
        total = 0
        for j in range(len(ingredients)):
            total += ingredients[j][i] * recipe[j]
        if total < 0:
            total = 0
        if i == len(ingredients[0]) - 1:
            calories = total
        else:
            score *= total
    return score, calories


def sums(n):
    for a in range(n + 1):
        for b in range(n - a + 1):
            for c in range(n - a - b + 1):
                d = n - a - b - c
                yield [a, b, c, d]


##### CALL main() ###################################################

if __name__ == "__main__":
    main()

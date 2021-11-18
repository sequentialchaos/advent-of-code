import re
from json import loads as load_json

##### MAIN FUNCTION #################################################


def main():
    json = parse_input()
    print(f"part 1: {part_1(json)}")
    print(f"part 2: {part_2(json)}")


##### PART 1 & PART 2 ###############################################


def part_1(string):
    return sum(get_numbers(string))


def part_2(string):
    json = load_json(string)
    return sum(value for value in traverse_json(json) if type(value) == int)


##### PARSE INPUT ###################################################


def parse_input():
    with open("../inputs/12.txt") as f:
        return f.read().strip()


##### UTILITY FUNCTIONS #############################################


def get_numbers(string):
    return [int(s) for s in re.findall("\-*\d+", string)]


def traverse_json(json, items=[]):
    if type(json) != dict and type(json) != list:
        items.append(json)
        return
    if type(json) == list:
        for element in json:
            traverse_json(element)
        return
    else:
        if any(json[key] == "red" for key in json):
            return
        for key in json:
            traverse_json(json[key])
    return items


##### CALL main() ###################################################

if __name__ == "__main__":
    main()

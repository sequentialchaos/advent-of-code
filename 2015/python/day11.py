##### MAIN FUNCTION #################################################


def main():
    password = parse_input()
    print(f"part 1: {part_1(password)}")
    print(f"part 2: {part_2(password)}")


##### PART 1 & PART 2 ###############################################


def part_1(password):
    return next_valid_password(password)


def part_2(password):
    for _ in range(2):
        password = next_valid_password(password)
    return password


##### PARSE INPUT ###################################################


def parse_input():
    with open("../inputs/11.txt") as f:
        return f.read().strip()


##### UTILITY FUNCTIONS #############################################


def next_character(character):
    return chr(ord(character) + 1)


def next_password(password):
    if password[-1] != "z":
        return password[:-1] + next_character(password[-1])
    return next_password(password[:-1]) + "a"


def next_valid_password(password):
    if is_valid(password):
        password = next_password(password)
    while not is_valid(password):
        password = next_password(password)
    return password


def passes_rule_1(password):
    for i in range(len(password) - 2):
        ords = [ord(c) for c in password[i : i + 3]]
        if ords[0] == ords[1] - 1 == ords[2] - 2:
            return True
    return False


def passes_rule_2(password):
    return not any(c in ["i", "o", "l"] for c in password)


def passes_rule_3(password):
    found = set()
    for i, c in enumerate(password[:-1]):
        if c == password[i + 1]:
            found.add(c)
    return len(found) >= 2


def is_valid(password):
    return (
        passes_rule_1(password) and passes_rule_2(password) and passes_rule_3(password)
    )


##### CALL main() ###################################################

if __name__ == "__main__":
    main()

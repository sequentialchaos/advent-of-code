import re


##### MAIN FUNCTION #################################################


def main():
    numbers, cards = parse_input()
    print(f"part 1: {part_1(numbers, cards)}")
    print(f"part 2: {part_2(numbers, cards)}")


##### PART 1 & PART 2 ###############################################


def part_1(numbers, cards):
    marks_list = [initial_marks() for _ in range(len(cards))]
    for number in numbers:
        for marks, card in zip(marks_list, cards):
            mark(marks, card, number)
            if has_bingo(marks):
                return number * sum(unmarked_numbers(marks, card))


def part_2(numbers, cards):
    marks_list = [initial_marks() for _ in range(len(cards))]
    for number in numbers:
        for i, (marks, card) in enumerate(zip(marks_list, cards)):
            mark(marks, card, number)
            if all_have_bingo(marks_list):
                return number * sum(unmarked_numbers(marks, card))


##### PARSE INPUT ###################################################


def parse_input():
    parse = lambda line: list(map(int, re.split("\s+", line.strip())))
    with open("../inputs/04.txt") as f:
        lines = f.readlines()
        numbers = list(map(int, lines[0].split(",")))
        cards = []
        for i in range(2, len(lines), 6):
            card = []
            for line in list(map(parse, lines[i : i + 5])):
                for n in line:
                    card.append(n)
            cards.append(card)
        return numbers, cards


##### UTILITY FUNCTIONS #############################################


def initial_marks():
    return [0] * 25


def mark(marks, card, number):
    if number in card:
        i = card.index(number)
        marks[i] = 1


def has_bingo(marks):
    # Check rows.
    for i in range(0, 25, 5):
        if all(marks[i : i + 5]):
            return True
    # Check columns.
    for i in range(5):
        if all(marks[i + n] for n in range(0, 25, 5)):
            return True
    return False


def all_have_bingo(marks_list):
    return all(has_bingo(marks) for marks in marks_list)


def unmarked_numbers(marks, card):
    return [card[i] for i in range(len(card)) if not marks[i]]


##### CALL main() ###################################################


if __name__ == "__main__":
    main()

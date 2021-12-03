##### MAIN FUNCTION #################################################


def main():
    diagnostic_report = parse_input()
    print(f"part 1: {part_1(diagnostic_report)}")
    print(f"part 2: {part_2(diagnostic_report)}")


##### PART 1 & PART 2 ###############################################


def part_1(diagnostic_report):
    return gamma_rate(diagnostic_report) * epsilon_rate(diagnostic_report)


def part_2(diagnostic_report):
    oxygen_generator_rating = rating(diagnostic_report, most_common_bit)
    co2_scrubber_rating = rating(diagnostic_report, least_common_bit)
    return oxygen_generator_rating * co2_scrubber_rating


##### PARSE INPUT ###################################################


def parse_input():
    parse = lambda line: list(map(int, line.strip()))

    with open("../inputs/03.txt") as f:
        return list(map(parse, f.readlines()))


##### UTILITY FUNCTIONS #############################################


def most_common_bit(column, diagnostic_report):
    bits = [row[column] for row in diagnostic_report]
    return max(bits, key=lambda bit: bits.count(bit))


def least_common_bit(column, diagnostic_report):
    return abs(1 - most_common_bit(column, diagnostic_report))


def binary_to_decimal(bits):
    return int("".join(map(str, bits)), 2)


def gamma_rate(diagnostic_report):
    length = len(diagnostic_report[0])
    bits = [most_common_bit(i, diagnostic_report) for i in range(length)]
    return binary_to_decimal(bits)


def epsilon_rate(diagnostic_report):
    length = len(diagnostic_report[0])
    return 2 ** length - gamma_rate(diagnostic_report) - 1


def rating(diagnostic_report, function):
    copy = [entry for entry in diagnostic_report]
    length = len(copy[0])
    for i in range(length):
        bit = function(i, copy)
        j = 0
        while j < len(copy) and len(copy) > 1:
            row = copy[j]
            if row[i] != bit:
                copy.remove(row)
            else:
                j += 1
    return binary_to_decimal(copy[0])


##### CALL main() ###################################################


if __name__ == "__main__":
    main()

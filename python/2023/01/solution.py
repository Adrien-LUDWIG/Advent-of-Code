import sys

spelling_to_integer = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def to_digit(line, index):
    return int(line[index]) if line[index].isdigit() else None


def to_digit_spelling(line, index):
    if line[index].isdigit():
        return int(line[index])

    for spelling, integer in spelling_to_integer.items():
        if line.startswith(spelling, index):
            return integer

    return None


def first_digit(line, to_digit, reverse=False):
    indexes = range(len(line) - 1, -1, -1) if reverse else range(len(line))
    return next(to_digit(line, i) for i in indexes if to_digit(line, i))


def sum_of_calibration_values(input, to_digit):
    total = 0

    for line in input:
        total += first_digit(line, to_digit) * 10 + first_digit(line, to_digit, True)

    return total


if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")
        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    # Part 1
    print(sum_of_calibration_values(input, to_digit))

    # Part 2
    print(sum_of_calibration_values(input, to_digit_spelling))

import sys
from collections import defaultdict
from math import prod


def is_number_finished(input, line_i, char_i):
    # The current char is the last of the line or the next char is not a digit
    return char_i + 1 == len(input[line_i]) or not input[line_i][char_i + 1].isdigit()


def get_numbers(input):
    """Parse numbers, with there starting coordinates, from input."""
    numbers = []
    number = 0

    for line_i, line in enumerate(input):
        for char_i, char in enumerate(line):
            # If we have a digit, form the current number
            if char.isdigit():
                # Add the current digit to the part number
                number = number * 10 + int(char)

                if is_number_finished(input, line_i, char_i):
                    numbers.append((number, line_i, char_i - len(str(number)) + 1))
                    number = 0

    return numbers


def find_symbol(input, line_i, char_i, length):
    """
    Find the symbol around the number starting at (`line_i`, `char_i`) of size `length`.
    Return the symbol and its coordinates if there is any, else None.
    """
    for line_j in range(max(0, line_i - 1), min(len(input), line_i + 2)):
        for char_j in range(
            max(0, char_i - 1), min(len(input[line_i]) - 1, char_i + length + 1)
        ):
            char = input[line_j][char_j]

            if char.isdigit():
                continue
            elif char != ".":
                return char, line_j, char_j

    return None


def get_parts_and_gears(input, numbers):
    """
    Get parts and gears from a list of numbers with there starting coordinates.
    Parts are numbers that touches a symbol.
    Gears are the `*` symbols.
    """
    parts = []
    gears = defaultdict(list)

    for number, line_i, char_i in numbers:
        result = find_symbol(input, line_i, char_i, len(str(number)))

        if result:
            parts.append(number)

            symbol, line_j, char_j = result
            if symbol == "*":
                gears[(line_j, char_j)].append(number)

    return parts, gears


if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    gears = defaultdict(list)
    numbers = get_numbers(input)
    parts, gears = get_parts_and_gears(input, numbers)

    # Part 1
    print(sum(parts))

    # Part 2
    # Keep gears touching 2 parts
    gears_parts = filter(lambda parts: len(parts) == 2, gears.values())
    print(sum(map(prod, gears_parts)))

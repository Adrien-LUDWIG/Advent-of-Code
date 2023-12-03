import sys


def is_symbol(input, line_i, char_i):
    # Check line index before getting the char and checking it
    if not (0 <= line_i and line_i < len(input)):
        return False

    char = input[line_i][char_i]
    return char != "." and not char.isdigit()  # Check char value


def check_symbol_up_down(input, line_i, char_i):
    # Up and down
    return is_symbol(input, line_i - 1, char_i) or is_symbol(input, line_i + 1, char_i)


def check_symbol_side(input, line_i, char_i):
    return is_symbol(input, line_i, char_i) or check_symbol_up_down(
        input, line_i, char_i
    )


def update_sum(part_sum, part, has_symbol):
    # Add up to total if it's a part number (i.e. a symbol is adjacent)
    if has_symbol:
        part_sum += part

    # Reset current variables
    part = 0
    has_symbol = False

    return part_sum, part, has_symbol


if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    part_sum = 0

    part = 0
    has_symbol = False

    for line_i, line in enumerate(input):
        for char_i, char in enumerate(line):
            # If we have a digit, form the current number
            if char.isdigit():
                # For the first_digit, check if there is a symbol on its left
                if part == 0 and char_i > 0:
                    has_symbol |= check_symbol_side(input, line_i, char_i - 1)

                # Add the current digit to the part number
                part = part * 10 + int(char)
                has_symbol |= check_symbol_up_down(input, line_i, char_i)

            # If we are right after a number, check it has a symbol and update
            # the sum
            elif part != 0:
                # No need to increment char_i because we already are on the
                # next char
                has_symbol |= check_symbol_side(input, line_i, char_i)

                part_sum, part, has_symbol = update_sum(part_sum, part, has_symbol)
        part_sum, part, has_symbol = update_sum(part_sum, part, has_symbol)
    part_sum, part, has_symbol = update_sum(part_sum, part, has_symbol)

    # Part 1
    print(part_sum)

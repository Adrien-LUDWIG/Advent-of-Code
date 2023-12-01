import sys

if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")
        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    total = 0

    for line in input:
        # Find first digit
        first_digit_index = 0
        while not line[first_digit_index].isdigit():
            first_digit_index += 1

        total += int(line[first_digit_index]) * 10

        # Find last digit
        last_digit_index = len(line) - 1
        while not line[last_digit_index].isdigit():
            last_digit_index -= 1

        total += int(line[last_digit_index])

    # Part 1
    print(total)

import sys


def find_first_marker(input):
    for i in range(len(input) - 4):
        if len(set(input[i : i + 4])) == 4:
            return i + 4

    print("No marker found")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")
        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    if len(input) != 1:
        print("Input file should contain only one line")
        sys.exit(1)

    input = input[0]

    # Find the first marker (Part 1)
    first_marker = find_first_marker(input)

    print(first_marker)
    print("TODO: Part 2")

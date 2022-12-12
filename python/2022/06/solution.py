import sys


# A marker is a slice of unique characters in a string
def find_first_marker(input, length):
    for i in range(len(input) - length):
        if len(set(input[i : i + length])) == length:
            return i + length

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
    start_of_packet = find_first_marker(input, 4)
    start_of_message = find_first_marker(input, 14)

    print(start_of_packet)
    print(start_of_message)

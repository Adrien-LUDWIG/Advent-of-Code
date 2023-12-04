import sys

if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    points_sum = 0

    for card in input:
        _, numbers = card.split(":")
        winning_numbers, my_numbers = numbers.split("|")
        winning_numbers = set(map(int, winning_numbers.split()))
        my_numbers = set(map(int, my_numbers.split()))
        points = winning_numbers.intersection(my_numbers)

        if len(points):
            points_sum += 2 ** (len(points) - 1)

    # Part 1
    print(points_sum)

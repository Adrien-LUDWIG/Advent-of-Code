import sys


def get_sorted_calories(input):
    # Create a list of each elve's food total calories
    elves_calories = [0]

    for calories in input:
        if calories == "":
            # Add a new elve to the list
            elves_calories.append(0)
        else:
            # Add the calories to the current elve
            elves_calories[-1] += int(calories)

    return sorted(elves_calories)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")
        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    calories = get_sorted_calories(input)

    # Get the biggest elve's total calories
    part1 = calories[-1]

    # Get the sum of the 3 biggest elves' total calories
    part2 = sum(calories[-3:])

    print(part1)
    print(part2)

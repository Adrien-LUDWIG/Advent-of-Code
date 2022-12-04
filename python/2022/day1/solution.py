import sys


def first(input):
    # Create a list of each elve's food total calories
    elves_calories = [0]

    for calories in input:
        if calories == "":
            # Add a new elve to the list
            elves_calories.append(0)
        else:
            # Add the calories to the current elve
            elves_calories[-1] += int(calories)

    # Return the biggest elve's total calories
    return sorted(calories)[-1]


def second(input):
    pass


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")
        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    print(first(input))
    print(second(input))

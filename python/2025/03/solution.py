import sys

from aocd import data, submit


def maxWithIndex(iterable):
    max = 0
    maxIndex = 0

    for index, element in enumerate(iterable):
        element = int(element)
        if element > max:
            max = element
            maxIndex = index

    return (max, maxIndex)


def part1(banks):
    """Solve part 1."""
    totalJoltage = 0

    for bank in banks:
        maxJoltage, maxJoltageIndex = maxWithIndex(map(int, bank))

        if (maxJoltageIndex + 1) < len(bank):
            secondMaxJoltage = max(map(int, bank[maxJoltageIndex + 1 :]))
            bankJoltage = maxJoltage * 10 + secondMaxJoltage
        else:
            secondMaxJoltage = max(map(int, bank[:maxJoltageIndex]))
            bankJoltage = secondMaxJoltage * 10 + maxJoltage

        totalJoltage += int(bankJoltage)

    return totalJoltage


def part2(banks):
    """Solve part 2."""
    pass


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    banks = puzzle_input.splitlines()
    return part1(banks), part2(banks)


if __name__ == "__main__":
    hasArgs = len(sys.argv) > 1
    answer = solve(data if not hasArgs else open(sys.argv[1], "r").read())

    if not hasArgs:
        submit(answer[0] if answer[1] is None else answer[1])

    print(answer)

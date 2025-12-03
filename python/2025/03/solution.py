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


def biggestSubNumber(iterable, digitsCount):
    if len(iterable) == 0:
        return ""

    max, maxIndex = maxWithIndex(iterable)
    max = str(max)
    digitsCount -= 1
    rhs = ""

    if digitsCount == 0:
        return max
    if (maxIndex + 1) < len(iterable):
        rhs = biggestSubNumber(iterable[maxIndex + 1 :], digitsCount)

        if len(rhs) == digitsCount:
            return max + rhs

    lhs = biggestSubNumber(iterable[:maxIndex], digitsCount - len(rhs))
    return lhs + max + rhs


def part1(banks):
    """Solve part 1."""
    totalJoltage = 0

    for bank in banks:
        bankJoltage = biggestSubNumber(list(map(int, bank)), 2)
        print(bankJoltage)
        totalJoltage += int(bankJoltage)
    return totalJoltage


def part2(banks):
    """Solve part 2."""
    totalJoltage = 0

    for bank in banks:
        bankJoltage = biggestSubNumber(list(map(int, bank)), 12)
        print(bankJoltage)
        totalJoltage += int(bankJoltage)
    return totalJoltage


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

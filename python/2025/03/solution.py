import sys

from aocd import data, submit


def maxWithIndex(iterable):
    (max, index) = ("0", 0)

    for i, element in enumerate(iterable):
        if element > max:
            (max, index) = (element, i)

    return (max, index)


def biggestSubNumber(iterable, digitsCount):
    if len(iterable) == 0 or digitsCount <= 0:
        return ""

    maxDigit, maxIndex = maxWithIndex(iterable)
    rhs = biggestSubNumber(iterable[maxIndex + 1 :], digitsCount - 1)
    lhs = biggestSubNumber(iterable[:maxIndex], digitsCount - 1 - len(rhs))

    return lhs + maxDigit + rhs


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    banks = puzzle_input.splitlines()
    totalJoltage1 = 0
    totalJoltage2 = 0

    for bank in banks:
        totalJoltage1 += int(biggestSubNumber(bank, 2))
        totalJoltage2 += int(biggestSubNumber(bank, 12))

    return (totalJoltage1, totalJoltage2)


if __name__ == "__main__":
    hasArgs = len(sys.argv) > 1
    answer = solve(data if not hasArgs else open(sys.argv[1], "r").read())

    if not hasArgs:
        submit(answer[0] if answer[1] is None else answer[1])

    print(answer)

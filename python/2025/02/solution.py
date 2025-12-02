"""AoC 01, 2025: Secret Entrance."""

import sys

from aocd import data, submit


def parse_data(puzzle_input):
    """Parse input."""
    ranges = [list(map(int, range.split("-"))) for range in puzzle_input.split(",")]

    return ranges


def part1(ranges):
    """Solve part 1."""
    fakeIdsSum = 0

    for start, end in ranges:
        for id in range(start, end + 1):
            idString = str(id)
            digitsCount = len(idString)
            mid = digitsCount // 2
            if idString[:mid] == idString[mid:]:
                fakeIdsSum += id

    return fakeIdsSum


def part2(rotations):
    """Solve part 2."""
    pass


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    rotations = parse_data(puzzle_input)
    return part1(rotations), part2(rotations)


if __name__ == "__main__":
    hasArgs = len(sys.argv) > 1
    answer = solve(data if not hasArgs else open(sys.argv[1], "r").read())

    if not hasArgs:
        submit(answer[0] if answer[1] is None else answer[1])

    print(answer)

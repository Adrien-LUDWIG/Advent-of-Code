"""AoC 01, 2025: Secret Entrance."""

import re
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


def part2(ranges):
    """Solve part 2."""

    def isFakeId():
        for i in range(1, mid + 1):
            group = idString[:i]
            pattern = f"^({group}){{2,{digitsCount // len(group)}}}$"
            if re.match(pattern, idString):
                return True
        return False

    fakeIdsSum = 0

    for start, end in ranges:
        for id in range(start, end + 1):
            idString = str(id)
            digitsCount = len(idString)
            mid = digitsCount // 2
            if isFakeId():
                fakeIdsSum += id

    return fakeIdsSum


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    ranges = parse_data(puzzle_input)
    return part1(ranges), part2(ranges)


if __name__ == "__main__":
    hasArgs = len(sys.argv) > 1
    answer = solve(data if not hasArgs else open(sys.argv[1], "r").read())

    if not hasArgs:
        submit(answer[0] if answer[1] is None else answer[1])

    print(answer)

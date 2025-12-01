"""AoC 01, 2025: Secret Entrance."""

import sys

from aocd import data


def parse_data(puzzle_input):
    """Parse input."""
    rotations = [
        (1 if line[0] == "R" else -1, int(line[1:]))
        for line in puzzle_input.splitlines()
    ]

    return rotations


def part1(rotations):
    """Solve part 1."""
    dial = 50
    zeroCount = 0

    for sign, offset in rotations:
        dial = (dial + sign * offset) % 100

        if dial == 0:
            zeroCount += 1

    return zeroCount


def part2(rotations):
    """Solve part 2."""
    dial = 50
    zeroCount = 0

    for sign, offset in rotations:
        previousDial = dial
        zeroCount += offset // 100
        dial = dial + sign * (offset % 100)

        if previousDial != 0 and dial <= 0 or 100 <= dial:
            zeroCount += 1

        dial %= 100

    return zeroCount


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    rotations = parse_data(puzzle_input)
    return part1(rotations), part2(rotations)


if __name__ == "__main__":
    print(solve(data if len(sys.argv) != 2 else open(sys.argv[1], "r").read()))

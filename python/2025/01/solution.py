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


def create_grid(blocks):
    grid = []


def part1(rotations):
    """Solve part 1."""
    print(rotations)
    dial = 50
    zeroCount = 0

    for sign, offset in rotations:
        dial = (dial + sign * offset) % 100

        if dial == 0:
            zeroCount += 1

    return zeroCount


def part2(data):
    """Solve part 2."""


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    blocks = parse_data(puzzle_input)
    return part1(blocks), part2(data)


if __name__ == "__main__":
    print(solve(data if len(sys.argv) != 2 else open(sys.argv[1], "r").read()))

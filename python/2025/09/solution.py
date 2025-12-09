import re
import sys

from aocd import data, submit


def parse_data(puzzle_input):
    coordinates = [
        tuple(map(int, line.split(","))) for line in puzzle_input.splitlines()
    ]

    return coordinates


def part1(coordinates):
    return max(
        (max(x1, x2) - min(x1, x2) + 1) * (max(y1, y2) - min(y1, y2) + 1)
        for i1, (x1, y1) in enumerate(coordinates)
        for i2, (x2, y2) in enumerate(coordinates)
        if i1 < i2
    )


def part2(coordinates):
    pass


def solve(puzzle_input):
    coordinates = parse_data(puzzle_input)
    return part1(coordinates), part2(coordinates)


if __name__ == "__main__":
    hasArgs = len(sys.argv) > 1
    answer = solve(data if not hasArgs else open(sys.argv[1], "r").read())

    if not hasArgs:
        submit(answer[0] if answer[1] is None else answer[1])

    print(answer)

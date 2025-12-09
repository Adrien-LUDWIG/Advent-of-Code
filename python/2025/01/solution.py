import sys

from aocd import data, submit


def parse_data(puzzle_input):
    rotations = [
        (1 if line[0] == "R" else -1, int(line[1:]))
        for line in puzzle_input.splitlines()
    ]

    return rotations


def part1(rotations):
    dial = 50
    zeroCount = 0

    for sign, offset in rotations:
        dial = (dial + sign * offset) % 100

        if dial == 0:
            zeroCount += 1

    return zeroCount


def part2(rotations):
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
    rotations = parse_data(puzzle_input)
    return part1(rotations), part2(rotations)


if __name__ == "__main__":
    hasArgs = len(sys.argv) > 1
    answer = solve(data if not hasArgs else open(sys.argv[1], "r").read())

    if not hasArgs:
        submit(answer[0] if answer[1] is None else answer[1])

    print(answer)

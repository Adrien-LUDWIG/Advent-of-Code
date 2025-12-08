import sys
import bisect
import math

from aocd import data, submit


def parse_data(puzzle_input):
    """Parse input."""
    coordinates = [
        tuple(map(int, line.split(","))) for line in puzzle_input.splitlines()
    ]

    return coordinates


def part1(coordinates):
    """Solve part 1."""
    distances = []

    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            distance = math.dist(coordinates[i], coordinates[j])
            bisect.insort(distances, (distance, i, j))

    print("Sorted")

    circuits = []
    junctionsCircuits = {}
    skipped = 0
    i = 0

    while i < 1000:
        (_, junction1, junction2) = distances[i]
        print(
            (
                junction1,
                junction2,
                # coordinates[junction1],
                # coordinates[junction2],
                # circuits,
                # junctionsCircuits,
            )
        )

        circuit1 = junctionsCircuits.get(junction1, None)
        circuit2 = junctionsCircuits.get(junction2, None)

        if circuit1 is None and circuit2 is None:
            circuits.append(set((junction1, junction2)))
            junctionsCircuits[junction1] = len(circuits) - 1
            junctionsCircuits[junction2] = len(circuits) - 1
        elif circuit1 is None:
            junctionsCircuits[junction1] = circuit2
            circuits[circuit2].add(junction1)
        elif circuit2 is None:
            junctionsCircuits[junction2] = circuit1
            circuits[circuit1].add(junction2)
        elif circuit1 != circuit2:
            fusionedCircuit = circuits[circuit2]
            circuits[circuit2] = set()

            for junction in fusionedCircuit:
                junctionsCircuits[junction] = circuit1
                circuits[circuit1].add(junction)
        else:
            skipped += 1

        i += 1

    circuitsSizes = sorted(map(len, circuits))
    circuitsSizes.reverse()
    # print(circuitsSizes)
    return math.prod(circuitsSizes[:3])


def part2(ranges):
    """Solve part 2."""

    pass


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    coordinates = parse_data(puzzle_input)
    print("Parsed")
    return part1(coordinates), part2(coordinates)


if __name__ == "__main__":
    hasArgs = len(sys.argv) > 1
    answer = solve(data if not hasArgs else open(sys.argv[1], "r").read())

    if not hasArgs:
        submit(answer[0] if answer[1] is None else answer[1])

    print(answer)

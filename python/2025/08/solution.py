import sys
import math

from aocd import data, submit


def parse_data(puzzle_input):
    coordinates = [
        tuple(map(int, line.split(","))) for line in puzzle_input.splitlines()
    ]

    return coordinates


def updateCircuits(i, distances, circuits, junctionsCircuits):
    (_, junction1, junction2) = distances[i]

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
        return False

    return True


def solve(puzzle_input):
    coordinates = parse_data(puzzle_input)
    distances = []

    distances = sorted(
        (math.dist(a, b), i, j)
        for i, a in enumerate(coordinates)
        for j, b in enumerate(coordinates)
        if a < b
    )

    circuits = []
    junctionsCircuits = {}
    skipped = 0
    i = 0
    maxCircuitLength = 0
    part1 = None

    while maxCircuitLength < len(coordinates):
        addedConnection = updateCircuits(i, distances, circuits, junctionsCircuits)

        if not addedConnection:
            skipped += 1

        i += 1
        maxCircuitLength = max(maxCircuitLength, max(map(len, circuits)))

        if i == 1000:
            circuitsSizes = sorted(map(len, circuits))
            circuitsSizes.reverse()
            part1 = math.prod(circuitsSizes[:3])

    (_, junction1, junction2) = distances[i - 1]
    part2 = coordinates[junction1][0] * coordinates[junction2][0]
    return part1, part2


if __name__ == "__main__":
    hasArgs = len(sys.argv) > 1
    answer = solve(data if not hasArgs else open(sys.argv[1], "r").read())

    if not hasArgs:
        submit(answer[0] if answer[1] is None else answer[1])

    print(answer)

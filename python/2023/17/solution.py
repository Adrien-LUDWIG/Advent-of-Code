from aocd import data
from aocd.models import Puzzle
from heapq import heappush, heappop


def dijkstra(map, src, dst, min_consecutive, max_consecutive):
    """
    Finds the shortest path from src to dst making sure direction changes
    only after at least min_consecutive moves and at most max_consectutive
    moves.

    Returns the cost of the path.
    """
    seen = set()

    # Dist, node id, node, direction, consecutive direction count
    heap = [(0, id(src), src, complex(0, 1)), (0, id(src), src, complex(1, 0))]

    while heap:
        distance, _, node, direction = heappop(heap)

        if (node, direction) in seen:
            continue

        if node == dst:
            return distance

        seen.add((node, direction))

        # Go through neighbors
        for delta in (direction * 1j, direction * -1j):
            neighbor = node
            neighbor_distance = distance
            neighbor_count = 0

            # Move
            while neighbor_count < max_consecutive and neighbor + delta in map:
                neighbor += delta
                neighbor_distance += map[neighbor]
                neighbor_count += 1

                if neighbor_count >= min_consecutive:
                    heappush(
                        heap,
                        (
                            neighbor_distance,
                            id(neighbor),  # Hack to avoid comparing complex numbers
                            neighbor,
                            delta,
                        ),
                    )

    raise RuntimeError("Path to destination not found.")


def parse_data(data):
    map = {}
    src, dst = complex(0, 0), None
    for x, line in enumerate(data.splitlines()):
        for y, cost in enumerate(line.strip()):
            map[complex(x, y)] = int(cost)
            dst = complex(x, y)

    return map, src, dst


def part1(map, src, dst):
    return dijkstra(map, src, dst, 1, 3)


def part2(map, src, dst):
    return dijkstra(map, src, dst, 4, 10)


def solve(data):
    map, src, dst = parse_data(data)
    return part1(map, src, dst), part2(map, src, dst)


if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=17)

    for example in puzzle.examples:
        answer_a, answer_b = solve(example.input_data)

        if example.answer_a is not None:
            assert answer_a == int(example.answer_a)

        if example.answer_b is not None:
            assert answer_b == int(example.answer_b)

    print(solve(data))

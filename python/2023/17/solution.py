import sys
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


if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file
    map = {}
    src, dst = complex(0, 0), None
    with open(sys.argv[1]) as f:
        for x, line in enumerate(f.readlines()):
            for y, cost in enumerate(line.strip()):
                map[complex(x, y)] = int(cost)
                dst = complex(x, y)

    # Part 1
    print(dijkstra(map, src, dst, 1, 3))

    # Part 2
    print(dijkstra(map, src, dst, 4, 10))

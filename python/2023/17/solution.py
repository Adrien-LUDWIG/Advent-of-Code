import sys
from heapq import heappush, heappop


def dijkstra(map, src, dst, min_consecutive, max_consecutive):
    seen = set()

    # Dist, node id, node, direction, consecutive direction count
    heap = [(0, id(src), src, complex(1, 0), 0)]

    while heap:
        distance, _, node, direction, count = heappop(heap)

        if (node, direction, count) in seen:
            continue

        if node == dst and count >= min_consecutive:
            return distance

        seen.add((node, direction, count))

        for delta in (direction, direction * 1j, direction * -1j):
            neighbor = node
            neighbor_distance = distance
            neighbor_count = count if delta == direction else 0

            while neighbor + delta in map and neighbor_count < (min_consecutive - 1):
                neighbor += delta
                neighbor_distance += map[neighbor]
                neighbor_count += 1

            neighbor += delta

            if neighbor not in map:
                continue

            neighbor_distance += map[neighbor]
            neighbor_count += 1

            if neighbor_count > max_consecutive:
                continue

            heappush(
                heap,
                (
                    neighbor_distance,
                    id(neighbor),
                    neighbor,
                    delta,
                    neighbor_count,
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

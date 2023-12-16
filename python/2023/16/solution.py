import sys

from collections import defaultdict, deque


def is_inside(position, height, width):
    """Check if a given 2D position  is in a grid reprsented by its height and width."""
    return 0 <= position[0] < height and 0 <= position[1] < width


def count_seen_tiles(layout, start_postion, start_direction):
    """
    Simulate the path of rays in a layout starting from a specific position
    and direction. Returns the count of tiles visited.
    """

    # Keep track of seen tiles, but also direction in which it was visited to
    # avoid loops.
    seen_tiles = defaultdict(set)
    rays = deque([(start_postion, start_direction)])  # position, direction
    height, width = len(layout), len(layout[0])

    # Simulate rays
    while rays:
        position, direction = rays.popleft()
        i, j = position
        delta_i, delta_j = direction

        if not is_inside(position, height, width) or direction in seen_tiles[position]:
            continue

        seen_tiles[position].add(direction)

        # Figure out the new direction (and thus position)
        match layout[i][j]:
            case "-" if delta_i != 0:
                rays.append(((i, j - 1), (0, -1)))
                rays.append(((i, j + 1), (0, 1)))
            case "|" if delta_j != 0:
                rays.append(((i - 1, j), (-1, 0)))
                rays.append(((i + 1, j), (1, 0)))
            case "/":
                delta_i, delta_j = direction = -delta_j, -delta_i
                rays.append(((i + delta_i, j + delta_j), direction))
            case "\\":
                delta_i, delta_j = direction = delta_j, delta_i
                rays.append(((i + delta_i, j + delta_j), direction))
            case _:
                rays.append(((i + delta_i, j + delta_j), direction))

    return len(seen_tiles)


if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        layout = [line.strip() for line in f.readlines()]

    # Part 1
    print(count_seen_tiles(layout, (0, 0), (0, 1)))

    # Part 2
    height, width = len(layout), len(layout[0])
    max_count = 0

    # Test all starting positions
    # Up and down
    for j in range(width):
        max_count = max(max_count, count_seen_tiles(layout, (0, j), (1, 0)))
        max_count = max(max_count, count_seen_tiles(layout, (height - 1, j), (-1, 0)))

    # Left and right
    for i in range(height):
        max_count = max(max_count, count_seen_tiles(layout, (i, 0), (0, 1)))
        max_count = max(max_count, count_seen_tiles(layout, (i, width - 1), (0, -1)))

    print(max_count)

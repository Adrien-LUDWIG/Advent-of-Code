import sys

from collections import defaultdict, deque


class Vec(tuple):
    """Tuples you can add, swap and negate."""

    def __add__(self, other):
        return Vec((self[0] + other[0], self[1] + other[1]))

    def swap(self):
        return Vec(reversed(self))

    def __neg__(self):
        return Vec(-x for x in self)


# Directions
UP = Vec((-1, 0))
DOWN = Vec((1, 0))
LEFT = Vec((0, -1))
RIGHT = Vec((0, 1))


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

        if not is_inside(position, height, width) or direction in seen_tiles[position]:
            continue

        seen_tiles[position].add(direction)

        # Figure out the new direction (and thus position)
        match layout[position[0]][position[1]]:
            case "-" if direction[0] != 0:
                rays.append((position + LEFT, LEFT))
                rays.append((position + RIGHT, RIGHT))
            case "|" if direction[1] != 0:
                rays.append((position + UP, UP))
                rays.append((position + DOWN, DOWN))
            case "/":
                direction = -direction.swap()
                rays.append((position + direction, direction))
            case "\\":
                direction = direction.swap()
                rays.append((position + direction, direction))
            case _:
                rays.append((position + direction, direction))

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
    print(count_seen_tiles(layout, Vec((0, 0)), RIGHT))

    # Part 2
    height, width = len(layout), len(layout[0])
    max_count = 0

    # Test all starting positions
    # Up and down
    for j in range(width):
        max_count = max(max_count, count_seen_tiles(layout, Vec((height - 1, j)), UP))
        max_count = max(max_count, count_seen_tiles(layout, Vec((0, j)), DOWN))

    # Left and right
    for i in range(height):
        max_count = max(max_count, count_seen_tiles(layout, Vec((i, width - 1)), LEFT))
        max_count = max(max_count, count_seen_tiles(layout, Vec((i, 0)), RIGHT))

    print(max_count)

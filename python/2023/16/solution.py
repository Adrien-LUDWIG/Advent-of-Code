import sys

from collections import defaultdict, deque


def count_energized_tiles(layout):
    energized_tiles = defaultdict(set)
    rays = deque()
    rays.append(((0, 0), (0, 1)))  # position, direction

    while rays:
        position, direction = rays.popleft()
        i, j = position
        delta_i, delta_j = direction

        if not (0 <= i < len(layout)) or not (0 <= j < len(layout[0])):
            continue

        if direction in energized_tiles[position]:
            continue

        energized_tiles[position].add(direction)

        match layout[i][j]:
            case ".":
                rays.append(((i + delta_i, j + delta_j), direction))
            case "-":
                if delta_i == 0:
                    rays.append(((i, j + delta_j), direction))
                else:
                    rays.append(((i, j - 1), (0, -1)))
                    rays.append(((i, j + 1), (0, 1)))
            case "|":
                if delta_j == 0:
                    rays.append(((i + delta_i, j), direction))
                else:
                    rays.append(((i - 1, j), (-1, 0)))
                    rays.append(((i + 1, j), (1, 0)))
            case "/":
                if direction == (0, 1):
                    delta_i, delta_j = direction = (-1, 0)
                elif direction == (-1, 0):
                    delta_i, delta_j = direction = (0, 1)
                elif direction == (0, -1):
                    delta_i, delta_j = direction = (1, 0)
                elif direction == (1, 0):
                    delta_i, delta_j = direction = (0, -1)
                rays.append(((i + delta_i, j + delta_j), direction))
            case "\\":
                if direction == (0, 1):
                    delta_i, delta_j = direction = (1, 0)
                elif direction == (1, 0):
                    delta_i, delta_j = direction = (0, 1)
                elif direction == (0, -1):
                    delta_i, delta_j = direction = (-1, 0)
                elif direction == (-1, 0):
                    delta_i, delta_j = direction = (0, -1)
                rays.append(((i + delta_i, j + delta_j), direction))

    return len(energized_tiles)


if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        layout = [line.strip() for line in f.readlines()]

    print(count_energized_tiles(layout))

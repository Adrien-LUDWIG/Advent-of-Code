import sys
from scipy.ndimage import binary_fill_holes

DIRECTIONS = {
    "U": complex(-1, 0),
    "D": complex(1, 0),
    "L": complex(0, -1),
    "R": complex(0, 1),
}


def parse_data(data):
    directions, counts, colors = list(zip(*(row.split() for row in data.splitlines())))
    directions = list(map(lambda direction: DIRECTIONS[direction], directions))
    counts = list(map(int, counts))

    return directions, counts, colors


def get_boundaries(directions, counts):
    position = complex(0, 0)

    min_x, min_y = 0, 0
    max_x, max_y = 0, 0

    for direction, count in zip(directions, counts):
        for _ in range(count):
            position += direction

        min_x = min(min_x, position.real)
        min_y = min(min_y, position.imag)
        max_x = max(max_x, position.real)
        max_y = max(max_y, position.imag)

    return (
        complex(abs(min_x), abs(min_y)),  # Starting position
        int(max_x - min_x) + 1,  # Height of the map
        int(max_y - min_y) + 1,  # Width of th map
    )


def create_map(directions, counts, start, height, width):
    map = [[False for _ in range(width + 2)] for _ in range(height + 2)]

    position = start

    for direction, count in zip(directions, counts):
        for _ in range(count):
            map[int(position.real)][int(position.imag)] = True
            position += direction

    return map


def lake_area(map):
    return binary_fill_holes(map).astype(int).sum()


def print_map(map):
    print("Map:")
    print("\n".join("".join("#" if cell else "." for cell in line) for line in map))


if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    directions, counts, _ = parse_data(open(sys.argv[1]).read())
    start, height, width = get_boundaries(directions, counts)
    map = create_map(directions, counts, start, height, width)

    # Part 1
    print(lake_area(map))

import sys
from scipy.ndimage import binary_fill_holes
from itertools import pairwise

DIRECTIONS = {
    "R": complex(0, 1),
    "D": complex(1, 0),
    "L": complex(0, -1),
    "U": complex(-1, 0),
}

DIRECTIONS_LIST = list(DIRECTIONS.values())


def parse_data(data):
    directions, counts, colors = list(zip(*(row.split() for row in data.splitlines())))
    directions = list(map(lambda direction: DIRECTIONS[direction], directions))
    counts = list(map(int, counts))

    return directions, counts, colors


def print_map(map):
    print("Map:")
    print("\n".join("".join("#" if cell else "." for cell in line) for line in map))


def polygon_area(points):
    area = 0

    for point1, point2 in pairwise(points):
        x1, y1 = int(point1.real), int(point1.imag)
        x2, y2 = int(point2.real), int(point2.imag)

        area += (y1 + y2) * (x1 - x2)

    return abs(area) // 2


def get_points(directions, counts):
    position = complex(0, 0)
    points = [position]

    for direction, count in zip(directions, counts):
        position += direction * count
        points.append(position)

    return points


def lake_area(directions, counts):
    return polygon_area(get_points(directions, counts)) + sum(counts) // 2 + 1


def part1(directions, counts):
    return lake_area(directions, counts)


def part2(colors):
    directions = list(map(lambda color: DIRECTIONS_LIST[int(color[7])], colors))
    counts = list(map(lambda color: int(color[2:7], 16), colors))
    return lake_area(directions, counts)


if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    directions, counts, colors = parse_data(open(sys.argv[1]).read())

    print(part1(directions, counts))
    print(part2(colors))

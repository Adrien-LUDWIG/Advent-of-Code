import sys


def expand(image):
    for index in range(len(image) - 1, -1, -1):
        if all(cell == "." for cell in image[index]):
            image.insert(index, image[index])

    image_transposed = list(zip(*image))

    for index in range(len(image_transposed) - 1, -1, -1):
        if all(cell == "." for cell in image_transposed[index]):
            image_transposed.insert(index, image_transposed[index])

    return list(zip(*image_transposed))


if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    expanded = expand(input)

    galaxies_positions = [
        (i, j)
        for i in range(len(expanded))
        for j in range(len(expanded[0]))
        if expanded[i][j] == "#"
    ]

    total_distance = 0
    for i in range(len(galaxies_positions)):
        for j in range(i + 1, len(galaxies_positions)):
            x1, y1 = galaxies_positions[i]
            x2, y2 = galaxies_positions[j]
            total_distance += abs(x1 - x2) + abs(y1 - y2)

    print(total_distance)

import sys


def get_fake_indices(image, expansion):
    fake_row_indices = []
    fake_index = 0

    for index in range(len(image)):
        if all(cell == "." for cell in image[index]):
            fake_index += expansion
        else:
            fake_index += 1
        fake_row_indices.append(fake_index)

    return fake_row_indices


def expand(image, expansion):
    fake_row_indices = get_fake_indices(image, expansion)
    fake_col_indices = get_fake_indices(list(zip(*image)), expansion)

    return fake_row_indices, fake_col_indices


def distance_sum(image, expansion):
    fake_row_indices, fake_col_indices = expand(image, expansion)

    galaxies_positions = [
        (fake_i, fake_j)
        for real_i, fake_i in enumerate(fake_row_indices)
        for real_j, fake_j in enumerate(fake_col_indices)
        if image[real_i][real_j] == "#"
    ]

    total_distance = 0
    for i in range(len(galaxies_positions)):
        for j in range(i + 1, len(galaxies_positions)):
            x1, y1 = galaxies_positions[i]
            x2, y2 = galaxies_positions[j]
            total_distance += abs(x1 - x2) + abs(y1 - y2)

    return total_distance


if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        image = [line.strip() for line in f.readlines()]

    # Part 1
    print(distance_sum(image, expansion=2))

    # Part 2
    print(distance_sum(image, expansion=1000000))

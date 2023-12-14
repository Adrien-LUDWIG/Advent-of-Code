import sys


def compute_load(reflector):
    """Compute the load on the reflector support beams when tilting north."""

    height, width = len(reflector), len(reflector[0])

    total_load = 0

    for j in range(width):
        rock_load = height

        for i in range(height):
            if reflector[i][j] == "O":
                total_load += rock_load
                rock_load -= 1
            elif reflector[i][j] == "#":
                rock_load = height - i - 1

    return total_load


if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        reflector = list(map(str.strip, f.readlines()))

    print(compute_load(reflector))

import sys


def tilt_north_south(reflector, north=True):
    """Given a reflector state, return the new state after tilting it north."""

    height, width = len(reflector), len(reflector[0])
    step = 1 if north else -1

    for j in range(width):
        rock_destination = 0 if north else height - 1

        for i in range(height) if north else range(height - 1, -1, -1):
            if reflector[i][j] == "O":
                # Swap rock with its destination
                reflector[i][j], reflector[rock_destination][j] = (
                    reflector[rock_destination][j],
                    reflector[i][j],
                )

                rock_destination += step
            elif reflector[i][j] == "#":
                rock_destination = i + step

    return reflector


def transpose(matrix):
    return list(list(row) for row in zip(*matrix))


def tilt_west_east(reflector, west=True):
    """Given a reflector state, return the new state after tilting it west."""
    return transpose(tilt_north_south(transpose(reflector), north=west))


def spin_cycle(reflector):
    reflector = tilt_north_south(reflector, north=True)
    reflector = tilt_west_east(reflector, west=True)
    reflector = tilt_north_south(reflector, north=False)
    reflector = tilt_west_east(reflector, west=False)

    return reflector


def spin_n_times(reflector, n):
    """Spin n times."""

    def to_tuple(matrix):
        return tuple(tuple(row) for row in matrix)

    seen = {}

    for i in range(n):
        seen[to_tuple(reflector)] = i
        reflector = spin_cycle(reflector)

        if to_tuple(reflector) in seen:
            cycle_start = seen[to_tuple(reflector)]
            cycle_length = i + 1 - cycle_start

            for _ in range((n - cycle_start) % cycle_length):
                reflector = spin_cycle(reflector)
            break

    return reflector


def compute_load(reflector):
    """Compute the load on the reflector support beams given the reflector state."""

    h, w = len(reflector), len(reflector[0])  # height, width
    return sum(h - i for j in range(w) for i in range(h) if reflector[i][j] == "O")


if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        reflector = list(map(list, map(str.strip, f.readlines())))

    # Part 1
    print(compute_load(tilt_north_south(reflector)))

    # Part 2
    print(compute_load(spin_n_times(reflector, 1_000_000_000)))

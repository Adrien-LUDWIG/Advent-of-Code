import sys


def tilt_north(reflector):
    """Given a reflector state, return the new state after tilting it north."""

    height, width = len(reflector), len(reflector[0])

    for j in range(width):
        rock_destination = 0

        for i in range(height):
            if reflector[i][j] == "O":
                # Swap rock with its destination
                reflector[i][j], reflector[rock_destination][j] = (
                    reflector[rock_destination][j],
                    reflector[i][j],
                )

                rock_destination += 1
            elif reflector[i][j] == "#":
                rock_destination = i + 1

    return reflector


def tilt_south(reflector):
    """Given a reflector state, return the new state after tilting it south."""

    height, width = len(reflector), len(reflector[0])

    for j in range(width):
        rock_destination = height - 1

        for i in range(height - 1, -1, -1):
            if reflector[i][j] == "O":
                # Swap rock with its destination
                reflector[i][j], reflector[rock_destination][j] = (
                    reflector[rock_destination][j],
                    reflector[i][j],
                )

                rock_destination -= 1
            elif reflector[i][j] == "#":
                rock_destination = i - 1

    return reflector


def tilt_west(reflector):
    """Given a reflector state, return the new state after tilting it west."""

    height, width = len(reflector), len(reflector[0])

    for i in range(height):
        rock_destination = 0

        for j in range(width):
            if reflector[i][j] == "O":
                # Swap rock with its destination
                reflector[i][j], reflector[i][rock_destination] = (
                    reflector[i][rock_destination],
                    reflector[i][j],
                )

                rock_destination += 1
            elif reflector[i][j] == "#":
                rock_destination = j + 1

    return reflector


def tilt_east(reflector):
    """Given a reflector state, return the new state after tilting it east."""

    height, width = len(reflector), len(reflector[0])

    for i in range(height):
        rock_destination = width - 1

        for j in range(width - 1, -1, -1):
            if reflector[i][j] == "O":
                # Swap rock with its destination
                reflector[i][j], reflector[i][rock_destination] = (
                    reflector[i][rock_destination],
                    reflector[i][j],
                )

                rock_destination -= 1
            elif reflector[i][j] == "#":
                rock_destination = j - 1

    return reflector


def spin_cycle(reflector):
    reflector = tilt_north(reflector)
    reflector = tilt_west(reflector)
    reflector = tilt_south(reflector)
    reflector = tilt_east(reflector)

    return reflector


def spin_n_times(reflector, n):
    """Spin n times."""

    def to_tuple(matrix):
        return tuple(tuple(row) for row in matrix)

    seen = {}
    count = 0

    while count < n and to_tuple(reflector) not in seen:
        seen[to_tuple(reflector)] = count
        count += 1

        reflector = spin_cycle(reflector)

    if count == n:
        return reflector

    cycle_start = seen[to_tuple(reflector)]
    cycle_length = count - cycle_start

    for _ in range((n - cycle_start) % cycle_length):
        reflector = spin_cycle(reflector)

    return reflector


def compute_load(reflector):
    """Compute the load on the reflector support beams given the reflector state."""

    height, width = len(reflector), len(reflector[0])

    total_load = 0

    for j in range(width):
        for i in range(height):
            if reflector[i][j] == "O":
                total_load += height - i

    return total_load


if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        reflector = list(map(list, map(str.strip, f.readlines())))

    # Part 1
    print(compute_load(tilt_north(reflector)))

    # Part 2
    print(compute_load(spin_n_times(reflector, 1_000_000_000)))

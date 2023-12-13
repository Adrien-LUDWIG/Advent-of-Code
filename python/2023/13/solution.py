import sys

HORIZONTAL_COEF = 100


def find_symmetry(map):
    for i in range(len(map) - 1):
        if map[i] != map[i + 1]:
            continue
        for offset in range(min(i + 1, len(map) - 1 - i)):
            if map[i - offset] != map[i + 1 + offset]:
                break
        else:
            return i + 1
    return None


if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        maps = f.read().split("\n\n")
        maps = [[line.strip() for line in map.split("\n") if line] for map in maps]

    summary = 0

    for map in maps:
        hor_sym_index = find_symmetry(map)

        if hor_sym_index:
            summary += hor_sym_index * HORIZONTAL_COEF
        else:
            summary += find_symmetry(list(zip(*map)))

    print(summary)

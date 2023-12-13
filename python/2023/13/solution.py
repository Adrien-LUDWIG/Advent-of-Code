import sys

HORIZONTAL_COEF = 100


def count_differences(list1, list2):
    return sum(x != y for x, y in zip(list1, list2))


def find_symmetry(map):
    for i in range(len(map) - 1):
        if map[i] != map[i + 1]:
            continue
        for offset in range(1, min(i + 1, len(map) - 1 - i)):
            if map[i - offset] != map[i + 1 + offset]:
                break
        else:
            return i + 1
    return None


def find_symmetry_smudge(map):
    for i in range(len(map) - 1):
        diff_count = count_differences(map[i], map[i + 1])
        if diff_count > 1:
            continue

        found_smudge = diff_count == 1

        for offset in range(1, min(i + 1, len(map) - 1 - i)):
            found_smudge |= diff_count == 1
            diff_count = count_differences(map[i - offset], map[i + 1 + offset])
            if diff_count > 1 or (found_smudge and diff_count != 0):
                break
        else:
            found_smudge |= diff_count == 1
            if found_smudge:
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
        map_transposed = list(zip(*map))
        hor_sym_index = find_symmetry_smudge(map)

        if hor_sym_index:
            summary += hor_sym_index * HORIZONTAL_COEF
        else:
            ver_sym_index = find_symmetry_smudge(map_transposed)
            summary += ver_sym_index

    print(summary)

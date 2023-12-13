import sys

HORIZONTAL_COEF = 100


def count_differences(list1, list2):
    return sum(x != y for x, y in zip(list1, list2))


def find_symmetry(map):
    """Finds a horizontal line of symmetry in a 2D matrix."""
    for i in range(len(map) - 1):
        # Check consecutive lines for equality.
        if map[i] != map[i + 1]:
            continue

        # If we found 2 identical consecutive lines, check every other pair of
        # lines along this symmetry for equality, until we reach the end of the
        # matrix on ether side of the symmetry axis.
        for offset in range(1, min(i + 1, len(map) - 1 - i)):
            if map[i - offset] != map[i + 1 + offset]:
                # If we found different lines break and keep looking for another
                # symmetry axis.
                break
        else:
            # Else, we found a symmetry axis.
            return i + 1
    return None


def find_symmetry_with_smudge(map):
    """Finds a horizontal line of symmetry in a 2D matrix that has exactly one smudge."""
    for i in range(len(map) - 1):
        diff_count = count_differences(map[i], map[i + 1])

        # If we have more than one difference, one smudge is not the cause.
        if diff_count > 1:
            continue

        # Keep track if we already found a smudge, as we should have exactly one.
        found_smudge = diff_count == 1

        # If we found consecutive lines similar (equal or one smudge), check
        # every other pair of lines along this symmetry for similarity (equal or
        # one smudge), until we reach the end of the matrix on ether side of the
        # symmetry axis.
        for offset in range(1, min(i + 1, len(map) - 1 - i)):
            # As should have exactly one smudge, we must keep track of the
            # difference we overlooked.
            found_smudge |= diff_count == 1
            diff_count = count_differences(map[i - offset], map[i + 1 + offset])

            # If we have multiple differences or if we have one difference but
            # we already corrected a smudge, keep looking for a symmetry line.
            if diff_count > 1 or (found_smudge and diff_count != 0):
                break
        else:
            # We should have found a smudge, if it's the case return the index
            # of the symmetry line.
            found_smudge |= diff_count == 1
            if found_smudge:
                return i + 1
            # Else, keep looking for a symmetry line with a smudge.
    return None


def summarize(maps, find_symmetry_function):
    """
    Given a list of maps and a function to find the symmetry axis of a map.
    Summarize the results depending on the orientation of each axis and it's index.

    This function assumes that there is always a symmetry axis.
    """
    summary = 0

    for map in maps:
        if hor_sym_index := find_symmetry_function(map):
            summary += hor_sym_index * HORIZONTAL_COEF
        else:
            # If there is no horizontal symmetry, transpose the matrix to look
            # for vertical symmetry.
            map_transposed = list(zip(*map))
            summary += find_symmetry_function(map_transposed)

    return summary


if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        maps = f.read().split("\n\n")
        maps = [[line.strip() for line in map.splitlines() if line] for map in maps]

    # Part 1
    print(summarize(maps, find_symmetry))

    # Part 2
    print(summarize(maps, find_symmetry_with_smudge))

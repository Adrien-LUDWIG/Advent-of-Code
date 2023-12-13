import sys
from math import ceil, floor, sqrt


def solve_polynomial(a, b, c):
    # calculate the discriminant
    delta = sqrt(b**2 - 4 * a * c)
    # find two roots
    root1 = (-b + delta) / (2 * a)
    root2 = (-b - delta) / (2 * a)
    return root1, root2


def compute_possibilities(times, distances):
    possibilities_product = 1

    for time, distance in zip(times, distances):
        root1, root2 = solve_polynomial(-1, time, -distance)
        possibilities_product *= floor(root2) - ceil(root1) + 1

    return possibilities_product


if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        times, distances = f.read().splitlines()

    times = times.split()[1:]
    distances = distances.split()[1:]

    # Part 1
    print(compute_possibilities(map(int, times), map(int, distances)))

    # Part 2
    big_time = int("".join(times))
    big_distance = int("".join(distances))

    print(compute_possibilities([big_time], [big_distance]))

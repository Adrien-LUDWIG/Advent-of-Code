import sys


def hash_function(step):
    result = 0

    for char in step:
        result += ord(char)
        result *= 17
        result %= 256

    return result


if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        steps = f.read().strip().split(",")

    print(sum(map(hash_function, steps)))

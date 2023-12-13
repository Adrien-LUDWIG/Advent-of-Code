import sys


def steps_stack(seq):
    """
    Given a sequence, create a stack of sequences, each sequence being the
    steps between the elements of the previous sequence, until the sequence is
    only zeros.
    """
    stack = [seq]

    while any(seq):
        stack.append([rhs - lhs for lhs, rhs in zip(seq[:-1], seq[1:])])
        seq = stack[-1]

    return stack


def predict(seq):
    """Predict the previous and next values of a given sequence."""
    steps = steps_stack(seq)

    prev = 0
    next = 0

    while steps:
        seq = steps.pop()
        prev = seq[0] - prev
        next = seq[-1] + next

    return prev, next


if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        input = [list(map(int, line.split())) for line in f.readlines()]

    sum_previous = 0
    sum_next = 0

    for seq in input:
        prev, next = predict(seq)
        sum_previous += prev
        sum_next += next

    # Part 1
    print(sum_next)

    # Part 2
    print(sum_previous)

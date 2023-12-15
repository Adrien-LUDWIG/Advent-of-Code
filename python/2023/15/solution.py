import sys


def hash_function(step):
    """Given a string returns a number between 0 and 255."""
    result = 0

    for char in step:
        result += ord(char)
        result *= 17
        result %= 256

    return result


def hashmap(steps):
    """Holiday ASCII String Helper Manual Arrangement Procedure

    Given some steps encoded as "<label>(=|-)[<focus_length>]", organize the
    lens in the 256 available boxes.
    """
    boxes = [{} for _ in range(256)]

    for step in steps:
        if step[-1] == "-":
            label = step[:-1]
            boxes[hash_function(label)].pop(label, None)
        else:  # step[-2] == "=" and step[-1] is a digit
            label = step[:-2]
            focal_length = int(step[-1])
            boxes[hash_function(label)][label] = focal_length

    return boxes


def focusing_power(boxes):
    """
    Given a list of boxes containing ordered lenses, return the focusing power
    of sequences of boxes.
    """
    total_focusing_power = 0

    for box_index, box in enumerate(boxes, start=1):
        for label_index, lens in enumerate(box.items(), start=1):
            _, focus_length = lens
            total_focusing_power += box_index * label_index * focus_length

    return total_focusing_power


if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        steps = f.read().strip().split(",")

    # Part 1
    print(sum(map(hash_function, steps)))

    # Part 2
    print(focusing_power(hashmap(steps)))

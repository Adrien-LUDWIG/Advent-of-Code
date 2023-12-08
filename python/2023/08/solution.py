import math
import sys
import re


def is_ZZZ(node):
    return node == "ZZZ"


def is_xxZ(node):
    return node[-1] == "Z"


def path_length(instructions, network, node, is_dst):
    """Find the length of the path separating node from its destination."""
    count = 0
    index = 0

    while not is_dst(node):
        count += 1
        node = network[node][instructions[index]]
        index = (index + 1) % len(instructions)

    return count


if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        # Get instructions and turn them into digits to use them easily later
        instructions = f.readline().strip()
        instructions = instructions.replace("L", "0").replace("R", "1")
        instructions = list(map(int, instructions))

        # Discard the blank line
        f.readline()

        # Get the network as a dictionary
        network = {}
        for line in f.readlines():
            src, dst0, dst1 = re.findall("\w+", line.strip())
            network[src] = (dst0, dst1)

    # Part 1
    print(path_length(instructions, network, "AAA", is_ZZZ))

    # Part 2
    nodes = [node for node in network if node[-1] == "A"]
    # Find the number of instructions needed to arrive at destination for each node
    paths_lengths = [path_length(instructions, network, node, is_xxZ) for node in nodes]
    # Deduce the number of instructions needed to arrive at destination for all nodes
    print(math.lcm(*paths_lengths))

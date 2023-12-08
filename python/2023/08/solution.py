import sys
import re

if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        instructions = f.readline().strip()
        instructions = instructions.replace("L", "0").replace("R", "1")
        instructions = list(map(int, instructions))

        f.readline()

        network = {}

        for line in f.readlines():
            src, dst0, dst1 = re.findall("\w+", line.strip())
            network[src] = (dst0, dst1)

    count = 0
    index = 0
    node = "AAA"

    while node != "ZZZ":
        count += 1

        node = network[node][instructions[index]]

        index = (index + 1) % len(instructions)

    print(count)

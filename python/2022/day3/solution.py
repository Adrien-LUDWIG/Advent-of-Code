import sys

def item_to_priority(item):
  if item.islower():
      return ord(item) - ord('a') + 1
  else:
      return ord(item) - ord('A') + 27


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")
        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    # Part 1: Sum of the priorities of the items badly packed
    priorities_sum = 0

    for rucksack in input:
        # Split the rucksack in two compartments
        partition = len(rucksack) // 2
        compartment1 = set(rucksack[:partition])
        compartment2 = set(rucksack[partition:])

        # Get the item badly packed
        item_badly_packed = compartment1.intersection(compartment2)
        item_badly_packed = list(item_badly_packed)[0]

        # Add the priority of the item badly packed to the sum
        priorities_sum += item_to_priority(item_badly_packed)


    print(priorities_sum)
    print("TODO part 2")

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
    priorities_sum_1 = 0

    # Part 2: Sum of the priorities of the badges
    priorities_sum_2 = 0

    for rucksack in input:
        # Split the rucksack in two compartments
        partition = len(rucksack) // 2
        compartment1 = set(rucksack[:partition])
        compartment2 = set(rucksack[partition:])

        # Get the item badly packed
        item_badly_packed = compartment1.intersection(compartment2)
        item_badly_packed = list(item_badly_packed)[0]

        # Add the priority of the item badly packed to the sum
        priorities_sum_1 += item_to_priority(item_badly_packed)

    for i in range(0, len(input), 3):
        rucksack1 = set(input[i])
        rucksack2 = set(input[i + 1])
        rucksack3 = set(input[i + 2])

        # Get the badge
        badge = rucksack1.intersection(rucksack2, rucksack3)
        badge = list(badge)[0]


        # Add the priority of the badge to the sum
        priorities_sum_2 += item_to_priority(badge)

    print(priorities_sum_1)
    print(priorities_sum_2)

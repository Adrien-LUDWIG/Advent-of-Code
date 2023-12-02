import sys
from re import split
from collections import defaultdict
from math import prod

CUBES_COUNT = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")
        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    game_ids_sum = 0
    powers_sum = 0

    # For each line looking like : "Game 1: 42 red, 51 green; 69 blue"
    for line in input:
        # Parse line -----------------------------------------------------------
        # Split as : ["Game", "1", "42", "red", "51", "green", "69", "blue"]
        line = split("[:;, ]+", line)

        game_id = int(line[1])
        counts = list(map(int, line[2::2]))
        colors = line[3::2]

        # Part 1 ---------------------------------------------------------------
        # Check every count is inferior or equal to the actual count of cubes
        if all(count <= CUBES_COUNT[color] for count, color in zip(counts, colors)):
            game_ids_sum += game_id

        # Part 2 ---------------------------------------------------------------
        max_color_count = defaultdict(int)

        for color, count in zip(colors, counts):
            max_color_count[color] = max(max_color_count[color], count)

        powers_sum += prod(max_color_count.values())

    # Part 1
    print(game_ids_sum)

    # Part 2
    print(powers_sum)

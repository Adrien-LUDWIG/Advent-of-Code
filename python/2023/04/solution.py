import sys

if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    # Part 1
    points_sum = 0

    # Part 2
    cards_count = [1] * len(input)
    total_nb_cards = 0

    for index, card in enumerate(input):
        _, numbers = card.split(":")
        winning_numbers, my_numbers = numbers.split("|")
        winning_numbers = set(map(int, winning_numbers.split()))
        my_numbers = set(map(int, my_numbers.split()))
        my_winning_numbers_count = len(winning_numbers.intersection(my_numbers))

        # Part 1
        if my_winning_numbers_count:
            points_sum += 2 ** (my_winning_numbers_count - 1)

        # Part 2
        total_nb_cards += cards_count[index]
        for offset in range(1, my_winning_numbers_count + 1):
            cards_count[index + offset] += cards_count[index]

    # Part 1
    print(points_sum)

    # Part 2
    print(total_nb_cards)

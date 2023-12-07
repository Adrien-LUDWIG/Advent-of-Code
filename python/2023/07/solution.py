import sys
from collections import Counter

CARD_TO_RANK = {card: index for index, card in enumerate("23456789TJQKA")}


def key_hands_bids(hand_bid):
    hand, _ = hand_bid

    cards_count = list(zip(*Counter(hand).most_common()))[1]
    cards_ranks = [CARD_TO_RANK[card] for card in hand]

    return (cards_count, cards_ranks)


if __name__ == "__main__":
    # Check args and indicate usage if necessary
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")

        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        input = f.read().split()

    hands = input[::2]
    bids = map(int, input[1::2])

    hands_sorted, bids_sorted = zip(*sorted(zip(hands, bids), key=key_hands_bids))

    # Part 1
    print(sum([(rank + 1) * bid for rank, bid in enumerate(bids_sorted)]))

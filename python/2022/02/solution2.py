""" This solution casts the letters to indexes and uses a matrix to calculate the score. 
    Whereas the previous solution used dictionaries of all the possible combinations.
"""

import sys

# Round outcomes scores
LOSE = 0
DRAW = 3
WIN = 6

ROCK = 1
PAPER = 2
SCISSORS = 3

# Matrix of second player's score based on each player's choice
# Row is the first player's choice, column is the second player's choice, value is the score
player2_score = [
    # Rock, Paper, Scissors
    [DRAW, WIN, LOSE],  # Rock
    [LOSE, DRAW, WIN],  # Paper
    [WIN, LOSE, DRAW],  # Scissors
]


# Matrix of second player's choice based on first player's choice and the round outcome
# Row is the first player's choice, column is the round outcome, value is the second player's choice
player2_choice = [
    # Lose, Draw, Win
    [SCISSORS, ROCK, PAPER],  # Rock
    [ROCK, PAPER, SCISSORS],  # Paper
    [PAPER, SCISSORS, ROCK],  # Scissors
]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")
        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    # Calculate the total score for each part (with different rules)
    score1 = 0
    score2 = 0

    # For each round, add the score to the total score
    for line in input:
        # Split the line into characters
        player1_choice, _, player2_tips = line

        # Convert the characters to indexes
        # A = 0, B = 1, C = 2
        # X = 0, Y = 1, Z = 2
        player1_choice = ord(player1_choice) - ord("A")
        player2_tips = ord(player2_tips) - ord("X")

        # Part 1: second player's tips is the choice of the second player
        # Increment the total score based on the round outcome and the second player's choice
        score1 += player2_score[player1_choice][player2_tips] + player2_tips + 1

        # Part 2: second player's tips is the outcome of the round
        # Increment the total score based on the scond player's choice and the round outcome
        score2 += player2_choice[player1_choice][player2_tips] + player2_tips * 3

    print(score1)
    print(score2)

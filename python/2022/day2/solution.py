import sys

# Round outcomes scores
LOSE = 0
DRAW = 3
WIN = 6

A = X = 1  # Rock
B = Y = 2  # Paper
C = Z = 3  # Scissors

# Create a dictionary of all possible rounds and their scores
POSSIBLE_ROUNDS = {
    "A X": X + DRAW, # Rock vs Rock
    "A Y": Y + WIN, # Rock vs Paper
    "A Z": Z + LOSE, # Rock vs Scissors
    "B X": X + LOSE, # Paper vs Rock
    "B Y": Y + DRAW, # Paper vs Paper
    "B Z": Z + WIN, # Paper vs Scissors 
    "C X": X + WIN, # Scissors vs Rock
    "C Y": Y + LOSE, # Scissors vs Paper
    "C Z": Z + DRAW, # Scissors vs Scissors
}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")
        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    # Part 1: Calculate the total score
    score = 0

    # For each round, add the score to the total score
    for line in input:
        score += POSSIBLE_ROUNDS[line]

    print(score)
    print("TODO part 2")

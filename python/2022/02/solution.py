import sys

# Round outcomes scores
LOSE = 0
DRAW = 3
WIN = 6

ROCK = 1
PAPER = 2
SCISSORS = 3

# Create a dictionary of all possible rounds and their scores for part 1
# X = Rock, Y = Paper, Z = Scissors
POSSIBLE_ROUNDS_1 = {
    "A X": ROCK + DRAW, # Rock vs Rock
    "A Y": PAPER + WIN, # Rock vs Paper
    "A Z": SCISSORS + LOSE, # Rock vs Scissors
    "B X": ROCK + LOSE, # Paper vs Rock
    "B Y": PAPER + DRAW, # Paper vs Paper
    "B Z": SCISSORS + WIN, # Paper vs Scissors 
    "C X": ROCK + WIN, # Scissors vs Rock
    "C Y": PAPER + LOSE, # Scissors vs Paper
    "C Z": SCISSORS + DRAW, # Scissors vs Scissors
}

# Create a dictionary of all possible rounds and their scores for part 2
POSSIBLE_ROUNDS_2 = {
    "A X": LOSE + SCISSORS, # Lose against Rock, play Scissors
    "A Y": DRAW + ROCK, # Draw against Rock, play Rock
    "A Z": WIN + PAPER, # Win against Rock, play Paper
    "B X": LOSE + ROCK, # Lose against Paper, play Rock
    "B Y": DRAW + PAPER, # Draw against Paper, play Paper
    "B Z": WIN + SCISSORS, # Win against Paper, play Scissors
    "C X": LOSE + PAPER, # Lose against Scissors, play Paper
    "C Y": DRAW + SCISSORS, # Draw against Scissors, play Scissors
    "C Z": WIN + ROCK, # Win against Scissors, play Rock
}


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
        score1 += POSSIBLE_ROUNDS_1[line]
        score2 += POSSIBLE_ROUNDS_2[line]

    print(score1)
    print(score2)

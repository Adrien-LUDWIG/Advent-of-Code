import sys

# Represent direction left and up
BACKWARD = -1
# Represent direction right and down
FORWARD = 1

# Check if the tree at index i is visible from the border
# We need to check left and right only because we are on a line
def is_visible_1D(list, i):
    return max(list[:i]) < list[i] or list[i] > max(list[i + 1 :])


# Check if the tree at (i, j) is visible from the border
# We need to check left, right, up and down
# We can split the problem in 2 1D problems by checking the line and the column
def is_visible_2D(array, i, j):
    line = array[i]
    column = [array[k][j] for k in range(len(array))]
    return is_visible_1D(line, j) or is_visible_1D(column, i)


# Count the number of trees visible from this tree in a given direction
def scenic_score_direction(list, i, step):
    score = step

    # Loop on the trees in the given direction until we find a tree higher or equal to the current one
    while 0 <= i + score + step < len(list) and list[i + score] < list[i]:
        score += step

    # Return the absolute value of the score because step can be negative
    return abs(score)


# Count the number of trees visible from this tree in all directions
def scenic_score_tree(array, i, j):
    line = array[i]
    column = [array[k][j] for k in range(len(array))]

    left = scenic_score_direction(line, j, BACKWARD)
    right = scenic_score_direction(line, j, FORWARD)
    up = scenic_score_direction(column, i, BACKWARD)
    down = scenic_score_direction(column, i, FORWARD)

    return left * right * up * down


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")
        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    # Split lines into characters and cast characters to int
    array = [[int(char) for char in line] for line in input]

    height = len(array)
    width = len(array[0])

    # Part 1: Count the number of trees visible from the border

    # Count the trees constituting the border which are always visible
    # Subtract 4 because we don't want to count the corners twice
    visible_count = height * 2 + width * 2 - 4

    # Part 2: Get the highest scenic score of all the trees

    # We can ignore the border trees because they have a scenic score of 0
    max_scenic_score = 0

    # Loop on the inner trees, count the visible ones and get the highest scenic score
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            # If the tree is visible, increment the counter
            visible_count += int(is_visible_2D(array, i, j))

            # Compute the scenic score of the tree and update the max if needed
            max_scenic_score = max(max_scenic_score, scenic_score_tree(array, i, j))

    print(visible_count)
    print(max_scenic_score)

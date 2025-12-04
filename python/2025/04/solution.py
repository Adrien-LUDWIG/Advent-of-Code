import sys

from aocd import data, submit


def getAccessibleRolls(grid):
    height = len(grid)
    width = len(grid[0])
    accessibleRollsCoordinates = set()

    for row in range(height):
        for column in range(width):
            isRoll = grid[row][column] == "@"
            if not isRoll:
                continue

            adjacentRollsCount = 0

            for i in range(row - 1, row + 2):
                for j in range(column - 1, column + 2):
                    isSelf = i == row and j == column
                    isOutOfBound = i < 0 or i >= height or j < 0 or j >= width

                    if isSelf or isOutOfBound:
                        continue

                    isRoll = grid[i][j] == "@"
                    adjacentRollsCount += isRoll

            isAccessible = adjacentRollsCount < 4
            if isAccessible:
                accessibleRollsCoordinates.add((row, column))

    return accessibleRollsCoordinates


def part1(grid):
    return len(getAccessibleRolls(grid))


def part2(grid):
    totalAccessibleRollsCount = 0
    accessibleRollsCoordinates = getAccessibleRolls(grid)

    while len(accessibleRollsCoordinates) > 0:
        totalAccessibleRollsCount += len(accessibleRollsCoordinates)

        for row, column in accessibleRollsCoordinates:
            grid[row][column] = "."

        accessibleRollsCoordinates = getAccessibleRolls(grid)

    return totalAccessibleRollsCount


def solve(puzzle_input):
    grid = list(map(list, puzzle_input.splitlines()))

    return part1(grid), part2(grid)


if __name__ == "__main__":
    hasArgs = len(sys.argv) > 1
    answer = solve(data if not hasArgs else open(sys.argv[1], "r").read())

    if not hasArgs:
        submit(answer[0] if answer[1] is None else answer[1])

    print(answer)

# Solved on smartphone using Pydroid

# TODO: Load input
input = <input>

PIPE_DIRECTIONS = {
    "|": [(-1, 0), (1, 0)],  # Up and down
    "-": [(0, -1), (0, 1)],  # Left and right
    "F": [(1, 0), (0, 1)],
    "7": [(1, 0), (0, -1)],
    "J": [(-1, 0), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "S": [(-1, 0), (1, 0), (0, -1), (0, 1)],
}

# For each direction, map to the compatible pipes if you look in this direction
DIRECTION_PIPES = {
    (-1, 0): "|F7S",
    (1, 0): "|JLS",
    (0, -1): "-FLS",
    (0, 1): "-7JS",
}


def find_next_pipe(input, curr_row, curr_col, last_row, last_col):
    for offset_row, offset_col in PIPE_DIRECTIONS[input[curr_row][curr_col]]:
        next_row, next_col = curr_row + offset_row, curr_col + offset_col

        if (next_row, next_col) == (last_row, last_col) or not (
            0 <= next_row < len(input) and 0 <= next_col < len(input[0])
        ):
            continue
        next_pipe = input[next_row][next_col]
        if next_pipe in DIRECTION_PIPES[(offset_row, offset_col)]:
            return next_row, next_col, curr_row, curr_col
    raise ValueError(
        f"No compatible pipe in neighbors at position ({curr_row}, {curr_col}) but ({last_row}, {last_col})."
    )


scan = [row.strip() for row in input.split("\n")]

start_row = 0
while not "S" in scan[start_row]:
    start_row += 1

start_col = scan[start_row].index("S")

curr_row, curr_col, last_row, last_col = find_next_pipe(
    scan, start_row, start_col, None, None
)
count = 1

while scan[curr_row][curr_col] != "S":
    curr_row, curr_col, last_row, last_col = find_next_pipe(
        scan, curr_row, curr_col, last_row, last_col
    )
    count += 1

print(count // 2)

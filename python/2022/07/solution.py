import sys

LS_LINE = ["$", "ls"]
LITTLE_DIR_THRESHOLD = 100000
TOTAL_DISK_SPACE = 70000000
NEEDED_FREE_SPACE = 30000000


# Recursive function that visits all the subdirectories and returns the total size of the current directory
def depth_first_search(input, index, directories_sizes):
    directory_size = 0

    if index >= len(input):
        directories_sizes.append(directory_size)
        return index

    tokens = input[index]

    if len(tokens) < 2:
        print("A line should have at least 2 tokens but received:")
        print(tokens)
        sys.exit(1)

    if tokens != LS_LINE:
        print("Every recursion should start by a 'ls' command but received: ")
        print(tokens)
        sys.exit(1)

    index += 1
    tokens = input[index]

    # Loop on the files and directories shown by ls. Sum the files size.
    while tokens[0] != "$":
        if tokens[0] != "dir":  # If is file
            directory_size += int(tokens[0])

        index += 1

        if index >= len(input):
            directories_sizes.append(directory_size)
            return index

        tokens = input[index]

    if len(tokens) != 3:
        print("Invalid arguments for 'cd'. Tokens: ")
        print(tokens)
        exit(1)

    # Loop on the subdirectories, recursively call depth_first_search and sum the subdirectories size
    while index < len(input) and tokens[1] == "cd" and tokens[2] != "..":
        index = depth_first_search(input, index + 1, directories_sizes)

        directory_size += directories_sizes[-1]

        if index >= len(input):
            directories_sizes.append(directory_size)
            return index

        tokens = input[index]

    if tokens[2] != "..":
        print("We visited all the subdirectories, expected 'cd ..' but received: ")
        print(tokens)
        sys.exit(1)

    directories_sizes.append(directory_size)
    return index + 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input file>")
        sys.exit(1)

    # Read input file and split into stripped lines
    with open(sys.argv[1]) as f:
        input = [line.strip() for line in f.readlines()]

    input = [line.split(" ") for line in input]

    first_line = input[0]
    if len(first_line) != 3 or first_line[:2] != ["$", "cd"]:
        print("First line should be a 'cd' command but received: ")
        print(first_line)
        sys.exit(1)

    directories_sizes = []
    depth_first_search(input, 1, directories_sizes)

    # Part 1
    little_directories_total_size = 0

    # Part 2
    # The biggest directory is the last one we pushed in the list
    biggest_directory_size = directories_sizes[-1]
    # Compute the size of the littlest directory to delete to free the needed space
    size_to_free = NEEDED_FREE_SPACE - (TOTAL_DISK_SPACE - biggest_directory_size)
    littlest_directory_too_big = biggest_directory_size

    for directory_size in directories_sizes:

        # We take into account the directory size only if it is under the given threshold
        if directory_size <= LITTLE_DIR_THRESHOLD:
            little_directories_total_size += directory_size

        # We take into account the directory size only if it is under the given threshold
        # and if it is the littlest directory that is too big
        if (
            size_to_free > 0
            and directory_size >= size_to_free
            and directory_size < littlest_directory_too_big
        ):
            littlest_directory_too_big = directory_size

    print(little_directories_total_size)
    print(littlest_directory_too_big)

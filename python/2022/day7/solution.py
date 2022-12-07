import sys

LS_LINE = ["$", "ls"]
LITTLE_DIR_THRESHOLD = 100000

# We take into account the directory size only if it is under the given threshold
def check_directory_size(directory_size):
    if directory_size <= LITTLE_DIR_THRESHOLD:
        return directory_size
    else:
        return 0


# Recursive function that visits all the subdirectories and returns the total size of the current directory
def depth_first_search(input, index):
    directory_size = 0
    little_directories_total_size = 0

    if index >= len(input):
        return directory_size, index, little_directories_total_size

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
            return directory_size, index, check_directory_size(directory_size)

        tokens = input[index]

    if len(tokens) != 3:
        print("Invalid arguments for 'cd'. Tokens: ")
        print(tokens)
        exit(1)

    # Loop on the subdirectories, recursively call depth_first_search and sum the subdirectories size
    while index < len(input) and tokens[1] == "cd" and tokens[2] != "..":
        subdirectory_size, index, little_subdirectories_total_size = depth_first_search(
            input, index + 1
        )

        directory_size += subdirectory_size
        little_directories_total_size += little_subdirectories_total_size

        if index >= len(input):
            little_directories_total_size += check_directory_size(directory_size)
            return directory_size, index, little_directories_total_size

        tokens = input[index]

    if tokens[2] != "..":
        print("We visited all the subdirectories, expected 'cd ..' but received: ")
        print(tokens)
        sys.exit(1)

    little_directories_total_size += check_directory_size(directory_size)
    return directory_size, index + 1, little_directories_total_size


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

    total_size, _, little_directories_total_size = depth_first_search(input, 1)

    print(little_directories_total_size)
    print("TODO Part 2")

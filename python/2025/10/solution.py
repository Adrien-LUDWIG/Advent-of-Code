import re
import sys

from aocd import data, submit


def parse_data(puzzle_input):
    lineRegex = re.compile("^\[(.*)\] (.*) ({.*})$")

    machines = []

    for line in puzzle_input.splitlines():
        (indicator, buttons, joltage) = lineRegex.match(line).groups()

        indicator = sum(2**i for i, light in enumerate(indicator) if light == "#")

        buttons = [
            set(map(int, button[1:-1].split(","))) for button in buttons.split(" ")
        ]
        buttons = [sum(2**n for n in button) for button in buttons]
        buttons.sort()

        machines.append((indicator, buttons, joltage))

    return machines


def count_presses(machine):
    """
    First idea create all combinations.
    Misses the fact that 2 and 2 presses is 4 presses not 3.
    """
    indicator, buttons, _ = machine
    print("indicator:", indicator)

    pressesCount = 1

    while True:
        print("buttons:", buttons)
        for button in buttons:
            if button == indicator:
                print("presses:", pressesCount)
                return pressesCount

        buttons += [
            button1 ^ button2
            for button1 in buttons
            for button2 in buttons
            if button1 < button2
        ]
        buttons = list(set(buttons))
        buttons.sort()
        pressesCount += 1


def count_presses2(machine):
    """
    Second idea, creates all the states after pressing all combinations of buttons.
    """
    indicator, buttons, _ = machine

    states = [indicator]
    pressesCount = 0

    while True:
        pressesCount += 1
        newStates = []

        for state in states:
            for button in buttons:
                newState = state ^ button

                if newState == 0:
                    return pressesCount

                newStates.append(newState)

        states = newStates


def part1(machines):
    return sum(count_presses2(machine) for machine in machines)


def part2(machines):
    pass


def solve(puzzle_input):
    machines = parse_data(puzzle_input)
    return part1(machines), part2(machines)


if __name__ == "__main__":
    hasArgs = len(sys.argv) > 1
    answer = solve(data if not hasArgs else open(sys.argv[1], "r").read())

    if not hasArgs:
        submit(answer[0] if answer[1] is None else answer[1])

    print(answer)

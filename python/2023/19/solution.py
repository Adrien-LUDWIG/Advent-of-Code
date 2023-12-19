import operator
import sys
import re
from aocd import data
from copy import deepcopy
from math import prod

CATEGORIES = {
    "x": 0,
    "m": 1,
    "a": 2,
    "s": 3,
}

OPERATIONS = {
    ">": operator.gt,
    "<": operator.lt,
}


def parse_rules(rules_str):
    rules = {}

    for rule in rules_str.splitlines():
        rule = re.findall("[^{,}]+", rule)
        name, tests, default = rule[0], rule[1:-1], rule[-1]
        tests = [
            (CATEGORIES[category], OPERATIONS[operation], int(value), next_rule)
            for test in tests
            for category, operation, value, next_rule in re.findall(
                "(\w+)([<>])(\d+):(\w+)", test
            )
        ]

        rules[name] = tests + [(None, None, None, default)]

    return rules


def parse_data(data):
    rules, parts = data.split("\n\n")
    rules = parse_rules(rules)
    parts = list(
        map(lambda part: list(map(int, re.findall("\d+", part))), parts.splitlines())
    )
    return rules, parts


def part1(rules, parts):
    total = 0

    for part in parts:
        rule = "in"

        while rule != "A" and rule != "R":
            for test in rules[rule]:
                category, operation, value, next_rule = test

                if not operation:
                    rule = next_rule
                    break
                if operation(part[category], value):
                    rule = next_rule
                    break

        if rule == "A":
            total += sum(part)

    return total


def update_combination(combination, test, invert=False):
    category, operation, value, _ = test

    if invert:
        if operation == operator.gt:
            operation = operator.lt
            value += 1
        else:  # operation == operator.lt
            operation = operator.gt
            value -= 1

    if operation == operator.gt:
        combination[category][0] = max(combination[category][0], value + 1)
    else:  # operation == operator.lt
        combination[category][1] = min(combination[category][1], value - 1)

    return combination


def accepted_combinations(rules):
    combinations = []

    def dfs(rule, combination):
        if rule == "A":
            combinations.append(combination)
            return
        if rule == "R":
            return

        reversed_combination = deepcopy(combination)

        for test in rules[rule][:-1]:
            _, _, _, next_rule = test
            new_combination = deepcopy(reversed_combination)
            new_combination = update_combination(new_combination, test)
            dfs(next_rule, new_combination)

            reversed_combination = update_combination(reversed_combination, test, True)

        # Default
        dfs(rules[rule][-1][-1], reversed_combination)

    dfs("in", [[1, 4000] for _ in range(4)])
    return combinations


def part2(rules):
    combinations = accepted_combinations(rules)
    return sum(
        [
            prod([max - min + 1 for min, max in combination])
            for combination in combinations
        ]
    )


def solve(data):
    rules, parts = parse_data(data)
    return part1(rules, parts), part2(rules)


if __name__ == "__main__":
    print(solve(data if len(sys.argv) != 2 else open(sys.argv[1], "r").read()))

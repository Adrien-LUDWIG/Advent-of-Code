import operator
import sys
import re
from aocd import data

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


def part2(data):
    pass


def solve(data):
    rules, parts = parse_data(data)

    return part1(rules, parts), part2(data)


if __name__ == "__main__":
    print(solve(data if len(sys.argv) != 2 else open(sys.argv[1], "r").read()))

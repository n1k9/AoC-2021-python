#!/bin/env python
# Advent of Code 2021 Day 10
from python.utils import read_file_str as read_file

ERR_POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
OPENER_CHARS = "([{<"
CLOSER_CHARS = ")]}>"


def check_chuncks(chunks):
    stack = []
    errors = []
    for c in chunks:
        if c in OPENER_CHARS:
            stack.append(c)
        else:
            last_opener_char = stack.pop()
            index_last_closer_char = CLOSER_CHARS.index(c)
            if last_opener_char != OPENER_CHARS[index_last_closer_char]:
                errors.append(c)
    return errors


def part1(nav_cmd: list) -> int:
    error_points = 0
    for r in nav_cmd:
        errs = check_chuncks(r)
        if errs:
            error_points += ERR_POINTS[errs[0]]
    return error_points


if __name__ == "__main__":
    input_test = [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]"
    ]

    assert part1(input_test) == 26397

    input_data = read_file('day10_data.txt')
    print(f"PART1: {part1(input_data)}")

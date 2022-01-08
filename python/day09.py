# Advent of Code 2021 Day 9 first
from python.utils import read_file


def str_to_int_list(s): return [int(c) for c in s]


def lower_cross_neighbors(hm, r: int, c: int) -> bool:
    p = hm[r][c]
    n = hm[r-1][c] if r-1 >= 0 else 9
    s = hm[r+1][c] if r+1 < len(hm) else 9
    w = hm[r][c-1] if c-1 >= 0 else 9
    e = hm[r][c+1] if c+1 < len(hm[r]) else 9
    return p < min(n, s, w, e)


def part1(map: list[list[int]]):
    risk_level = 0
    for r in range(len(map)):
        for c in range(len(map[r])):
            risk_level += map[r][c] + 1 if lower_cross_neighbors(map, r, c) else 0
    return risk_level


if __name__ == "__main__":
    test_input = [
        str_to_int_list("2199943210"),
        str_to_int_list("3987894921"),
        str_to_int_list("9856789892"),
        str_to_int_list("8767896789"),
        str_to_int_list("9899965678")
    ]
    assert part1(test_input) == 15

    input = read_file("day09_data.txt")
    print(f"Part1: {part1(test_input)}")

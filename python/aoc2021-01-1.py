#!/bin/env python
# 

def count_inc(measures:list) -> int:
    count = 0
    for i in range(1, len(measures)):
        if measures[i] > measures[i-1]:
            count += 1
        print(f"{measures[i]} > {measures[i-1]} --> {measures[i] > measures[i-1]} | {count}")
    return count

def read_file(filename:str) -> list:
    with open(filename, 'r') as f:
        return list(map(int, f.readlines()))

if __name__ == "__main__":
    measures_list = read_file('aoc2021-01_data01.txt')
    # measures_list = read_file('aoc2021-01_test01.txt')
    print(count_inc(measures_list))

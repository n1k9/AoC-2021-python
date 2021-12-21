#!/bin/env python
# Advent of Code 2021 Day 3 first



def gamma_epsilon_rate(dagnostics):
    ones = [0]*len(dagnostics[0])
    n_recs = len(dagnostics)
    for n in dagnostics:
        signal = [int(x) for x in n.strip()]
        ones = map(sum, zip(ones, signal))
    # zeros = map(lambda a,b: a-b, [n_recs]*5, ones)
    # print (ones, zeros)
    gamma = [n > n_recs/2 for n in ones]
    epsilon = [not g for g in gamma]
    exps =  [2**i for i in range(len(gamma)-1, -1, -1)]

    print(gamma, epsilon, exps, sep='\n')

    gamma_r = sum(map(lambda c,e: int(c)*e, gamma, exps))
    epsilon_r = sum(map(lambda c,e: int(c)*e, epsilon, exps))
    return gamma_r, epsilon_r

def read_file(filename:str) -> list:
    with open(filename, 'r') as f:
        return f.readlines()


if __name__ == "__main__":
    dagnostics = read_file('aoc2021-03_data.txt')
    # dagnostics = read_file('aoc2021-03_test.txt')
    gamma, epsilon = gamma_epsilon_rate(dagnostics)

    power_consuption = gamma * epsilon
    print (power_consuption)

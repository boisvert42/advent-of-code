#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 22:13:54 2021

@author: aboisvert
"""

_input = '''
5251578181
6158452313
1818578571
3844615143
6857251244
2375817613
8883514435
2321265735
2857275182
4821156644
'''.strip().split('\n')

# Test input
"""
_input = '''
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''.strip().split('\n')
"""

# Convert to dictionary
input2 = dict()
for i, row in enumerate(_input):
    for j, char in enumerate(row):
        input2[(i, j)] = int(char)

def adjacent_indices(i, j):
    ret = set()
    for i1 in range(i-1, i+2):
        for j1 in range(j-1, j+2):
            if i == i1 and j == j1:
                continue
            try:
                input2[(i1, j1)]
                ret.add((i1, j1))
            except:
                pass
    return ret

num_rows = len(_input)
num_cols = len(_input[0])

#%% Part 1

"""
The energy level of each octopus is a value between 0 and 9. Here, the top-left octopus has an energy level of 5, the bottom-right one has an energy level of 6, and so on.

You can model the energy levels and flashes of light in steps. During a single step, the following occurs:

First, the energy level of each octopus increases by 1.
Then, any octopus with an energy level greater than 9 flashes. This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than 9, it also flashes. This process continues as long as new octopuses keep having their energy level increased beyond 9. (An octopus can only flash at most once per step.)
Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.
"""
import itertools

def iteration(input3):
    num_flashes = 0
    output = input3.copy()
    # First, increase the energy level of all octopi by 1
    for i, j in itertools.product(range(num_rows), range(num_cols)):
        output[(i, j)] += 1
        
    # Then, any octopus with an energy level greater than 9 flashes.
    new_flashes = 1e6
    while new_flashes > 0:
        new_flashes = 0
        for i, j in itertools.product(range(num_rows), range(num_cols)):
            if output[(i, j)] > 9:
                num_flashes += 1
                new_flashes += 1
                output[(i, j)] = 0
                for adj in adjacent_indices(i, j):
                    if output[adj] != 0:
                        output[adj] += 1
    return num_flashes, output


num_flashes = 0
input3 = input2.copy()
for _ in range(100):
    nf, input3 = iteration(input3)
    num_flashes += nf
    
print(num_flashes)

#%% Part 2: What is the first step during which all octopuses flash?

not_all_flashes = True
ctr = 0
input3 = input2.copy()
while not_all_flashes:
    ctr += 1
    nf, input3 = iteration(input3)
    if nf == num_rows * num_cols:
        not_all_flashes = False
        
print(ctr)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 22:15:41 2021

@author: aboisvert
"""

"""
The sea floor is getting steeper. Maybe the sleigh keys got carried this way?

A massive school of glowing lanternfish swims past. They must spawn quickly to reach such large numbers - maybe exponentially quickly? You should model their growth rate to be sure.

Although you know nothing about this specific species of lanternfish, you make some guesses about their attributes. Surely, each lanternfish creates a new lanternfish once every 7 days.

However, this process isn't necessarily synchronized between every lanternfish - one lanternfish might have 2 days left until it creates another lanternfish, while another might have 4. So, you can model each fish as a single number that represents the number of days until it creates a new lanternfish.

Furthermore, you reason, a new lanternfish would surely need slightly longer before it's capable of producing more lanternfish: two more days for its first cycle.
"""

input = '''
4,2,4,1,5,1,2,2,4,1,1,2,2,2,4,4,1,2,1,1,4,1,2,1,2,2,2,2,5,2,2,3,1,4,4,4,1,2,3,4,4,5,4,3,5,1,2,5,1,1,5,5,1,4,4,5,1,3,1,4,5,5,5,4,1,2,3,4,2,1,2,1,2,2,1,5,5,1,1,1,1,5,2,2,2,4,2,4,2,4,2,1,2,1,2,4,2,4,1,3,5,5,2,4,4,2,2,2,2,3,3,2,1,1,1,1,4,3,2,5,4,3,5,3,1,5,5,2,4,1,1,2,1,3,5,1,5,3,1,3,1,4,5,1,1,3,2,1,1,1,5,2,1,2,4,2,3,3,2,3,5,1,5,1,2,1,5,2,4,1,2,4,4,1,5,1,1,5,2,2,5,5,3,1,2,2,1,1,4,1,5,4,5,5,2,2,1,1,2,5,4,3,2,2,5,4,2,5,4,4,2,3,1,1,1,5,5,4,5,3,2,5,3,4,5,1,4,1,1,3,4,4,1,1,5,1,4,1,2,1,4,1,1,3,1,5,2,5,1,5,2,5,2,5,4,1,1,4,4,2,3,1,5,2,5,1,5,2,1,1,1,2,1,1,1,4,4,5,4,4,1,4,2,2,2,5,3,2,4,4,5,5,1,1,1,1,3,1,2,1
'''.strip().split(',')

#%% Part 1: How many lanternfish after 80 days?

# Set up our "fish" dictionary
fish = dict()
for x in range(9):
    fish[x] = 0
empty_dict = fish.copy()
for x in input:
    fish[int(x)] += 1
    
for _ in range(80):
    d2 = empty_dict.copy()
    for d in range(9):
        if d == 0:
            d2[6] += fish[0]
            d2[8] += fish[0]
        else:
            d2[d-1] += fish[d]
    fish = d2.copy()
print(sum([x for x in d2.values()]))

#%% Part 2
"""
Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?

After 256 days in the example above, there would be a total of 26984457539 lanternfish!

How many lanternfish would there be after 256 days?
"""

# Set up our "fish" dictionary
fish = dict()
for x in range(9):
    fish[x] = 0
empty_dict = fish.copy()
for x in input:
    fish[int(x)] += 1
    
for _ in range(256):
    d2 = empty_dict.copy()
    for d in range(9):
        if d == 0:
            d2[6] += fish[0]
            d2[8] += fish[0]
        else:
            d2[d-1] += fish[d]
    fish = d2.copy()
print(sum([x for x in d2.values()]))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 23:02:40 2021

@author: aboisvert
"""

_input = '''
mx-IQ
mx-HO
xq-start
start-HO
IE-qc
HO-end
oz-xq
HO-ni
ni-oz
ni-MU
sa-IE
IE-ni
end-sa
oz-sa
MU-start
MU-sa
oz-IE
HO-xq
MU-xq
IE-end
MU-mx
'''.strip().split('\n')

# For testing
"""
_input = '''
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
'''.strip().split('\n')
"""


paths = dict()
for line in _input:
    c1, c2 = line.split('-')
    paths[c1] = paths.get(c1, set()).union(set([c2]))
    paths[c2] = paths.get(c2, set()).union(set([c1]))
    
#%% Part 1
# How many paths through this cave system are there that visit small caves at most once?
ctr = 0
all_paths = [['start']]
new_paths = all_paths.copy()
while new_paths:
    new_paths1 = []
    for p in new_paths:
        prev_visited = set([_ for _ in p if _.islower()])
        last_node = p[-1]
        if last_node == 'end':
            continue
        new_nodes1 = paths[last_node].difference(prev_visited)
        for nn in new_nodes1:
            new_paths1.append(p + [nn])
    new_paths = new_paths1.copy()
    all_paths = all_paths + new_paths
    ctr += 1
    #if ctr >= 3:
    #    break

good_paths = [x for x in all_paths if x[-1] == 'end']
print(len(good_paths))

#%% Part 2
"""
After reviewing the available paths, you realize you might have time 
to visit a single small cave twice.
Given these new rules, how many paths through this cave system are there?
"""
from collections import Counter

ctr = 0
all_paths = [['start']]
new_paths = all_paths.copy()
while new_paths:
    new_paths1 = []
    for p in new_paths:
        # prev_visited is sort of the same as before
        # except we only count it if something is there more than once
        prev_visited1 = [_ for _ in p if _.islower()]
        prev_visited_numbers = set(Counter(prev_visited1).values())
        if 2 in prev_visited_numbers:
            prev_visited = prev_visited1.copy()
        else:
            # We can re-visit anywhere except the start
            prev_visited = set(['start'])
        last_node = p[-1]
        if last_node == 'end':
            continue
        new_nodes1 = paths[last_node].difference(prev_visited)
        for nn in new_nodes1:
            new_paths1.append(p + [nn])
    new_paths = new_paths1.copy()
    all_paths = all_paths + new_paths
    ctr += 1
    #if ctr >= 3:
    #    break

good_paths = [x for x in all_paths if x[-1] == 'end']
print(len(good_paths))


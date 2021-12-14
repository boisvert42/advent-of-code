#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:17:50 2021

@author: aboisvert
"""

"""
The submarine manual contains instructions for finding the optimal polymer formula; specifically, it offers a polymer template and a list of pair insertion rules (your puzzle input). You just need to work out what polymer would result after repeating the pair insertion process a few times.
"""

_input = '''
PBVHVOCOCFFNBCNCCBHK

FV -> C
SS -> B
SC -> B
BP -> K
VP -> S
HK -> K
FS -> F
CC -> V
VB -> P
OP -> B
FO -> N
FH -> O
VK -> N
PV -> S
HV -> O
PF -> F
HH -> F
NK -> S
NC -> S
FC -> H
FK -> K
OO -> N
HP -> C
NN -> H
BB -> H
CN -> P
PS -> N
VF -> S
CB -> B
OH -> S
CF -> C
OK -> P
CV -> V
CS -> H
KN -> B
OV -> S
HB -> C
OS -> V
PC -> B
CK -> S
PP -> K
SN -> O
VV -> C
NS -> F
PN -> K
HS -> P
VO -> B
VC -> B
NV -> P
VS -> N
FP -> F
HO -> S
KS -> O
BN -> F
VN -> P
OC -> K
SF -> P
PO -> P
SB -> O
FN -> F
OF -> F
CP -> C
HC -> O
PH -> O
BC -> O
NO -> C
BH -> C
VH -> S
KK -> O
SV -> K
KB -> K
BS -> S
HF -> B
NH -> S
PB -> N
HN -> K
SK -> B
FB -> F
KV -> S
BF -> S
ON -> S
BV -> P
KC -> S
NB -> S
NP -> B
BK -> K
NF -> C
BO -> K
KF -> B
KH -> N
SP -> O
CO -> S
KO -> V
SO -> B
CH -> C
KP -> C
FF -> K
PK -> F
OB -> H
SH -> C
'''.strip().split('\n')

# Test input
"""
_input = '''
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
'''.strip().split('\n')
"""

# All the insertions happen simultaneously

INITIAL_POLYMER = _input[0]
INSERTIONS = dict()
for i in range(len(_input)):
    if i < 2:
        continue
    k, v = _input[i].split(' -> ')
    INSERTIONS[k] = v
    
def make_insertions(polymer):
    p2 = ''
    for i in range(len(polymer) - 1):
        pair = polymer[i:i+2]
        p2 += pair[0] + INSERTIONS.get(pair, '')
    p2 += polymer[-1]
    return p2

#%% Part 1

"""
Apply 10 steps of pair insertion to the polymer template and find the most 
and least common elements in the result. What do you get if you take the 
quantity of the most common element and subtract the quantity of the least common element?
"""

from collections import Counter
p2 = INITIAL_POLYMER
for _ in range(10):
    p2 = make_insertions(p2)

counts = Counter(p2)
print(counts)
min_v = min(counts.values())
max_v = max(counts.values())
print(max_v - min_v)

#%% Part 2

"""
Apply 40 steps of pair insertion to the polymer template and find the most 
and least common elements in the result. What do you get if you take the 
quantity of the most common element and subtract the quantity of the least common element?
"""

# This is too slow with the above method
# Instead let's track our polymer as a bunch of pairs
# We also keep track of the first and last elements, so they don't get half-counted
FIRST_ELEMENT = INITIAL_POLYMER[0]
LAST_ELEMENT = INITIAL_POLYMER[-1]

INITIAL_POLYMER_DICT = dict((k, 0) for k in INSERTIONS.keys())
for i in range(len(INITIAL_POLYMER) - 1):
    pair = INITIAL_POLYMER[i:i+2]
    INITIAL_POLYMER_DICT[pair] += 1
    
def make_insertions2(p_dict):
    pd2 = p_dict.copy()
    pd_pos = dict((k, v) for k, v in p_dict.items() if v  > 0)
    for pair, val in pd_pos.items():
        if INSERTIONS[pair]:
            new_pairs = (pair[0] + INSERTIONS[pair], INSERTIONS[pair] + pair[1])
        else:
            new_pairs = (pair,)
        for np in new_pairs:
            pd2[np] += val
        pd2[pair] -= val
    return pd2

def count_elements(p_dict):
    ret = dict()
    for pair, v in p_dict.items():
        for elt in pair:
            ret[elt] = ret.get(elt, 0) + v
    ret[FIRST_ELEMENT] += 1
    ret[LAST_ELEMENT] += 1
    for k, v in ret.items():
        ret[k] = ret[k]//2
    return ret

pd2 = INITIAL_POLYMER_DICT.copy()
for _ in range(40):
    pd2 = make_insertions2(pd2)
    
counts = count_elements(pd2)
min_v = min(counts.values())
max_v = max(counts.values())
print(max_v - min_v)




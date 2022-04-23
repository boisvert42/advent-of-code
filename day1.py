# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 21:11:53 2020

@author: boisv

Advent of code 2020
Puzzle 1

After saving Christmas five years in a row, you've decided to take a vacation 
at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. 
The gold coins used there have a little picture of a starfish; the locals just 
call them stars. None of the currency exchanges seem to have heard of them, 
but somehow, you'll need to find fifty of these coins by the time you arrive 
so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each 
day in the Advent calendar; the second puzzle is unlocked when you complete the first. 
Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report 
(your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then
 multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

To begin, get your puzzle input.
"""

input = '''1864
1192
1802
1850
1986
1514
1620
1910
1557
1529
1081
1227
1869
1545
1064
1509
1060
1590
1146
1855
667
1441
1241
1473
1321
1429
1534
1959
1188
1597
1256
1673
1879
1821
1423
1838
1392
1941
1124
1629
1780
1271
1190
1680
1379
1601
1670
1916
1787
1844
2000
1672
1276
1896
1746
1369
1687
1263
1948
1159
1710
1304
1806
1709
1286
1635
1075
1125
1607
1408
1903
1143
1736
1266
1645
1571
1488
1200
211
1148
1585
2005
1724
1071
1690
1189
1101
1315
1452
1622
1074
1486
1209
1253
1422
1235
1354
1399
1675
241
1229
1136
1901
1453
1344
1685
1985
1455
1764
1634
1935
1386
1772
1174
1743
1818
1156
1221
167
1398
1552
1816
1197
1829
1930
1812
1983
1185
1579
1928
1892
1978
1720
1584
1506
1245
1539
1653
1876
1883
1982
1114
1406
2002
1765
1175
1947
1519
1943
1566
1361
1830
1679
999
1366
1575
1556
1555
1065
1606
1508
1548
1162
1664
1525
1925
1975
1384
1076
1790
1656
1578
1671
1424
757
1485
1677
1583
1395
1793
1111
1522
1195
1128
1123
1151
1568
1559
1331
1191
1753
1630
1979
953
1480
1655
1100
1419
1560
1667'''
nums = set(int(x) for x in input.strip().split('\n'))

for x in nums:
    if 2020 - x in nums:
        print(x, 2020-x, x * (2020-x))
        
#%%
"""
Part 2
The Elves in accounting are thankful for your help; one of them even offers 
you a starfish coin they had left over from a past vacation. They offer you a 
second one if you can find three numbers in your expense report that meet the 
same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 
366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
"""
for x in nums:
    for y in nums:
        if 2020-(x+y) in nums:
            print(x, y, 2020-x-y, x*y*(2020-x-y))
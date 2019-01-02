#!/usr/bin/env python
# -*- coding:utf-8 -*-

s = 'abcdefg'
for (index, char) in enumerate(s):
    print(index)
    print(char)

ta = [4, 5, 6]
tb = [1, 2, 3]
tc = ['a', 'b', 'c', 'd']
for (a, b, c) in zip(ta, tb, tc):
    print(a, b, c)

ta = [1, 2, 3]
tb = [9, 8, 7]

# cluster
zipped = zip(ta, tb)
print(zipped)

# decompose
na, nb = zip(*zipped)
print(na, nb)

#!/usr/bin/env python
# -*- coding:utf-8 -*-

li1 = ['a', 'b', 'c']
li2 = [65, 66, 67]

# 列表解析
li = [x + str(y) for x, y in zip(li1, li2)]
print(li)

# 元组解析
t = tuple(i for i in list(map(lambda x, y: str(ord(x)) + str(y), li1, li2)))
print(t)

# 集合解析
s = {ord(x) + y for x, y in zip(li1, li2)}
print(s)

# 字典解析
d = {x: chr(y) for x, y in zip(li1, li2)}
print(d)

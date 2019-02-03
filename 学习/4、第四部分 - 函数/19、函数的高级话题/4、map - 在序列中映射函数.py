#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
map(func, seq)
对一个序列对象中的所有元素应用被传入的函数
返回一个包含所有函数调用结果的列表
"""

# 示例一、map 应用-------------------------------------------------------------
counters = [1, 2, 3, 4, 5]
# map 与 lambda 的组合
res = list(map(lambda x: x + 3, counters))
print(res)


# map 与 def 的组合
def adds(x):
    return x + 3


res = list(map(adds, counters))
print(res)

# 用 for 循环实现
res = []
for x in counters:
    res.append(x + 3)
print(res)

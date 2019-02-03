#!/usr/bin/env python
# -*- coding:utf-8 -*-
from functools import reduce
import operator
"""
filter
基于某一测试函数过滤出一些元素

reduce
对每对元素都应用函数并运行到最后结果

"""


# 示例一、filter 的应用--------------------------------------------------------
li = list(range(-5, 5))
# 使用 filter 函数
res = list(filter(lambda x: x > 0, li))
print(res)

# 使用 for 循环
res = []
for x in li:
    if x > 0:
        res.append(x)
print(res)

# 示例二、reduce 的应用--------------------------------------------------------
li = [1, 2, 3, 4]
# 使用 reduce 函数
res = reduce(lambda x, y: x + y, li)  # 其实这个使用 sum(li) 更简单
print(res)
res = reduce(lambda x, y: x * y, li)
print(res)

# 使用 for 循环
res = li[0]
for x in li:
    res += x
print(res)

res = 1
for x in li:
    res *= x
print(res)


# 示例三、模拟 reduce 函数-----------------------------------------------------
def myreduce(func, seq):
    res = seq[0]
    for next in seq[1:]:
        res = func(res, next)
    return res
res = myreduce(lambda x, y: x + y, li)
print(res)
res = myreduce(lambda x, y: x * y, li)
print(res)

# 示例四、reduce 函数与 operator 模块------------------------------------------
res = reduce(operator.sub, li)
print(res)
res = reduce(operator.truediv, li)
print(res)

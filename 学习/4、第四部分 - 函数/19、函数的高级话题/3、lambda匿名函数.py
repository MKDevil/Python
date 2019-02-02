#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
lambda 是一个表达式，不是语句
lambda 后跟一个或多个参数，然后一个冒号，接着一个表达式
lambda argument1, argument2, argument3, ... argumentN: expression
"""


# 示例一，def 与 lambda 互换
def func(a, b, c):
    return a + b + c


print(func(1, 2, 3))

lam = lambda x, y, z: x + y + z  # 不建议这样使用 lambda 表达式
print(lam(1, 2, 3))


# def 与 lambda 嵌套使用
def knights():
    title = 'Sir'
    action = lambda x: title + ' ' + x  # 不建议这样使用 lambda 表达式
    return action


act = knights()
print(act('ass'))

# 示例二，lambda 条件语句------------------------------------------------------
lower = lambda x, y: x if x < y else y
print(lower(5, 3))

# 示例三，lambda 循环----------------------------------------------------------
import sys
showall = lambda x: [sys.stdout.write(line) for line in x]

print(showall(('ass ', 'we ', 'can')))


# 示例四，嵌套 lambda 和作用域-------------------------------------------------
def action(x):
    return lambda y: x + y

act = action(99)
print(act(1))


action = lambda x: (lambda y: x + y)

act = action(99)
print(act(1))

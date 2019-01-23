#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
nonlocal 类似于 global，声明了将要在一个嵌套的函数作用域中的一个名称
nonlocal 仅限于向上一层的 def 作用域
nonlocal 只能存在于嵌套的 def 中
"""


# 示例一，错误的示范
def tester(start):
    state = start

    def nested(label):
        print(label, state)
        state += 1
    return nested


f = tester(0)
try:
    f('spam')
except Exception as e:
    print('出现错误：', e)

# 示例二，修改
def tester(start):
    state = start

    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested


f = tester(0)
f('spam')
f('ham')
f('faq')

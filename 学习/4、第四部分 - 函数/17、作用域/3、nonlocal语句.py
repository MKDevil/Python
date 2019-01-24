#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
nonlocal 类似于 global，声明了将要在一个嵌套的函数作用域中的一个名称
nonlocal 仅限于向上一层的 def 作用域
nonlocal 只能存在于嵌套的 def 中，且上层 def 必须定义了指定变量，否则报错
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

# 示例三，不在上层 def 定义 nonlocal 指定的变量
state = 0


def tester():

    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested


f = tester()
f('spam')
f('ham')
f('faq')

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

"""
def 是可执行的代码
def 创建一个对象并将其赋值给某一个变量名
lambda 创建一个对象并将其作为结果返回
return 将一个结果对象发送给调用者
yield 向调用者发回一个结果对象，但是记住它离开的地方
global 声明了一个模块级的变量并被赋值
nonlocal 声明了将要赋值的一个封闭的函数变量
"""

# def 语句
"""
def <name>(arg1, arg2, ... argN):
    <statement>
    return <value>
return 语句是可选的，不加 return 语句则返回 None
return 语句在执行后，自动忽略后续语句（类似于break）
"""


# 示例，获取两个集合的交集
def intersect(li1, li2):
    res = []
    for i in li1:
        if i in li2:
            res.append(i)
    return res


print(intersect([1, 2, 3, 4, 5, 6], [2, 4, 6, 7, 19]))


# 示例，删除列表中的重复项，也可作用于字符串
def del_repeat(li):
    res = []
    for i in li:
        if i not in res:
            res.append(i)
    return res


li1 = [random.randint(0, 32) for i in range(32)]
print(sorted(del_repeat(li1)))

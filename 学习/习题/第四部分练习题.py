#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 2、参数-----------------------------------------------------------------------
def adder(a, b):
    return a + b


print(adder('111', '222'))
print(adder([1, 2, 3], [3, 4, 5]))
print(adder(2.232, 3.231))


# 3、可变参数-------------------------------------------------------------------
def adder(*args):
    res = args[0]
    for i in args[1:]:
        res += i
    return res


print(adder('111', '222'))
print(adder([1, 2, 3], [3, 4, 5]))
print(adder(2.232, 3.231))
# print(adder(a=1, b=2, c=3, {'c': 3}))  # 无法解析字典


# 4、关键字参数-----------------------------------------------------------------
def adder(good=10, bad=20, ugly=30):
    return good + bad + ugly


print(adder())
print(adder(1, 2, 3))
print(adder(1, 2))
print(adder(ugly=2, good=3))


# 拓展到字典
def adder(**args):
    args = list(args.values())
    res = args[0]
    for i in args[1:]:
        res += i
    return res


print(adder(a=1, b=2, c=3))


#

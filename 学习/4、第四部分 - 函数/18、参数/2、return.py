#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 示例一，return 语句返回多个值------------------------------------------------
# 当 return 返回多个值时，实际上是返回了这些值组成的一个元组
def change(a, b):
    return a, b

a = 'spam'
b = [1, 2]
c = change(a, b)
d, e = change(a, b)
print(c)
print(d, e)

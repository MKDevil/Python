#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 使用函数属性来保存函数状态，可以实现类似于 nonlocal 的效果
def tester(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1
    nested.state = start
    return nested


f = tester(0)
f('a')
f('b')
g = tester(20)
g('c')
g('d')
f('e')
